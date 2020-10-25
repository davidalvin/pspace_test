#!/usr/bin/env python
# coding: utf-8

# In[6]:



# importing pandas as pd  
# import pandas as pd  
   


# In[ ]:


#import os
#import time
import numpy as np
import pandas as pd
import tensorflow as tf
#from matplotlib import pyplot as plt
#from GlobalConstants import *
#import pydot
#import random
#from HelperFunctions import *
print("Hello world")

# list of name, degree, score 
nme = ["aparna", "pankaj", "sudhir", "Geeku"] 
deg = ["MBA", "BCA", "M.Tech", "MBA"] 
scr = [90, 40, 80, 98] 
   
# dictionary of lists  
dict = {'name': nme, 'degree': deg, 'score': scr}  
     
df = pd.DataFrame(dict) 
print("Saving df...") 
# saving the dataframe 
df.to_csv('/artifacts/file1.csv') 
print("Saved...") 

