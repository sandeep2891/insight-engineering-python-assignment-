#Author : Sandeep Deshpande
#Date : 3/22/15
#This program is written in python 

#GIVE THE FILE NAME
fname = raw_input("Enter file name: ")

#Opening a file to write output
file = open("wc_result.txt","w")

#Reading the file 
words = open(fname, 'r').read().lower().split()

#Removing common puntuations
words = [word.replace(".", "") for word in words]
words = [word.replace(",", "") for word in words]
words = [word.replace(";", "") for word in words]
words = [word.replace("!", "") for word in words]
words = [word.replace("?", "") for word in words]

#Calculating frequency of words
wordfreq =[words.count(p) for p in words]

#Creating a dictionary 
dictionary = dict(zip(words,wordfreq))

#Writing the contents of dictionary
for key in sorted(dictionary):
    file.write(str(key),"\t", str(dictionary[key]))

#Close the file    
file.close()
    
