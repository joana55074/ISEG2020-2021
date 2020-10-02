#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1- Verify if a value is an integer


# In[3]:


a=2


# In[4]:


type(a)


# In[ ]:


#2-Verify if a value is even


# In[6]:


a=3


# In[7]:


a % 2 == 0


# In[ ]:


#3-Insert two numbers. Is the first is bigger than the second?


# In[8]:


num1 = input("primeiro numero")


# In[9]:


type (num1)


# In[10]:


num1=int(num1)


# In[12]:


num2 = int(input ("segundo numero"))


# In[13]:


num1>num2


# In[ ]:


#4 Verify if one value is multiple of another


# In[14]:


b=35


# In[15]:


b % 2 == 0


# In[ ]:


#5 - Calculate the interest earn by an investor that invested an amount of capital of 200 during three years with an
#interest rate of 3%.
#(I= P*R*T)


# In[8]:


I = 200 * 0.03 * 3


# In[9]:


print (I)


# In[ ]:


# 6 - Capital that an investor obtained after investing an amount of capital of 200 during three years with an interest
#rate of 3%. (Compound interest)


# In[16]:


P = (200 / (1+0.03/3)**3)


# In[17]:


print (P)


# In[ ]:


#7 - Calculate your BMI (Body Mass Index)


# In[6]:


BMI = 60/1.72**2


# In[7]:


print (BMI)


# In[ ]:


#8 - Calculate the Golden ration:
#1. Solve the problem without using libraries
#2. Use module math (import math) and function sqr (math.sqrt)


# In[19]:


gr = (1+(5**(1/2))/2)


# In[20]:


print (gr)


# In[ ]:


#9 - Calculate the NPV (Net present value) of an investment, considering an initial investment of 10000, the following

#Cashflows 2000,3000, 4000, 4000 and 5000 and a discount rate of 10%.


# In[10]:


#NPV = (((2000 + 3000 + 4000 + 5000)/(1+0.1))-10000)


# In[21]:


NPV=((2000/((1+0.1)**1))+(3000/((1+0.1)**2))+(4000/((1+0.1)**3))+(4000/((1+0.1)**4))+(5000/((1+0.1)**5)))-10000


# In[22]:


print (NPV)


# In[ ]:


# 10 - Ask the user to insert name and age. Calculate the birth year. Print a result saying the 'this person was born in.'
#1. Solve the problem without using modules and libraries


# In[4]:


Nome = str(input("Insira o seu nome: ")) 


# In[5]:


Idade = int(input ("Insira a sua idade: "))


# In[9]:


Ano = 2020


# In[10]:


AnoNascimento=Ano-Idade


# In[11]:


print("Ano de Nascimento: ", AnoNascimento)


# In[ ]:


#Solve the problem using the date library from module datetime, as fallow:


# In[12]:


from datetime import date
today = date.today()
today.year
Nome = str(input("Insira o seu nome: "))
Idade = int(input ("Insira a sua idade: "))
AnoNascimento=today.year-Idade
print("Ano de Nascimento: ", AnoNascimento)


# In[ ]:


#11 -  Ask the user to insert forenames, surnames. Create a new variable (name) with your complete name.
#Create the following variables:
#nameBig - all the characters of the name are capitalized
#nameTitle - only the first character of each name (word) is capitalized
#nameSmall - all the characters of the name are lowercase.
#nameCapitalized - only the first character of the first name is capitalized


# In[13]:


Proprio = str (input("Insira o seu noe próprio: "))
Apelidos = str (input ("Insira apelidos: "))
Nome = Proprio + " " + Apelidos
nomeBig=Nome.upper()
nomeBig


# In[15]:


nomeTitle=Nome.title()
nomeTitle


# In[16]:


nomeSmall=Nome.lower()
nomeSmall


# In[17]:


nomeCapitalized = Nome.capitalize()
nomeCapitalized


# In[ ]:


# Use the following method to show in which character appears the first "da"
#str.find(sub,start,end)
#What happens if the content of sub is not found in str?


# In[ ]:




