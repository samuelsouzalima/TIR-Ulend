from ast import NotIn
from investments import investments
from installments import installments
from datetime import datetime
from datetime import timedelta
import numpy_financial as npf

clientIDs = []

#// Construir a lista de ID's
for clientID in investments:
    clientIDs.append(clientID["id"])

def calc_irr():
    cashflows = {}
    data = []
    
    #// Para cada ID:
    for clientID in clientIDs:
        
        for investment in investments:
            if clientID == investment["id"]:
                #// Conversão de Datas:
                date_time_obj = datetime.strptime(investment["created_at"], '%Y-%m-%d')
                #// Adequação de Valores:
                investmentAmount=(-float(investment["amount"]))
                cashflows[date_time_obj]=investmentAmount

        for installment in installments:
            if clientID == installment["investment_id"]:
                date_time_obj = datetime.strptime(installment["due_date"], '%Y-%m-%d') 
                installmentAmount=(float(installment["amount"]))

                if date_time_obj in cashflows:
                    cashflows[date_time_obj]+=installmentAmount
                else:
                    cashflows[date_time_obj]=installmentAmount

        # minDate=min(cashflows.keys())
        # maxDate=max(cashflows.keys())
        # currentDate=minDate
        # while currentDate < maxDate:
        #     if currentDate not in cashflows:
        #         cashflows[currentDate]=0.0
        #     currentDate +=timedelta(days=1)

        cashflows=dict(sorted(cashflows.items()))    

        for amount in cashflows.values():
            data.append(amount)

        irr = round(npf.irr(data), 6)

        print("TIR para cliente de ID",clientID,":",irr)
        
        #// Clear:
        data = []
        cashflows = {}

if __name__ == "__main__":
    calc_irr()