# purpose: Special free delivery to selected customer 
'''Criteria:
1. Shopping value is less then 250 no free delivery
2. Shopping value between 300 and 600 (5% discount)
3. Shopping value between 800 and 1000 (7% discount)
4. Shopping value between 1000 and 2000 (10% discount)
5. Shopping value less then 300 then delivery charge of 100
'''
# Begin
# Function for shopping value discount
def isDeliveryFree(bill_value,no_ofbills):
    total_finalbill = []
    for i in range(no_ofbills):
        if(bill_value[i]>300 and bill_value[i]<=600):
            total_finalbill.append(bill_value[i]-(5*bill_value[i])//100)
        elif(bill_value[i]>700 and bill_value[i]<=1000):
            total_finalbill.append(bill_value[i]-(7*bill_value[i])//100)
        elif(bill_value[i]>1000 and bill_value[i]<=2000):
            total_finalbill.append(bill_value[i]-(10*bill_value[i])//100)
        else:
            total_finalbill.append(bill_value[i])

    return total_finalbill                
# End isDeliveryFree function
#Taking input from user
Demobill = int(input("Enter no of bills: "))
Demobill_Totalvalues = list(map(int,input("Enter different total billed amount:").split()))
#Function call
total_finalbill = isDeliveryFree(Demobill_Totalvalues,Demobill)
#Printing O/p
i=1
for each in total_finalbill:
    if(each<=300):
        each += 100
        print(f"Total Bill value of bill-no {i}:{each}(Extra 100 for Delivery)")
    else:
        print(f"Total Bill value of bill-no {i}:{each}(Free Delivery)")    
    i+=1        
#End
        
