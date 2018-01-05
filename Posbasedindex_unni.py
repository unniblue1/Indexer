import urllib
import datetime
import os
import re
import html
import sys
from urllib.request import urlopen
from bs4 import BeautifulSoup


def getDocuments():
    count = 0
    documents = []
    path = r'C:\Users\user\Desktop\Information Retrieval\Assignment 2 -Web Crawler\Webcrawlerstuff\htmlpages'
    for file in os.listdir(path):
        filepath = os.path.join (r'C:\Users\user\Desktop\Information Retrieval\Assignment 2 -Web Crawler\Webcrawlerstuff\htmlpages', file)
        open_file = open(filepath, 'r', encoding = 'utf-8-sig')
        file_data = open_file.read()
        documents.append(file_data)
        count = count + 1
    return documents


def removeCommWords(formatted_Text):
    formatted_Text = formatted_Text.replace(" to "," ")
    formatted_Text = formatted_Text.replace(" a "," ")
    formatted_Text = formatted_Text.replace(" is "," ")
    formatted_Text = formatted_Text.replace(" be "," ")
    formatted_Text = formatted_Text.replace(" or "," ")
    formatted_Text = formatted_Text.replace(" of "," ")
    formatted_Text = formatted_Text.replace(" in "," ")
    formatted_Text = formatted_Text.replace(" up "," ")
    formatted_Text = formatted_Text.replace(" so "," ")
    formatted_Text = formatted_Text.replace(" and "," ")
    formatted_Text = formatted_Text.replace(" on "," ")
    formatted_Text = formatted_Text.replace(" as "," ")
    formatted_Text = formatted_Text.replace(" by "," ")
    formatted_Text = formatted_Text.replace(" from "," ")
    formatted_Text = formatted_Text.replace(" but "," ")
    formatted_Text = formatted_Text.replace(" for "," ")
    formatted_Text = formatted_Text.replace(" be "," ")
    formatted_Text = formatted_Text.replace(" are "," ")
    formatted_Text = formatted_Text.replace(" an "," ")
    formatted_Text = formatted_Text.replace(" yet "," ")
    formatted_Text = formatted_Text.replace(" nor "," ")
    formatted_Text = formatted_Text.replace(" not "," ")
    formatted_Text = formatted_Text.replace(" the "," ")   
    return formatted_Text


def getFormattedDoc(document):
    formatted_Text = document.replace("b'","")
    formatted_Text = formatted_Text.replace(">","> ")
    formatted_Text = formatted_Text.lower()
    formatted_Text = re.sub(r'&[a-z0-9]*=[a-z0-9]*#',r' ',formatted_Text)
    formatted_Text = re.sub(r'&[a-z0-9]*=[a-z0-9]*',r' ',formatted_Text)
    formatted_Text = re.sub(r'&[a-z0-9]*',r' ',formatted_Text)
    formatted_Text = re.sub(r'\s',r' ',formatted_Text)
    formatted_Text = re.sub(r'\\x..',r' ',formatted_Text)
    formatted_Text = re.sub(r'index.php[a-z0-9]*',r' ',formatted_Text)
    
    formatted_Text = formatted_Text.replace(" - "," ")
    formatted_Text = formatted_Text.replace("\\n"," ")
    formatted_Text = formatted_Text.replace("^"," ")
    formatted_Text = formatted_Text.replace(" @ "," ")
    formatted_Text = formatted_Text.replace("="," ")
    formatted_Text = formatted_Text.replace("{","")
    formatted_Text = formatted_Text.replace("(","")
    formatted_Text = formatted_Text.replace(")","")
    formatted_Text = formatted_Text.replace("[","")
    formatted_Text = formatted_Text.replace("}","")
    formatted_Text = formatted_Text.replace("\\","")
    formatted_Text = formatted_Text.replace("]","")
    formatted_Text = formatted_Text.replace("_"," ")
    formatted_Text = formatted_Text.replace('"',' ')
    formatted_Text = formatted_Text.replace("!","")
    formatted_Text = formatted_Text.replace("/"," ")
    formatted_Text = formatted_Text.replace(";","")
    formatted_Text = formatted_Text.replace("?","")
    formatted_Text = formatted_Text.replace(",","")
    formatted_Text = formatted_Text.replace("<","")
    formatted_Text = formatted_Text.replace(">","")
    formatted_Text = formatted_Text.replace("'s","")
    formatted_Text = formatted_Text.replace(":","")
    formatted_Text = formatted_Text.replace(". "," ")
    
    formatted_Text = re.sub(r"%20",r' ',formatted_Text)
    formatted_Text = re.sub(r"'",r' ',formatted_Text)
    formatted_Text = re.sub(r"%60",r'',formatted_Text)
    formatted_Text = re.sub(r'-',r' ',formatted_Text)
    formatted_Text = re.sub(r"%30",r'0',formatted_Text)
    formatted_Text = re.sub(r'.\Z',r'',formatted_Text)
    formatted_Text = formatted_Text.replace(".\n","\n")          
    return formatted_Text


if __name__=='__main__':
    documentCount = 0
    files = getDocuments()
    dictionary = {}
    for file in files:
        documentCount+=1
        formatted_text = getFormattedDoc(file)
        formatted_text = removeCommWords(formatted_text)
        loc = 0
        word_list = formatted_text.split()
        for word in word_list:
            loc += 1
            locationPtr = "(" + str(documentCount) + "," + str(loc) + ")"
            if(word not in dictionary):
                dictionary[word] = []
            dictionary[word].append(locationPtr)
    dict_list = dictionary.keys()
    word_loc_file = open(r"C:\Users\user\Desktop\Information Retrieval\Assignment 3 - Indexer\word_pos_pbased.txt",'w', encoding = 'utf-8-sig')
    words_file = open(r"C:\Users\user\Desktop\Information Retrieval\Assignment 3 - Indexer\words_pbased.txt",'w', encoding = 'utf-8-sig')
    doc_info = "Total number of documents processed  " + str(documentCount) + "\n"
    word_loc_file.write(doc_info)
    word_info = "Number of unique words " + str(len(dictionary)) + "\n\n"
    word_loc_file.write(word_info)
    for word in dict_list:
        string = "\n" + word + " --> "
        words_file.write(word + "\n")
        for location in dictionary[word]:
            string += location + " "
        word_loc_file.write(string + "\n")
    word_loc_file.close()
