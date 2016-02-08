'''
Created on 1 feb. 2016

@author: Timo
'''

class RowReader(object):

    row = []
    coCrediteurenBetaling   = 'cb'
    coDiverseBoekingen      = 'db'
    coGeldAutomaat          = 'ga'
    coBetaalAutomaat        = 'ba'
    coBetaalContactLoos     = 'bc'
    coBankGiro              = 'bg'
    coEuroIncasso           = 'ei'
    coIdeal                 = 'id'
    coEigenRek              = 'tb'

    def __init__(self, row):
        self.row = row
        
    def get_date(self):
        return self.row[2]
    def get_payee(self):
        pay_type = self.row[8]
        if ( self.row[8] == self.coGeldAutomaat
        or   self.row[8] == self.coBetaalAutomaat
        or   pay_type    == self.coBetaalContactLoos ) :
            return self.row[10]  
        
        elif (  pay_type == self.coBankGiro
             or pay_type == self.coCrediteurenBetaling
             or pay_type == self.coEuroIncasso
             or pay_type == self.coIdeal
             or pay_type == self.coEigenRek ):
            return self.row[5] + " - " + self.row[6]
        
        elif self.row[8] == self.coDiverseBoekingen :
            return self.row[6] + ' - '+ self.row[10]

        else:
            return self.row[5]
          
   
    def get_category(self): 
        return self.row[1]
    
    def get_memo(self):  
        return self.row[1]
       
    def get_outflow(self):  
        return self.row[1]
    
    def get_inflow(self): 
        return self.row[1]   