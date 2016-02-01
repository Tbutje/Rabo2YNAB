'''
Created on 1 feb. 2016

@author: Timo
'''

import csv, sys
from Raboreader.CLRabo2Ynab import CLRabo2Ynab

if __name__ == '__main__':
    filename_in = 'C:/Users/Timo/Documents/LiClipse Workspace/Raboreader/resource/transactions.csv'
    date        = []; 
    payee       = [];
    category    = [];
    memo        = [];
    outflow     = [];
    inflow      = [];

    Converter = CLRabo2Ynab( )
    
    Converter.read( filename_in )
    Converter.convert( )
#     Converter.write( )
    
    
    try:
        with open(filename_in) as file_in:
                
            reader = csv.reader(file_in)
    #             Skip first line
            next(reader, None)
            for row in reader:
                date.append(row[2])
    except IOError:
        sys.exit(
                    "input file error",
                    "input file not found\nplease check the input file name"
                )
        
    print('succes')
            
    
                
            
                    
            
        