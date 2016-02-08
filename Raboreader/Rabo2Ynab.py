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
    file_in     = 'init'
    dir_out     = 'init'
    accounts    = []
    tData       = []   


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
#                   add acount when not existing yet, otherwise get index
                    if not row[0] in self.accounts:
                        self.tData.append([])
                        self.accounts.append(row[0])
                        account_idx = len(self.accounts) - 1
                    else:
                        account_idx = self.accounts.index(row[0])
                        
                    row_res = { 'date':     rowReader.get_date(),
                               'payee':     rowReader.get_payee(), 
                               'category':  rowReader.get_category(),
                                'memo':     rowReader.get_memo(),
                                'out':      rowReader.get_outflow(),
                                'in':       rowReader.get_inflow() }
                    self.tData[account_idx].append(row_res)
                        
        except IOError:
            sys.exit(
                        "input file error",
                        "input file not found\nplease check the input file name"
                    )
            
    
    def write(self):
        print(1)    
        
 
        
      
        