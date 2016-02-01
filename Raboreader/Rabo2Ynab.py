'''
Created on 1 feb. 2016

@author: Timo
'''
from Raboreader.RowReader import RowReader
import csv, sys

class Rabo2Ynab(object):
    '''
    classdocs
    '''
    file_in = 'init'
    dir_out = 'init'
    date        = []
    payee       = []
    category    = []
    memo        = []
    outflow     = []
    inflow      = []


    def __init__(self, file_in, dir_out):
        self.file_in = file_in
        self.dir_out = dir_out
        
    def read(self):
        try:
            with open(self.file_in) as File:
                
                reader = csv.reader(File)
    #             Skip first line
                next(reader, None)
                for row in reader:
                    rowReader = RowReader( row )
                    self.date.append(rowReader.get_date())
                    self.payee.append(rowReader.get_payee())     
                    self.category.append(rowReader.get_category())
                    self.memo.append(rowReader.get_memo())      
                    self.outflow.append(rowReader.get_outflow())   
                    self.inflow.append(rowReader.get_inflow())    
        except IOError:
            sys.exit(
                        "input file error",
                        "input file not found\nplease check the input file name"
                    )
            
    
    def convert(self):
        print(5)
        
    def write(self):
        print(1)    
        
 
        
      
        