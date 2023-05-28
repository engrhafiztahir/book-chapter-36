#!/usr/bin/env python
# coding: utf-8

# In[11]:


customers = [
{ " customer id": 0,
"first name":"John",
"last name": "Ogden",
"address": "301 Arbor Rd.",
},
{ " customer id": 1,
"first name":"Ann",
"last name": "Sattermyer",
 "address": "PO Box 1145",
},
{ " customer id": 2,
"first name":"Jill",
"last name": "Somers",
"address": "3 Main St.",
},
]


customer_info = customers[0]
print(customer_info)
print(customer_info["address"])

new_dictionary = {
    "customer id": 3,
    "first name":"George",
    "last name":"Peter",
    "address":"Main street Washington D.C"
}

customers.append(new_dictionary)
print(customers)
a = len(customers)
a = int(a)
print(a)
new_dictionary1 ={
    "customer id":a,
    "first name":"David"
}


customers.append(new_dictionary1)
print(customers)


# In[ ]:




