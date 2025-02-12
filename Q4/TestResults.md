## Testing 
### Console output - if syntax is not correct 
```
PS ~Q4> python backup.py 
Usage: python backup.py /path/to/source /path/to/destination


Usage: Provide syntax as mentioned above

```
#### Console output - where destination filepath is incorrect 
```
PS ~Q4> python backup.py C:/Devops/CodeBase/src C:/Devops/CodeBase/ds
An unexpected error occurred: Destination directory 'C:/Devops/CodeBase/ds' does not exist
```
### Console output - where source filepath is incorrect 

```
PS ~Q4> python backup.py C:/Devops/CodeBase/sr C:/Devops/CodeBase/dst             
An unexpected error occurred: Source directory 'C:/Devops/CodeBase/sr' does not exist.
```
#### Console output- source and destination file path are valid 
```
PS ~Q4> python backup.py C:/Devops/CodeBase/src C:/Devops/CodeBase/dst            
subdirectory copy not supported for current subroutine

Successfully backed up 'DevOps Roadmap-72.png' to 'C:/Devops/CodeBase/dst\DevOps Roadmap-72.png'.
Successfully backed up 'FORM12BB_signed.pdf' to 'C:/Devops/CodeBase/dst\FORM12BB_signed.pdf'.
Successfully backed up 'OldvsNewtaxRegime.xls' to 'C:/Devops/CodeBase/dst\OldvsNewtaxRegime.xls'.
Successfully backed up 'Readme.txt' to 'C:/Devops/CodeBase/dst\Readme.txt'.
Successfully backed up 'tax calculator old vs new.xlsx' to 'C:/Devops/CodeBase/dst\tax calculator old vs new.xlsx'.
```
#### Console output - source and destination file path are valid  and few SRC file already exist in dst location
```

PS~Q4> python backup.py C:/Devops/CodeBase/src C:/Devops/CodeBase/dst

subdirectory copy not supported for current subroutine

File 'DevOps Roadmap-72.png' already exists in destination.  Saving as 'DevOps Roadmap-72_20250213010720.png'.
Successfully backed up 'DevOps Roadmap-72.png' to 'C:/Devops/CodeBase/dst\DevOps Roadmap-72_20250213010720.png'.
File 'FORM12BB_signed.pdf' already exists in destination.  Saving as 'FORM12BB_signed_20250213010720.pdf'.
Successfully backed up 'FORM12BB_signed.pdf' to 'C:/Devops/CodeBase/dst\FORM12BB_signed_20250213010720.pdf'.
File 'OldvsNewtaxRegime.xls' already exists in destination.  Saving as 'OldvsNewtaxRegime_20250213010720.xls'.
Successfully backed up 'OldvsNewtaxRegime.xls' to 'C:/Devops/CodeBase/dst\OldvsNewtaxRegime_20250213010720.xls'.
File 'Readme.txt' already exists in destination.  Saving as 'Readme_20250213010720.txt'.
Successfully backed up 'Readme.txt' to 'C:/Devops/CodeBase/dst\Readme_20250213010720.txt'.
File 'tax calculator old vs new.xlsx' already exists in destination.  Saving as 'tax calculator old vs new_20250213010720.xlsx'.
Successfully backed up 'tax calculator old vs new.xlsx' to 'C:/Devops/CodeBase/dst\tax calculator old vs new_20250213010720.xlsx'.
```