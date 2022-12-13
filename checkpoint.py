#!/usr/bin/env python
# coding: utf-8

# In[ ]:


firstname = str(input("Firstname="))


# In[1]:


def reversename():
    firstname = str(input("Firstname="))
    lastname = str(input("Lastname="))
    print(lastname+" "+firstname)


# In[3]:


reversename()


# In[15]:


def n():
    n = int(input("enter n"))
    return n+(n*n)+(n*n*n)


# In[10]:


def number():
    number=int(input("enter a number"))
    if(number%2 == 0):
        print("number is even")
    else:
        print("number is odd")


# In[12]:


number()


# In[39]:


numbers = range(2000,3201)
for x in numbers: 
    if(x%7 == 0 and x%5 != 0):
        print(x)


# In[8]:


def fact(i):
    if(i==0 or i==1):
        return 1
    else:
        i*fact(i-1)


# In[9]:


range()


# In[ ]:


n = int(input("donner n"))
resultat = 1
for i in range(1,n+1,1):
    resultat = resultat*i
print(resultat)


# In[14]:


mystring = str(input("enter a string"))
result=""
for i in range(len(mystring)):
    if(i%2==0):
        result=result+mystring[i]
print(result)


# In[18]:



x = int(input("enter a price"))
y=()
    if x>=500 :
    y = x*0.5
    print(y)
    elif x in range(201,500)
    y = x*0.7
    print(y)
    elif x<200
    y=x*0.9
    print(y)
    else 
    print("invalid price") 
 


# In[ ]:




