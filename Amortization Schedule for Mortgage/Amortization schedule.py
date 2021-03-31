#!/usr/bin/env python
# coding: utf-8

# In[13]:


years = int(input("Term of Mortgage in years: "))
loan = float(input("Amount of Loan: "))
rate = float(input("Nominal Yearly interst rate: "))
months = int(input("Number of compounding periods: "))

payment = (rate/months)*loan*(1-(1+(rate/months))**(-1*years*months))**-1

EAIR = ((1+(rate/months))**(months))-1
EAIRP = EAIR*100
print("The Yearly Effective Annual Interst Rate is ","{0:.3f}".format(EAIRP)+"%")


print("______________________________________________________________________")
print("|{0:^5}|{1:^15}|{2:^15}|{3:^15}|{4:^15}|".format("Month","Payment","Interst","Principal","Remaining_P"))
rem_principal = loan

for i in range(1,(months*years)+1):
    interst = (rem_principal * rate)/12
    principal = payment - interst
    rem_principal -= principal
    print("|{0:^5}|{1:^15.3f}|{2:^15.3f}|{3:^15.3f}|{4:^15.3f}|".format(i,payment,interst,principal,rem_principal))





# In[ ]:





# In[ ]:




