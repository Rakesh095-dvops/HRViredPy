import os,sys,time,shutil

def backup_files(source_dir, dest_dir):
    """
    Copies all files from the source directory to the destination directory,
    appending a timestamp to filenames if a file with the same name already exists.

    Error: 
    exit if source and destination directory  doesn't exit 
    
    Console:
    Add sucessfull message of copy of file
    """
    try:
        src_dir_exst =True
        src_dest_exst = True
        # Check if source directory exists
        if not os.path.exists(source_dir):
            src_dir_exst=False
            raise ValueError(f"Source directory '{source_dir}' does not exist.")

        # Check if destination directory exists
        if not os.path.exists(dest_dir):
            src_dest_exst=False
            raise ValueError(f"Destination directory '{dest_dir}' does not exist")
        
        #Recursive folder search and folder creation - Not in scope.

        # Iterate over all files in the source directory based on condition 
        if(src_dir_exst and src_dest_exst ):
            for filename in os.listdir(source_dir):
                source_path = os.path.join(source_dir, filename)
                # Check if it's a file (not a directory)
                if os.path.isfile(source_path):
                    dest_path = os.path.join(dest_dir, filename)
                    if os.path.exists(dest_path):
                    # Append timestamp to filename to ensure uniqueness
                        name, ext = os.path.splitext(filename)
                        timestamp = time.strftime("%Y%m%d%H%M%S")
                        new_filename = f"{name}_{timestamp}{ext}"
                        dest_path = os.path.join(dest_dir, new_filename)
                        print(f"File '{filename}' already exists in destination.  Saving as '{new_filename}'.")                   
                # Copy the file
                    try:
                        shutil.copy2(source_path, dest_path)  # copy2 preserves metadata
                        print(f"Successfully backed up '{filename}' to '{dest_path}'.")
                    except Exception as copy_err:
                        print(f"Error copying '{filename}': {copy_err}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Check for correct number of arguments
    if len(sys.argv) != 3:
        print("Usage: python backup.py /path/to/source /path/to/destination")
        print("\n")
        print("Usage: Provide syntax as mentioned above")
        sys.exit(1)

    source_directory = sys.argv[1]
    destination_directory = sys.argv[2]
    print("subdirectory copy not supported for current subroutine\n")
    backup_files(source_directory, destination_directory)