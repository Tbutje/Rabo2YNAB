# Rabobank2YNAB
This is a very simple program to convert Rabobank csv files to a format suited for YNAB
Rabobank has 1 file / export, while YNAB has 1 file / account. Also there are some minor
other formatting differences between the two. this simple python program converts the
Rabobank file to the YNAB file(s)

# It can be run two ways:
## just run:
this will attampt to look for a file "transactions.csv" in the dir of main.

## commandline args
call main.py with command line args. First argument is dir in. Second argument is dir out.