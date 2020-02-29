# Database Logger

Reads TCPDump logfiles and parses them into either a SQLite
database or a comma seperated text file.  

Requires Python 3.7+.

## How to use

Install dependencies via `pip install -r requirements.txt`.  
After that you may use the program from Command-Line with
the corresponding parameters.  
Example:  
````cmd
python3.7 main.py -i dump.txt -o logger.db --saveto=db
````

The following parameters are supported:  

-i (required)  
The path to your input logfile, this file will not be modified 
in any way.  
May be any logfile with the standard TCPDump Syntax.  

-o (required)  
The path to your desired output logfile, 
please use a full filename ending with either .txt or .db, 
depending on wether you chose to save to a database or a file.  
As .txt files specified here will be overwritten during 
operation it is required to give a path to a new textfile.  
Databases will not be overwritten.  

--saveto=file|db  
Optional parameter that determines wether to save to a database
 or a textfile, defaults to file.  
Only two values are accepted: ‚file‘ and ‚db‘.  
Please note that if the value is set to ‚db‘ the outputfile 
must be a .db file.

## Clone this Project

````cmd
git clone https://www.github.com/ThaRising/database-logger.git
````

Setup venv:
````
# When using pip:
pip install -r requirements.txt
# For conda users:
conda env update --file environment.yml
````

To run the main program simply run main.py as the entry-point.  
Tested on Windows and Debian using Python 3.7.