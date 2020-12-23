# -*- coding: utf-8 -*-
"""
@author: narendra
"""

# program to read string from file and find all email addresses


import re

# reading a text file
with open('text1.txt', 'r') as file:
    strng = file.readlines() #.replace('\n', '')
    
print('String read from the file is:')    
print(strng)


email_ids = []

for line in strng: 
    
    # find email address from every line
    lst = re.findall('\S+@\S+', line.strip()) # 
    
    if lst != []:        
        lst1 = lst[0].replace(',','')        
        # append email addresses to the list "email_ids"
        email_ids.append(lst1) 
        
        
#print(email_ids)
print('\nFollowing are email addresses present in the string:')
for ids in email_ids:
    print(ids)
    
    