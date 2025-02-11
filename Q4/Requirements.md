# Python Exercise

## Question 4

Q4. In DevOps, performing regular backups of important files is crucial:

● Implement a Python script called backup.py that takes a source directory and a destination directory as command-line arguments.

● The script should copy all files from the source directory to the destination directory.

● Before copying, check if the destination directory already contains a file with the same name. If so, append a timestamp to the file name to ensure uniqueness.

● Handle errors gracefully, such as when the source directory or destination directory does not exist.

Sample Command:

python backup.py /path/to/source /path/to/destination

By running the script with the appropriate source and destination directories, it should create backups of the files in the source directory, ensuring unique file names in the destination directory.