'''
Created on 1 feb. 2016

@author: Timo
'''

class RowReader(object):
    '''
    classdocs
    '''
    row = []


    def __init__(self, row):
        self.row = row
        
    def get_date(self):
        return self.row[2]
             
    def get_payee(self):
        if self.row[8] == "ga" :
            return self.row[9] + " - " + self.row[10]     
        elif self.row[8] == 'db':
            return self.row[5] + ' - '+ self.row[6]
        else:
            return self.row[5] + " - " + self.row[10];
          
#             case "ba": // betaalautomaat
#             case "ga": // geldautomaat
#             case "tb": // spaaropdracht?
#             case "ei": // europese incasso
#             case "cb": // crediteuren betaling (geld ontvangen)
#             case "bg": // betaling
#             case "db": // betaling aan bank
#                   
   
    def get_category(self): 
        return self.row[1]
    
    def get_memo(self):  
        return self.row[1]
       
    def get_outflow(self):  
        return self.row[1]
    
    def get_inflow(self): 
        return self.row[1]   