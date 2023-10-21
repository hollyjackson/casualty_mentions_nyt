#!/usr/bin/env python
# coding: utf-8

# In[38]:


# Importing the required libraries
import os
import pandas as pd
from lxml import etree
from bs4 import BeautifulSoup
import random
import json
import time
import matplotlib as mpl
import matplotlib.pyplot as plt
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
# import multiprocessing as mp


# In[39]:


# NLTK imports
import nltk
nltk.data.path.append('../nltk_data/')
import string
from nltk import collocations 
from nltk.text import Text
from nltk.tokenize import WhitespaceTokenizer
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import word_tokenize


# ## Sampling from Dataset

# In[40]:


# Choosing a dataset
dataset_name = 'israel_palestine_war'

# Defining the dataset path
dataset_prefix = '/home/ec2-user/SageMaker/data/'

input_files = os.listdir(dataset_prefix + dataset_name + '/')


# In[41]:


# Define a function to get the text content that is needed from the XML articles available in the dataset
def getxmlcontent(root):
    if root.find('.//HiddenText') is not None:
        return(root.find('.//HiddenText').text)
    
    elif root.find('.//Text') is not None:
        return(root.find('.//Text').text)
    
    else:
        return None


# In[42]:


def create_data_lists(sample_input_files):
    # Creating lists to store article IDs, titles, dates, and text
    filename_list = []
    title_list = []
    date_list = []
    text_list = []

    # Parse files and add data to lists
    for file in sample_input_files:
        tree = etree.parse(dataset_prefix + dataset_name + '/' + file)
        root = tree.getroot()

        # The next 5 lines will gather the text of the articles (this will not be included in the final dataframe by default)
        if getxmlcontent(root) is not None:
            soup = BeautifulSoup(getxmlcontent(root))
            text = soup.get_text()
        else:
            text = 'Error in processing document'

        # Gathering the fields to include in the dataframe
        title = root.find('.//Title').text
        date = root.find('.//NumericDate').text

        filename_list.append(file)
        title_list.append(title)
        date_list.append(date)
        text_list.append(text)
    
    return filename_list, title_list, date_list, text_list


# In[43]:


def extract_data(file):
    tree = etree.parse(dataset_prefix + dataset_name + '/' + file)
    root = tree.getroot()

    # The next 5 lines will gather the text of the articles (this will not be included in the final dataframe by default)
    if getxmlcontent(root) is not None:
        soup = BeautifulSoup(getxmlcontent(root))
        text = soup.get_text()
    else:
        text = 'Error in processing document'

    # Gathering the fields to include in the dataframe
    title = root.find('.//Title').text
    date = root.find('.//NumericDate').text

    return file, title, date, text


# In[44]:


import datetime as dt

def parse_date(date_str):
    return dt.datetime.strptime(date_str, '%Y-%m-%d').date()
    


# In[45]:


sample_size = 1
prefix = "/home/ec2-user/SageMaker/preprocessed_data/"+dataset_name+"/"

index = 0
file_number = 0
while index < len(input_files):

    print('Processing', index, '/', len(input_files))
    start_index = index
    
    file_count = 0
    text = ""
    while file_count < sample_size:
        
        # Grab a file & extract info
        file, title, date, content = extract_data(input_files[index])

        # Assemble as part of large text block
        file_count += 1
        text += " F-N-S-T-A-R-T. "
        text += file
        text += " F-N-E-N-D. "
        text += " D-A-T-E-S-T-A-R-T. "
        text += date
        text += " D-A-T-E-E-N-D. "
        text += " T-I-T-L-E-S-T-A-R-T. "
        text += title
        text += " T-I-T-L-E-E-N-D. "
        text += " T-E-X-T-S-T-A-R-T. "
        text += content
        text += " T-E-X-T-E-N-D. "
        
        # Check next file
        index += 1
        if index >= len(input_files):
            break
    
    # Save current text chunk
    filename = prefix + "articles_" + str(file_number) + ".txt"
    with open(filename, 'w') as f:
        f.write(text)
    file_number += 1


# In[46]:


# Save current text chunk
filename = prefix + "articles_" + str(file_number) + ".txt"
with open(filename, 'w') as f:
    f.write(text)
file_number += 1
print(file_number)


# In[19]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




