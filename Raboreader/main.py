'''
Created on 1 feb. 2016

@author: Timo
'''

import csv, sys
from Raboreader.Rabo2Ynab import Rabo2Ynab

if __name__ == '__main__':
    filename_in = 'C:/Users/Timo/Documents/LiClipse Workspace/Raboreader/resource/transactions.csv'
    dir_out = 'C:/Users/Timo/Documents/LiClipse Workspace/Raboreader/output/'

    Converter = Rabo2Ynab(filename_in, dir_out  )
    Converter.read()
    Converter.convert( )
    Converter.write( )
    
    print('succes')
            
    
                
            
                    
            
        