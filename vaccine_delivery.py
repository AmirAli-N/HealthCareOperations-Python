#!/usr/bin/env python
# coding: utf-8

# In[60]:


import numpy


# In[61]:


child_req=numpy.loadtxt(fname='C:\\Users\\Amir Ali\\Google Drive\\Teaching-Health care operations management\\05-Immunization, Infection control, and Vaccination\\AMPL-Python\\vaccine_delivery-child_requirements.txt', dtype=int, delimiter=' ')


# In[62]:


injection_req=numpy.loadtxt(fname='C:\\Users\\Amir Ali\\Google Drive\\Teaching-Health care operations management\\05-Immunization, Infection control, and Vaccination\\AMPL-Python\\vaccine_delivery-child_requirements.txt', dtype=int)


# In[63]:


vaccine_set=range(0, 14)


# In[64]:


antigen_set=range(0, len(child_req))


# In[65]:


not_blending=[2-1, 5-1, 6-1]


# In[66]:


from gurobipy import *


# In[67]:


vac_del=Model("vaccine delivery model")


# In[68]:


v=vac_del.addVars(vaccine_set, vtype=GRB.BINARY)


# In[69]:


x=vac_del.addVars(antigen_set, vaccine_set, vtype=GRB.INTEGER)


# In[70]:


y=vac_del.addVars(antigen_set, vaccine_set, vtype=GRB.BINARY)


# In[71]:


vac_del.setObjective(sum(200*v[i] for i in vaccine_set), GRB.MINIMIZE)


# In[72]:


for i in vaccine_set:
    vac_del.addConstr(sum(x[j,i] for j in antigen_set)<=3*v[i], "max_antigen[%d] %i")


# In[73]:


for j in antigen_set:
    vac_del.addConstr(sum(x[j,i] for i in vaccine_set)==child_req[j], "child_requirement[%d] %j")


# In[74]:


for j in antigen_set:
    for i in vaccine_set:
        vac_del.addConstr(x[j,i]<=injection_req[j], "dose_requirement[%d][%d] %j %i");


# In[75]:


for j in not_blending:
    for i in vaccine_set:
        vac_del.addConstr(x[j, i]<=3*y[j,i], "not_blending1[%d][%d] %j %i")


# In[76]:


for i in vaccine_set:
    vac_del.addConstr(sum(y[j,i] for j in not_blending)<=1, "not_blending2[%d] %i")


# In[77]:


vac_del.optimize()


# In[78]:


print(vac_del.objVal)


# In[79]:


x_disp=vac_del.getAttr('x',x)


# In[80]:


v_disp=vac_del.getAttr('x',v)


# In[81]:


v_disp


# In[82]:


x_disp


# In[ ]:




