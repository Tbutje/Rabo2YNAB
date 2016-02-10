# Rabobank2YNAB
This is a very simple program to convert Rabobank csv files to a format suited for YNAB
Rabobank has 1 file / export, while YNAB has 1 file / account. Also there are some minor
other formatting differences between the two. this simple python program converts the
Rabobank file to the YNAB file(s). No gui or anything fancy. Just plain commandline input ( or no input at all )

# It can be run two ways:
## Run main.py:
this will attampt to look for a file "transactions.csv" in the dir of main.

## Run main.py with commandline arguments
call main.py with commandline arguments. First argument is the input file (Example: "C:/transactions.csv") 
Second argument is the directory where the YNAB file(s) should be stored (Example: "C:/output/")
