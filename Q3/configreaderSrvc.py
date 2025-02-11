from flask import Flask, json,request,jsonify,abort
from pymongo import MongoClient, ReturnDocument
from flask_pymongo import PyMongo
from bson import ObjectId
import re,os,configparser
import itertools

app = Flask(__name__)
mongo_uri = "mongodb+srv://dbuser:tUmusUV3MteObgt179ou@cluster0.i0pov.mongodb.net/?retryWrites=true&w=majority" 
# Connect to MongoDB
client = MongoClient(mongo_uri)
# Access the  database
database_name = 'config_db'
# Access the  collection
collection_name = 'configs'


def requestvalidation(_data):
    """
        Validate the Body of the request for POST 
    """
    if not any([
        _data.get("config_path"), 
        ]):
        return False  # At least path need to be provided
    else:
        return True
def validate_file_path(file_path):
    """
        Validate the config file  in the Client OS 
    """
    if not os.path.exists(file_path):
        return False

    if not os.path.isfile(file_path):
        return False
    return True
def load_keys_to_extract_from_config(config_path):
    """
        Genric function to read each element header from config 
    """
    try:
        config = configparser.ConfigParser(allow_no_value=True,comment_prefixes='#',delimiters='=')
        config.read_string(config_path)
        keys_to_extract = {}
        print(config.sections())
        for section in config.sections():
            keys_to_extract[section] = list(config.options(section))  # Get all keys in section
        return keys_to_extract
    except Exception as e:
        print(f"Error loading keys to extract: {e}")
        return None
def parse_config_string(config_path, keys_to_extract):
    try:
        config = configparser.ConfigParser(allow_no_value=True,comment_prefixes='#',delimiters='=')
        config.read_string(config_path)
        config_data = {}
        for section in config.sections():
            if section in keys_to_extract:
                config_data[section] = {}
                for key in keys_to_extract[section]:
                    if key in config[section]:
                        config_data[section][key] = config[section][key]
                    else:
                        print(f"Warning: Key '{key}' not found in section '{section}'")
        return config_data
    except Exception as e:
        print(f"Error: An error occurred while parsing the configuration string: {e}")
        return None
    
def save_to_mongodb(config_data):
    """
        Saving the data to mongo DB 
    """
    try:
        client = MongoClient(mongo_uri)
        db = client[database_name]
        collection = db[collection_name]
        # Insert the new configuration data
        collection.insert_one(config_data)
        client.close()
        return True
    except Exception as e:
        print(f"Error: An error occurred while saving to MongoDB: {e}")
        return False

    
def get_frm_mngodb():
    """
        Getting config data from MongoDB 
    """
    try:
        client = MongoClient(mongo_uri)
        db = client[database_name]
        config_collection = db[collection_name]
        config_data=[{**configs,'_id':str(configs['_id'])}for configs in config_collection.find()]
        client.close()
        #print(type(config_data))
        #print(config_data)
        return config_data
    except Exception as e:
        print(f"Error: An error occurred while retrieving data from MongoDB: {e}")
        return jsonify({"Error: An error occurred while retrieving data from MongoDB:": f"{e}"}), 500 # Internal Server Error


##API endpoint to Save the configuration data from MongoDB.
@app.route("/config", methods=['POST'])
def save_config():
    try:
        # Get the configuration data from the request body
        data=request.get_json()
        print(data)
        #validate the file path
        if (requestvalidation(data)):
            data['config_path']=str(data['config_path'])
        config_path=data['config_path']
        file_exist=validate_file_path(config_path)
        if file_exist == False:
            return ({"Error": f"File Doesn't exit in path {config_path}"}),500
            abort(500)
        else:
            with open(config_path, 'r') as f:
                config_string = f.read()
            # Load KEYS_TO_EXTRACT from the config string
            keys_to_extract = load_keys_to_extract_from_config(config_string)
            print(keys_to_extract)             
            # Parse the configuration data and convert to 
            config_data = parse_config_string(config_string, keys_to_extract)
            print(type(config_data))
            print(config_data)
            if config_data:
            # Save the configuration data to MongoDB
                if save_to_mongodb(config_data):
                    return jsonify({"Message": "Configuration data saved to MongoDB successfully."}), 201  # Created
                else:
                    return jsonify({"Error": "Failed to save configuration data to MongoDB."}), 500  # Internal Server Error
            else:
                return jsonify({"Error": "Failed to parse configuration data."}), 400  # Bad Request
    except Exception as e:
        print(f"Error: An error occurred while processing the POST request: {e}")
        return jsonify({"Error": f"An error occurred: {e}"}), 500  # Internal Server Error

#API endpoint to retrieve all configuration data from MongoDB.
@app.route("/config", methods=['GET'])
def get_config():
        config_data=get_frm_mngodb()
        #print(todolists)
        if len(config_data) == 0:
            return jsonify({"Message": "No Configs exists in database."}),200
        else:
            return jsonify(config_data),201    


if __name__== "__main__":
    app.run(debug=True,port=5000)