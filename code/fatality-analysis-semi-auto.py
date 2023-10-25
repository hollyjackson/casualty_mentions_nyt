#!/usr/bin/env python
# coding: utf-8

# In[1]:


# List identifiers for Palestinian/Israeli subjects so NLP can prompt with a guess

PALESTINE_IDENTIFIERS = ["Palestine", "Palestinian", "Palestinians"]
ISRAEL_IDENTIFIERS = ["Israel","Israeli","Israelis"]

# Cities in the West Bank and Gaza
PALESTINIAN_CITIES = ["Gaza", "Gaza Strip", "Jerusalem", "Abasan al-Kabira", "Abu Dis", "Bani Na\'im", "Bani Suheila", 
                      "Beit Hanoun", "Beit Jala", "Beit Lahia", "Beit Sahour", "Beit Ummar", "Beitunia", "Bethlehem",
                      "Beit Lahm", "al-Bireh", "Deir al-Balah", "ad-Dhahiriya", "Dura", "Gaza City", "Ghazzah", "Halhul",
                      "Hebron", "al-Khalil", "Idhna", "Jabalia", "Jenin", "Jericho", "Ariha", "Khan Yunis", "Nablus", 
                      "Qabatiya", "Qalqilya", "Rafah", "Ramallah", "Sa\'ir", "as-Samu", "Surif", "Tubas", "Tulkarm",
                      "Ya\'bad", "al-Yamun", "Yatta", "az-Zawayda", "Nazareth", "Jaljulia", "Kafr Bara", "Kafr Qasim",
                      "Qalansawe", "Tayibe", "Tira", "Zemer", "Ar\'ara", "Baqa al-Gharbiyye", "al-Arian", "Basma", "Jatt",
                      "Kafr Qara", "Ma\'ale Iron", "Meiser", "Umm al-Fahm", "Umm al-Qutuf", "Lod", "Ramla", "Wadi Nisnas",
                      "Halisa", "Kababir", "Abbas", "Daliyat al-Karmel", "Ein Hawd", "Fureidis", "Ibtin", "Isfiya", 
                      "Jisr az-Zarqa", "Khawaled", "Abu Ghosh", "Beit Jimal", "Ein Naqquba", "Ein Rafa", "Beit Hanina",
                      "Beit Safafa", "Jabel Mukaber", "Old City", "Ras al-Amud", "Sheikh Jarrah", "Shuafat", "Silwan", 
                      "Sur Baher", "At-Tur", "Umm Tuba", "Wadi al-Joz", "al-Walaja", "Abu Qrenat", "Abu Talul", 
                      "Ar\'arat an-Naqab", "Ateer", "al-Atrash", "Bir Hadaj", "Dhahiyah", "Drijat", "Ghazzah", "Hura", 
                      "Kukhleh", "Kuseife", "Lakiya", "Makhul", "Mitnan", "Mulada", "Qasr al-Sir", "Rahat", "al-Sayyid", 
                      "Shaqib al-Salam", "Tirabin al-Sana", "Tel as-Sabi", "Umm Batin", "Abu Sinan", "Arab al-Aramshe", 
                      "Arab al-Subeih", "Arab al-Na\'im", "Arraba", "Basmat Tab\'un", "Beit Jann", "Bi\'ina", 
                      "Bir al-Maksur", "Bu\'eine Nujeidat", "Buqei\'a", "Daburiyya", "Ed Dahi", "Deir al-Asad", 
                      "Deir Hanna", "Dmeide", "Eilabun", "Ein al-Asad", "Ein Mahil", "Fassuta", "Hamaam", "Hamdon", 
                      "Hurfeish", "Hussniyya", "I\'billin", "Iksal", "Ilut", "Jadeidi-Makr", "Jish", "Julis",
                      "Ka\'abiyye-Tabbash-Hajajre", "Kabul", "Kafr Kanna", "Kafr Manda", "Kafr Misr", "Kafr Yasif", 
                      "Kamanneh", "Kaukab Abu al-Hija", "Kfar Kama", "Kisra-Sumei", "Maghar", "Majd al-Krum", 
                      "Manshiya Zabda", "Mashhad", "Mazra\'a", "Mi\'ilya", "Muqeible", "Nahf", "Na\'ura", "Nazareth", 
                      "Nein", "Rameh", "Ras al-Ein", "Rehaniya", "Reineh", "Rumana", "Rumat al-Heib", "Sajur", "Sakhnin",
                      "Sallama", "Sandala", "Sha\'ab", "Shefa-\'Amr", "Sheikh Danun", "Shibli–Umm al-Ghanam", "Sulam",
                      "Suweid Hamira", "Tarshiha", "Tamra City", "Tamra Village", "Tuba-Zangariyye", "Tur\'an", "Uzeir", 
                      "Yafa an-Naseriyye", "Yanuh-Jat", "Yarka", "Zarzir", "Bani Suheila", "Beit Hanoun", "Beit Lahiya",
                      "Deir al-Balah", "Jabalia", "Khan Yunis", "Rafah"]

# Cities in Israel ('48 lands)
ISRAELI_CITIES = ["Acre","Afula","Arad","Arraba","Ashdod","Ashkelon","Baqa al-Gharbiyye","Bat Yam","Beersheba",
                  "Beit She\'an","Beit Shemesh","Bnei Brak","Dimona","Eilat","El\'ad","Giv\'at Shmuel","Givatayim",
                  "Hadera","Haifa","Herzliya","Hod HaSharon","Holon","Jerusalem","Kafr Qasim","Karmiel","Kfar Saba",
                  "Kfar Yona","Kiryat Ata","Kiryat Bialik","Kiryat Gat","Kiryat Malakhi","Kiryat Motzkin","Kiryat Ono",
                  "Kiryat Shmona","Kiryat Yam","Lod","Ma\'alot-Tarshiha","Migdal HaEmek","Modi\'in-Maccabim-Re\'ut",
                  "Nahariya","Nazareth","Nesher","Ness Ziona","Netanya","Netivot","Nof HaGalil","Ofakim","Or Akiva",
                  "Or Yehuda","Petah Tikva","Qalansawe","Ra\'anana","Rahat","Ramat Gan","Ramat HaSharon","Ramla",
                  "Rehovot","Rishon LeZion","Rosh HaAyin","Safed","Sakhnin","Sderot","Shefa-\'Amr","Tamra","Tayibe",
                  "Tel Aviv-Yafo","Tel Aviv","Tiberias","Tira","Tirat Carmel","Umm al-Fahm","Yavne","Yehud-Monosson",
                  "Yokneam Illit"]

PALESTINE_MEMBER_AFFILIATIONS = PALESTINE_IDENTIFIERS + PALESTINIAN_CITIES
ISRAEL_MEMBER_AFFILIATIONS = ISRAEL_IDENTIFIERS + ISRAELI_CITIES


# In[3]:


# Importing the required libraries

import sys
sys.version
from IPython.display import clear_output


import os
import pandas as pd
from lxml import etree
from bs4 import BeautifulSoup
import random
import matplotlib as mpl
import matplotlib.pyplot as plt
import json
import locale
locale.setlocale( locale.LC_ALL, 'en_US.UTF-8' ) 
import datetime as dt

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
from nltk.corpus import sentiwordnet as swn
from nltk import RegexpParser
from nltk.tree import *

# spaCy imports 
import spacy 
from spacy.symbols import nsubj, VERB

from time import sleep


# In[6]:


# NLP package add-ons
nlp = spacy.load('../spacy_data/en_core_web_sm/en_core_web_sm-3.0.0')

# enumerate spacy subject types
SUBJECTS = ["nsubj", "nsubjpass", "csubj", "csubjpass", "agent", "expl"]

# 27. VB  Verb, base form
# 28. VBD Verb, past tense
# 29. VBG Verb, gerund or present participle
# 30. VBN Verb, past participle
# 31. VBP Verb, non-3rd person singular present
# 32. VBZ Verb, 3rd person singular present
VERBS = ["VB", "VBD", "VBG", "VBN", "VBP", "VBZ"]

# Enumerate common words related to death for automated sentence tagging
FATAL_VERBS_PASSIVE = ["die", "decease"]
FATAL_VERBS_ACTIVE = ["kill", "murder", "shoot", "assassinate", "stab"]
FATAL_VERBS_ACTIVE_SPECIFIC = ["behead", "slaughter", "execute", "hang"]
ALL_FATAL_VERBS = FATAL_VERBS_PASSIVE + FATAL_VERBS_ACTIVE + FATAL_VERBS_ACTIVE_SPECIFIC

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()


# In[7]:


# Choosing a dataset
dataset_name = 'israel_palestine_war'
sample_size = 1

# Defining the dataset path
dataset_prefix = '/home/ec2-user/SageMaker/data/'
results_prefix = "/home/ec2-user/SageMaker/results/"+dataset_name+"/"
counts_prefix = "/home/ec2-user/SageMaker/results/"+dataset_name+"/fatality_counts/"
original_texts_prefix = "/home/ec2-user/SageMaker/preprocessed_data/"+dataset_name+"/"

input_files = os.listdir(dataset_prefix + dataset_name + '/')


# In[8]:


# Define a function to get the text content that is needed from the XML articles available in the dataset
def getxmlcontent(root):
    if root.find('.//HiddenText') is not None:
        return(root.find('.//HiddenText').text)
    
    elif root.find('.//Text') is not None:
        return(root.find('.//Text').text)
    
    else:
        return None
    
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


# In[9]:


# Reformat date
def parse_date(date_str):
    return dt.datetime.strptime(date_str, '%Y-%m-%d').date()

# Extract article date from file
def extract_date(index, offset):
    file_index = index + offset
    file = input_files[file_index]
    
    tree = etree.parse(dataset_prefix + dataset_name + '/' + file)
    root = tree.getroot()

    date = root.find('.//NumericDate').text
    return date#parse_date(date)    
    


# In[10]:


# for clearing UI
def refresh_screen():
    clear_output()
    sleep(0.02)


# # Content analysis

# In[11]:


def follow_compound(dep_idx, dependencies_by_governor):
    # Follow compound chain and return descriptors of a dependency
    visited = set([dep_idx])    
    current_idx = dep_idx    
    descriptors = set()
    
    found = True
    while found:
        found = False
        for dep in dependencies_by_governor[current_idx]:
            if dep["dep"] == "compound:prt" or dep["dep"] == "compound":
                current_idx = dep["dependent"]
                descriptors.add(dep["dependentGloss"])
                if current_idx not in visited:
                    found = True
                    visited.add(current_idx)
                break                
    return descriptors


# In[13]:


def investigate_subject(subject, dependencies_by_governor):
    # Investigate all dependencies related to a subject to find as many descriptors as possible
    # Present in a tiered list based on "closeness" to subject
    
    verbose = False
    
    subject_descriptors = [set(), set(), set(), 1]
    subject_descriptors[0].add(subject[1])
    # AMOD takes precedence over NMOD? takes precedence over ACL
    for dep in dependencies_by_governor[subj_idx]:
        if (dep["dep"] == "amod"):
            subject_descriptors[0].add(dep["dependentGloss"])
            if verbose:
                print(dep["dep"], dep["dependentGloss"], "\n")

        if (dep["dep"] == "acl" or dep["dep"] == "acl:relcl"):
            subject_descriptors[1].add(dep["dependentGloss"])
            # INVESTIGATE THE SUBJECT AND OBJECT OF DESCRIPTIVE CLAUSE
            if verbose:
                print(dep["dep"], dep["dependentGloss"])
                print(dependencies_by_governor[dep["dependent"]])
                print()
            for double_dep in dependencies_by_governor[dep["dependent"]]:
                # check nsubj and check obj
                 if (double_dep["dep"] == "nsubj" or double_dep["dep"] == "nsubj:pass" or double_dep["dep"] == "nsubj:outer"
                     or double_dep["dep"] == "csubj" or double_dep["dep"] == "csubj:pass" or double_dep["dep"] == "csubj:outer"
                     or double_dep["dep"] == "obj"):
                    subject_descriptors[2].add(double_dep["dependentGloss"])

        if (dep["dep"] == "nmod" or dep["dep"] == "nmod:npmod" or dep["dep"] == "nmod:tmod" or dep["dep"] == "nmod:poss"):
            subject_descriptors[1].add(dep["dependentGloss"])
            if verbose:
                print(dep["dep"], dep["dependentGloss"], "\n")

        if (dep["dep"] == "advmod"):
            subject_descriptors[1].add(dep["dependentGloss"])#TODO: CHECK THIS
            if verbose:
                print(dep["dep"], dep["dependentGloss"], "\n")

        if (dep["dep"] == "appos"):
            subject_descriptors[0].add(dep["dependentGloss"])#TODO:CHECK THIS
            # Look for adjectives for appos also 
            # CHECK COMPOUD AND AMOD 
            to_add = follow_compound(dep["dependent"], dependencies_by_governor)
            if verbose:
                print(dep["dep"], dep["dependentGloss"], "\n", to_add)
            for thing in to_add:
                subject_descriptors[0].add(thing)
            for double_dep in dependencies_by_governor[dep["dependent"]]:
                 if (double_dep["dep"] == "amod"):
                    subject_descriptors[2].add(double_dep["dependentGloss"])
                    
#         if (dep["dep"] == "ccomp"):
#             print(dependencies_by_governor[dep["dependent"]])
#             for double_dep in dependencies_by_governor[dep["dependent"]]:
#                 if (double_dep["dep"] == "nsubj" or double_dep["dep"] == "nsubj:pass" 
#                      or double_dep["dep"] == "csubj" or double_dep["dep"] == "csubj:pass"):
#                     subject_descriptors[2].add(double_dep["dependentGloss"])

        if (dep["dep"] == "nummod"):
            try:
                subject_descriptors[3] = locale.atoi(dep["dependentGloss"])
            except:
                subject_descriptors[3] = dep["dependentGloss"]
                

                
                
    return subject_descriptors


# In[14]:


def extract_sentences(sentences):
    # extract all sentences in an article
    sentences_text = [None]*len(sentences)
    for sentence in sentences:
        sentence_index = sentence["index"]
            
        tokens = sentence["tokens"]
        sentence_text = ""
        for token in tokens:
            sentence_text += token["before"] + token["word"] + token["after"]
            
        sentences_text[sentence_index] = sentence_text
    return sentences_text
           


# # UI for Sentence Tagging

# In[22]:



results_files = os.listdir(results_prefix + '/')

assigned_sentences = {} # init to handle duplicates

for index in range(0, len(input_files), sample_size):    

    indices = []
    titles = []
    dates = []
    voices = []
    categories = []
    recorded_sentences = []

    print(index, '/', len(input_files))
    
    # Open NLP-analyzed result
    filename = results_prefix + "articles_" + str(index) + ".txt.json"
    try:
        with open(filename) as d:
            data = json.load(d)
    except FileNotFoundError:
        print('FILE NOT FOUND')
        continue
        
    # Open original text block from preprocessed data file
    original_filename = original_texts_prefix + "articles_" + str(index) + ".txt"
    f = open(original_filename, "r")
    article_text = f.read()
    f.close() 

    # Extract original date
    _, title, date, _ = extract_data(input_files[index])
    
    # Extract NLP results
    sentences = data["sentences"]    
    text_all_sentences = extract_sentences(sentences)
    
    # Iterate through POS labels for each token
    file_count = -1
    fn_started = False
    for sentence in sentences:
        sentence_index = sentence["index"]
            
        tokens = sentence["tokens"]
        dependencies = sentence["basicDependencies"]
        sentence_text = ""
        for token in tokens:
            sentence_text += token["before"] + token["word"] + token["after"]
        
        # only relevant if sample_size > 1
        # if "T-I-T-L-E-S-T-A-R-T" in sentence_text:
        #     file_count += 1

        # create a data structure that maps governor dep_idx to dependencies
        dependencies_by_governor = [ [] for i in range(len(tokens)+1) ]
        for dep in dependencies:
            gov_idx = dep["governor"]
            dependencies_by_governor[gov_idx].append(dep)

        # create data structure for tokens
        tokens_by_idx = {}
        for token in tokens:
            tokens_by_idx[token["index"]] = token
            
        prepositional_information = None        
        for token in tokens:
            pos = token["pos"]

            if pos not in VERBS:
                continue
            
            word = token["word"]
            lemma = token["lemma"]
            dep_idx = token["index"]
            
            # ONLY present to user sentences related to death 
            if lemma not in ALL_FATAL_VERBS:
                continue

            verb_active = False if lemma in FATAL_VERBS_PASSIVE else True

            # Find subject
            voice = None
            for dep in dependencies_by_governor[dep_idx]:
                # If the sentence is in active voice, a 'nsubj' dependecy should exist.
                # If the sentence is in passive voice a 'nsubjpass' dependency should exist
                if dep["dep"] == "nsubj" or dep["dep"] == "csubj":
                    voice = "ACTIVE"
                    break
                elif dep["dep"] == "nsubj:pass" or dep["dep"] == "csubj:pass" or dep["dep"] == "aux:pass":
                    voice = "PASSIVE"
                    break

            # for ACTIVE verbs, we are looking for dobj is used actively or nsubjpass if used passively 
            # for PASSIVE verbs, we are looking for nsubj if used actively or nsubjpass if used passively 
            subject = None
            perp_keyword = None
            for dep in dependencies_by_governor[dep_idx]:
                if voice == "ACTIVE" and not verb_active and dep["dep"] == "nsubj":
                    # Example --> She died
                    subject = (dep["dependent"], dep["dependentGloss"])
                    break
                if voice == "PASSIVE" and dep["dep"] == "nsubj:pass":
                    # Example --> She is deceased, She was killed
                    subject = (dep["dependent"], dep["dependentGloss"])
#                         perp_keyword = "iobj" NEED TO CHECK THIS
                    break
                if verb_active and dep["dep"] == "obj":
                    voice = "ACTIVE"
                    # Example --> He killed her
                    subject = (dep["dependent"], dep["dependentGloss"])
#                         perp_keyword = "nsubj"
                    break
    
            # If subject found, find GUESS for subject's affiliation
            IS_MEMBER_PALESTINE = False
            IS_MEMBER_ISRAEL = False
            if subject is not None:
                subj_idx = subject[0]
                subj_token = tokens_by_idx[subj_idx]
                print("SUBJECT", subject[1], subj_token["ner"])
                subject_descriptors = investigate_subject(subject, dependencies_by_governor)
                # Check prepositional phrases for this sentence
                if prepositional_information is None:
                    prepositional_information = set()
                    for dep in dependencies:
                        if (dep["dep"] == "case"):
                            if (tokens_by_idx[dep["dependent"]]["lemma"] == "at"
                                or tokens_by_idx[dep["dependent"]]["lemma"] == "in"):
                                prepositional_information.add(dep["governorGloss"])
                for pi in prepositional_information:
                    subject_descriptors[2].add(pi)

                # Finally, check prepositional phrases in the sentence
                # token --> case --> to preposition (in or at)
                ### ---------------TODO: MUST CHANGE HERE WHEN DATASET UPDATES
                for j in range(3):
                    for sd in subject_descriptors[j]:
                        if sd in PALESTINE_MEMBER_AFFILIATIONS:
                            IS_MEMBER_PALESTINE = True
                        if sd in ISRAEL_MEMBER_AFFILIATIONS:
                            IS_MEMBER_ISRAEL = True

            # MANUALLY VALIDATE CATEGORY
            if sentence_text not in assigned_sentences:
                print(index, '/', len(input_files))
                print('Please assign a category to the VICTIM:')
                if (IS_MEMBER_PALESTINE or IS_MEMBER_ISRAEL) and not (IS_MEMBER_PALESTINE and IS_MEMBER_ISRAEL):
                    category_guess = 'palestine' if IS_MEMBER_PALESTINE else 'israel'
                    print('My guess is the VICTIM is from',category_guess)
                assigned = False
                sentence_chunk = " ".join(text_all_sentences[max(0,sentence_index-3):min(len(sentences)-1,sentence_index+4)])
                for string in [sentence_text, sentence_chunk, article_text]:
                    print(string)
                    while True:
                        category = input("Enter category ('palestine', 'israel', 'both', none', or 'next' for the next string): ").strip().lower()
                        print()
                        print('You chose',category)
                        if category == 'palestine' or category == 'israel' or category == 'both':
                            categories.append(category)
                            assigned = True
                            break
                        elif category == 'none':
                            assigned = True
                            break
                        elif category == 'next':
                            break
                        else:
                            print("Invalid category. Please enter 'palestine', 'israel', 'both', 'none', or 'next'.")
                    if assigned:
                        print('Categorized as',category)
                        break

                refresh_screen()
                print()
            else:
                print('ASSIGNED TO EXISTING CATEGORY')
                assigned = True
                category = assigned_sentences[sentence_text]
                categories.append(category)
            
            if assigned and category != 'none':
                # date_str = extract_date(index, file_count)
                # date = parse_date(date_str)
                dates.append(date)
                voices.append(voice)
                recorded_sentences.append(sentence_text)

                # metadata
                titles.append(title)
                indices.append(index)
                
                # add to dictionary to handle duplicates
                assigned_sentences[sentence_text] = category

                
    
    # After all sentences are complete, save info for a file
    file_dict = {
        'article_index': indices,
        'article_title': titles,
        'article_date': dates,
        'sentence': recorded_sentences,
        'category': categories,
        'voice': voices
    }
    df = pd.DataFrame(file_dict)
    df.to_csv(counts_prefix + 'articles_'+str(index)+'.csv',index=False)
    print('Saved CSV file, moving on to next article...',index+1)
    print('.......')
    refresh_screen()
    print()
    


# In[ ]:




