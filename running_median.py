#Author : Sandeep Deshpande
#Date : 3/22/15
#This program is written in python 

#GIVE THE FILE NAME
fname = raw_input("Enter file name: ")

#Opening a file to write output
f = open("med_result.txt", "w")

#Reading the file
words = open(fname, 'r').read()

#Creating Variables
space_count = 0
line_count = 0
word_count = 0
mid = 0

#Space count and word count 
for charecter in words:
    if charecter == "\n":
        line_count = line_count + 1
        word_count = space_count + 1
        mid = word_count/float(line_count)
        x = mid - int(mid)
        if x == 0.5:
            median = mid
        elif x < 0.5:
            median = int(mid)
        else:
            median = int(mid) + 1
            
#Writing the contents to the file           

        f.write(str(median) + "\n")
    if charecter == " ":
        space_count = space_count + 1
        
#Close the file    
f.close()
