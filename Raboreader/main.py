from Raboreader.Rabo2Ynab import Rabo2Ynab
import sys
import os

if __name__ == '__main__':
    
    if len(sys.argv) > 1:
        lv_filename_in = sys.argv[1]
        lv_dir_out = sys.argv[2]
    elif len(sys.argv) == 1:
        lv_filename_in = os.path.dirname(sys.argv[0]) + '\\transactions.csv'
        lv_dir_out = os.path.dirname(sys.argv[0]) 

    lr_converter = Rabo2Ynab(lv_filename_in, lv_dir_out)
    lr_converter.read()
    lr_converter.write()
    
    
                
            
                    
            
        
