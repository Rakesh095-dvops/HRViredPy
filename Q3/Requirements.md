# Python Exercise

## Question 3

In DevOps, automating configuration management tasks is essential for maintaining consistency and managing infrastructure efficiently.

●       The program should read a configuration file (you can provide them with a sample configuration file).

●       It should extract specific key-value pairs from the configuration file.

●       The program should store the extracted information in a data structure (e.g., dictionary or list).

●       It should handle errors gracefully in case the configuration file is not found or cannot be read.

●       Finally save the output file data as JSON data in the database.

●       Create a GET request to fetch this information.

```

Sample Configuration file: 

[Database]

host = localhost

port = 3306

username = admin

password = secret

 
[Server]

address = 192.168.0.1

port = 8080
```
```
Sample Output: 

Configuration File Parser Results:

Database:

- host: localhost

- port: 3306

- username: admin

- password: secret
 

Server:

- address: 192.168.0.1

- port: 8080 
```