#!/usr/bin/env python
# coding: utf-8

# stack operations:
# 1.push()
# 2.pop()
# 3.size()
# 4.top()

# In[11]:


graph={
    'Start':['A','B'],
    'A':['Start','E','F'],
    'B':['Start','D','C'],
    'C':['B'],
    'D':['B','Goal'],
    'E':['B','G'],
    'F':['B'],
    'G':['E'],
    'Goal':['E','F']
}


# In[14]:


def dfs(graph,Start,Goal,visited):
    stack=[Start]
    while stack:
        node=stack.pop()
        if node not in visited:
            visited.append(node)
            if node==Goal:
                print(visited)
            for neighbours in graph[node]:
               dfs(graph,neighbours,Goal,visited) 


# In[15]:


dfs(graph,"Start","Goal",[])


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




