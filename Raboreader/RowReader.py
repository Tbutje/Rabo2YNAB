
class RowReader(object):

    ms_row = []
    coCrediteurenBetaling = 'cb'
    coDiverseBoekingen = 'db'
    coGeldAutomaat = 'ga'
    coBetaalAutomaat = 'ba'
    coBetaalContactLoos = 'bc'
    coBankGiro = 'bg'
    coEuroIncasso = 'ei'
    coIdeal = 'id'
    coEigenRek = 'tb'

    def __init__(self, row):
        self.ms_row = row
        
    def get_date(self):
        lv_year = self.ms_row[2][0:4]
        lv_month = self.ms_row[2][4:6]
        lv_day = self.ms_row[2][6:8]
        return lv_day + '/' + lv_month + '/' + lv_year
    def get_payee(self):
        lv_pay_type = self.ms_row[8]
        if (self.ms_row[8] == self.coGeldAutomaat
        or   self.ms_row[8] == self.coBetaalAutomaat
        or   lv_pay_type == self.coBetaalContactLoos) :
            return self.ms_row[10]  
        
        elif (lv_pay_type == self.coBankGiro
             or lv_pay_type == self.coCrediteurenBetaling
             or lv_pay_type == self.coEuroIncasso
             or lv_pay_type == self.coIdeal
             or lv_pay_type == self.coEigenRek):
            return self.ms_row[5] + " - " + self.ms_row[6]
        
        elif self.ms_row[8] == self.coDiverseBoekingen :
            return self.ms_row[6] + ' - ' + self.ms_row[10]

        else:
            return self.ms_row[5]
          
   
    def get_category(self): 
        return ''
    
    def get_memo(self):  
        idx = 10
        lv_msg = ''
        while(not self.ms_row[idx] == ''):
            lv_msg = lv_msg + self.ms_row[idx]
            idx = idx + 1
#           prevent out of index size  
            if idx > 18:
                break
        return lv_msg
       
    def get_outflow(self):  
        if self.ms_row[3] == 'D':
            return self.ms_row[4]
        else:
            return ''
                
    
    def get_inflow(self): 
        if self.ms_row[3] == 'C':
            return self.ms_row[4]
        else:
            return ''
