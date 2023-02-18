#!/usr/bin/env python
# coding: utf-8

# In[1]:


a=[100,5,60,54 ]


# In[2]:


print (sorted(a))


# In[3]:


a ="omprakash vengatasami"


# In[4]:


print (sorted(a))


# In[5]:


a=[100,5,60,54]
a.append(2000)
print(a)


# In[6]:


a=[1,2,3,4]
b=[5,6,7]
a.append(b)
print(a)


# In[7]:


a=[1,2,3,4]
b=[5,6,7]
print(a+b)
print(a)


# In[8]:


a=[1,2,3,4]
b=[5,6,7]
a.extend(b)


# In[9]:


print(a
     )


# In[10]:


a=[1,2,3,4]
b=[5,6,7]
a.extend(b)
print a


# In[11]:


print (a)


# In[12]:


a=[1,2,2]
b=a
a.append(4)
print(a)
print(b)


# In[13]:


a=[1,2,2]
b= a.copy()
a.append(4)
print(a)
print(b)


# In[14]:


a=[1,2,3,4,5]
a.reverse()
print(a)


# In[15]:


a[0:3]


# In[16]:


a.index(3)


# In[17]:


a =[["kiran","25","chennai"], ["kumar","28", "madurai"]]

print(a[0:3])


# In[18]:


print(a[0])


# In[19]:


print(a[0] [1])


# In[20]:


print(a[0] [2])


# In[21]:


a=(1,2,3)
print (min(a))


# In[22]:


print(a[0])


# In[23]:


print(len(a))


# In[24]:


b=a
print(b)


# In[25]:


b=a.copy()


# In[26]:


print(b)


# In[27]:


a =[["kiran","25","chennai"], ["kumar","28", "madurai"]]
print(a[1][2])


# In[28]:


a ={1,2,3}
print(a)


# In[29]:


a=["test", "test", "try", "hello", "hello"]
print (a)


# In[30]:


print (set(a))


# In[31]:


print(list(set(a
              )))


# In[32]:


print(tuple(set(a)))


# In[33]:


a=("test", "test", "try", "hello", "hello")
print(tuple(set(a)))


# In[34]:


print(list(set(a
              )))


# In[35]:


print(a[0] [2])


# In[38]:


print(sorted(tuple(set(a)) )


# In[37]:


print(sorted tuple(set(a)))


# In[39]:


print(sorted(tuple(set(a)) )
      


# In[40]:


print(sorted(tuple(set(a)) ))


# In[41]:


a={1,2,3}
a.add(5)
print(a)


# In[42]:


a.remove(3)
print(a)


# In[43]:


b=a.pop()
print(b)
print(a)


# In[44]:


a={1,2,3,4,5}
b={4,5,6,7,8}
print(a.union(b))


# In[45]:


print(a|b)


# In[46]:


print(a.intersection(b))


# In[47]:


print(a &b)


# In[48]:


print (a.difference (b)
      )


# In[49]:


print(a-b)
print(b.difference(b))


# In[50]:


print(b.differnce (a))


# In[51]:


print(a-b)


# In[52]:


print(b.difference(b))


# In[53]:


a={1,2,3,4,5}
b={4,5,6,7,8}
print(b.differnce (a))


# In[54]:


a={1,2,3,4,5}
b={3,4}

print (a.issuperset(b
                   ))


# In[55]:


print (b.issuperset(a))


# In[56]:


print(a.issubset(b))


# In[ ]:




