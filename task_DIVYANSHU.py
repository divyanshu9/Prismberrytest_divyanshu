import sys
import ast

''' normalize function cancells credit to debt if same person has entry in both credit and debt dictionary '''

def normalize(debt,cred):
    #print(debt,cred)
    for i in list(cred):
        if i in debt:
            if cred[i]<debt[i]:
                debt[i] = debt[i] - cred[i]
                cred[i] = 0
                cred.pop(i)
            elif cred[i]>debt[i]:
                cred[i] = cred[i] - debt[i]
                debt[i] = 0
                debt.pop(i)
            else:
                cred.pop(i)
                debt.pop(i)
    return cred,debt


''' This creates to dictionaries cred and debt which represents total credit and debt for all persons '''

def minimize_transactions(trans_list):
    debt,cred = {},{}
    for trans in trans_list:
            if not trans[0] in debt:
               debt[trans[0]] = trans[2]
               #print('initialized debt %s with : %s'%(trans[0],trans[2]))
            else:
               debt[trans[0]] = debt[trans[0]] + trans[2]
               #print('increased debt %s with : %s'%(trans[0],debt[trans[0]]))
            if not trans[1] in cred:
               cred[trans[1]] = trans[2]
               #print('initialized cred %s with : %s'%(trans[1],trans[2]))
            else:
               cred[trans[1]] = cred[trans[1]] + trans[2]
               print('increased cred %s with : %s'%(trans[1],cred[trans[1]]))

    cred,debt = normalize(debt,cred)
    #print("normalized cred debt : ", cred,debt)
    count = 0
    
    ''' This chunk of code finds the final mininum no. of transactions that are needed to repay all debts '''
    
    for ctran in cred:
        for dtran in list(debt):
            if cred[ctran] == 0:
                    continue
            if cred[ctran]>=debt[dtran]:
                cred[ctran] = cred[ctran]-debt[dtran]
                print("%s gives Rs. %s to %s"%(dtran, debt[dtran], ctran))
                debt.pop(dtran)
                count += 1
            else:
                count += 1
                debt[dtran] = debt[dtran]-cred[ctran]
                print("%s gives Rs. %s to %s"%(dtran, cred[ctran], ctran))
    print("Min transaction needed : ",count)


if __name__ == "__main__":
    
    ''' Input is given in the form of list of tuples '''
    ''' Here a tuple represent single transaction for Ex. ('A','B',5000) means A owes Rs. 5000 to B '''
    
    try:
        trans_list = sys.argv[1]
        trans_list = ast.literal_eval(trans_list)
    except IndexError:
        trans_list = [('A','B',5000),('A','C',2000),('B','C',7000)]
    
    minimize_transactions(trans_list)


