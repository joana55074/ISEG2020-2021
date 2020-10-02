#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Construct a list (shoppingList) including 'potatoes', 'carrots', 'cod' and 'sprouts’


# In[4]:


shoppingList = [ 'patatoes', 'carrots', 'cod', 'sprouts']


# In[5]:


print (shoppingList)


# In[ ]:


#Get the second and the last element of the list


# In[6]:


shoppingList [1]


# In[7]:


shoppingList[-1]


# In[ ]:


#Iterate though the list


# In[8]:


print (shoppingList)


# In[ ]:


#Create a new list (studentList)


# In[10]:


studentList = []


# In[ ]:


#Add the follwoing elements to the shoppingList: orange and lime


# In[12]:


studentList. append ('Laranja')


# In[13]:


studentList. append ('Limao')


# In[14]:


print (studentList)


# In[ ]:


#Remove the carrots, the first element and last element of the shoppingList list


# In[15]:


del shoppingList [0]


# In[16]:


del shoppingList [1]


# In[17]:


shoppingList.pop()


# In[18]:


print (shoppingList)


# In[ ]:


#Delete the shoppingList list


# In[19]:


del shoppingList


# In[ ]:


#Create a list with the double values of all integer number between 1 and 15.


# In[1]:


squares = [x**2 for x in range (1,15)]


# In[2]:


print (squares)


# In[ ]:


#Obtain the first 3 elements of the list


# In[3]:


firstThree = squares [: 3]


# In[4]:


print (squares)


# In[41]:


#pergunta 12


# In[42]:


shoppingList = [ 'patatoes', 'carrots', 'cod', 'sprouts']


# In[43]:


shopping = shoppingList


# In[44]:


shoppingList.append("orange")


# In[45]:


print(shopping)


# In[ ]:


#Neste exercicio já tinhamos a lista shoppingList, criamos outra lista com todos os elementos que a lista shoppingList já continha. De seguida adicionámos um produto, a laranja, À lista e por fim mandámos imprimir a lista final que incluia já as laranjas.


# In[ ]:


#Remove all the items from the shoppingList


# In[46]:


shoppingList.clear()


# In[47]:


print (shoppingList)


# In[ ]:


#Exercicio 14


# In[48]:


newPurchases= ("bananas", "beans", "rice")


# In[49]:


print (newPurchases [1])


# In[50]:


newPurchases [0] = "apple"


# In[ ]:


#Trata-se de um Tuple. Neste exercicio é criada uma lista com 3 elementos, de seguida é pedido o 2º elemento a qual é apresentada a resposta beans. 
#Por último é feita uma tentativa de troca do priemiro elemento. ISto não é possível devido ao facto de um tuple ser imutável, ou seja não pode ser alterado. 


# In[ ]:


# Create a dictionary including the follwoing elements: orange, apple, pear, grape and peach. Key are 1 to 5. Iterate through
#key-value pair.


# In[51]:


fruta = {1: 'laranja', 2: 'maçã', 3:'pêra', 4: 'uva', 5: 'pêssego'}


# In[52]:


print (fruta)


# In[ ]:


#Create a weekList that is composed of several lists, each one corresponding to a day


# In[53]:


semana = []


# In[ ]:




