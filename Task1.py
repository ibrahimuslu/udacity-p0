"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
count =0
phoneDict = {}
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    
    for text in texts:
        if text[0] not in phoneDict:
            phoneDict[text[0]]=1
        else:
            phoneDict[text[0]]+=1
        if text[1] not in phoneDict:
            phoneDict[text[1]]=1
        else:
            phoneDict[text[1]]+=1
with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    for call in calls:
        if call[0] not in phoneDict:
            phoneDict[call[0]]=1
        else:
            phoneDict[call[0]]+=1
        if call[1] not in phoneDict:
            phoneDict[call[1]]=1
        else:
            phoneDict[call[1]]+=1
for phone in phoneDict:
    count+=1
print("There are {} different telephone numbers in the records.".format(count))

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
