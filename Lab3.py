#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 1)Create a list of lists (movies007). The list will be composed by each list of movies featured by
#each actor.


# In[18]:


moviesSeanConnery = ["Dr. No (1962)",
"From Russia with Love (1963)",
"Goldfinger (1964)",
"Thunderball (1965)",
"You Only Live Twice (1967)",
"Diamonds Are Forever (1971)",
"Never Say Never Again (1983)"]

moviesDavidNeven=["Casino Royale (1967)"]

moviesGeorgeLazenby=["On Her Majesty's Secret Service (1969)"]

moviesRogerMoore=[ "Live and Let Die (1973)",
"The Man with the Golden Gun (1974)",
"The Spy Who Loved Me (1977)",
"Moonraker (1979)",
"For Your Eyes Only (1981)",
"Octopussy (1983)",
"A View to a Kill (1985)"]

moviesTimothyDalton=[
"The Living Daylights (1987)",
"Licence to Kill (1989)"
]

moviesPierceBrosnan=[
"GoldenEye (1995)",
"Tomorrow Never Dies (1997)",
"The World Is Not Enough (1999)",
"Die Another Day (2002)"
]

moviesDanielCraig=["Casino Royale (2006)",
"Quantum of Solace (2008)",
"Skyfall (2012)",
"Spectre (2015)"]


# In[20]:


movies007 = [moviesSeanConnery, moviesDavidNeven,moviesGeorgeLazenby,moviesRogerMoore,moviesTimothyDalton,moviesPierceBrosnan,
moviesDanielCraig,]
print (movies007)


# In[21]:


#2) How many movies were played by the first actor to play James Bond?


# In[22]:


len(movies007[0])


# In[23]:


#3) How many movies were played by the last actor to play James Bond?


# In[24]:


len(movies007[-1])


# In[25]:


#4) How many actors played the role of James Bond?


# In[26]:


len(movies007)


# In[ ]:


#5) Create a new list with the number of movies played by each actor


# In[27]:


a=len(movies007[0])
b=len(movies007[1])
c=len(movies007[2])
d=len(movies007[3])
e=len(movies007[4])
f=len(movies007[5])
g=len(movies007[-1])
newlist = [a,b,c,d,e,f,g]
print(newlist)


# In[ ]:


#6) How many movies were played by the actor who appeared most often in movies?


# In[28]:


max(newlist)


# In[ ]:


#7) How many movies were played by the actor who appeared in fewer movies?


# In[29]:


min(newlist)


# In[ ]:


#8) Create a new list (movies007a) with all the films.


# In[30]:


movies007a = []
movies007a.extend(moviesSeanConnery)
movies007a.extend(moviesDavidNeven)
movies007a.extend(moviesGeorgeLazenby)
movies007a.extend(moviesRogerMoore)
movies007a.extend(moviesPierceBrosnan)
movies007a.extend(moviesDanielCraig)


# In[31]:


print (movies007a)


# In[ ]:


#9) Sort the elements of the list


# In[32]:


movies007a.sort()
print(movies007a)


# In[ ]:


#10)Reverse the order of the list. What will happen if this method is executed twice? Does this
#method sort the list if it is not sorted?


# In[33]:


movies007a.reverse()
print(movies007a)


# In[ ]:


#11) What is the index of the movie "Spectre (2015)" in the list of movies


# In[34]:


movies007a.index ("Spectre (2015)")


# In[ ]:


#12) Add the movie "007 and the bad Guy of the climate change (2020)" in the 11th position


# In[35]:


movies007a.insert(10,"007 and the bad Guy of the climate change (2020)")
print(movies007a)


# In[ ]:


#13) It was a mistake. Remove the movie "007 and the bad Guy of the climate change (2020)"


# In[36]:


movies007a.remove("007 and the bad Guy of the climate change (2020)")
print(movies007a)


# In[ ]:




