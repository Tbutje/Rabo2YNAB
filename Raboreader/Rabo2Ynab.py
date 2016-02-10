
from Raboreader.RowReader import RowReader
import csv, sys

class Rabo2Ynab(object):

    mv_file_in = 'init'
    mv_dir_out = 'init'
    mt_accounts = []
    mt_data = []   

    def __init__(self, file_in, dir_out):
        self.mv_file_in = file_in
        self.mv_dir_out = dir_out
        
    def read(self):
        try:
            with open(self.mv_file_in) as File:
                
                lr_reader = csv.reader(File)
                for ls_row in lr_reader:
                    lr_rowReader = RowReader(ls_row)
                    
#                   add acount when not existing yet, otherwise get index
                    if not ls_row[0] in self.mt_accounts:
                        self.mt_data.append([])
                        self.mt_accounts.append(ls_row[0])
                        lv_account_idx = len(self.mt_accounts) - 1
                    else:
                        lv_account_idx = self.mt_accounts.index(ls_row[0])
                        
                    ls_data = { 'date':     lr_rowReader.get_date(),
                               'payee':     lr_rowReader.get_payee(),
                               'category':  lr_rowReader.get_category(),
                                'memo':     lr_rowReader.get_memo(),
                                'out':      lr_rowReader.get_outflow(),
                                'in':       lr_rowReader.get_inflow() }
                    self.mt_data[lv_account_idx].append(ls_data)
                        
        except IOError:
            sys.exit( "input file error",
                      "input file not found\nplease check the input file name")
            
    
    def write(self):
        ls_data = {}
        for idx, lv_account in enumerate(self.mt_accounts):
#             check if we have that weird windows directory 
#             or normal input from command line
            if self.mv_dir_out.find('\\') > 0:
                lv_filename = self.mv_dir_out + '\\' + lv_account + '.csv'
            else:
                lv_filename = self.mv_dir_out + lv_account + '.csv'
            
            try:
                with open(lv_filename, 'w+', newline='') as lr_file:
                    lr_writer = csv.writer(lr_file, quoting=csv.QUOTE_NONNUMERIC)
                    
#                   write header row
                    lr_writer.writerow([ 'Date' , 'Payee' , 'Category' , \
                                      'Memo' , 'Outflow' , 'Inflow' ])
                
#                   write the rest
                    for jdx, ls_data in enumerate(self.mt_data[idx]):
                        lr_writer.writerow([ls_data.get('date'), \
                                            ls_data.get('payee'), \
                                            ls_data.get('category'), \
                                            ls_data.get('memo'), \
                                            ls_data.get('out'), \
                                            ls_data.get('in')])
            except IOError:
                sys.exit( "Output file error" )
        
      
        
