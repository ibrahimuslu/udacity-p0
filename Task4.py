"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
count =0
textPhoneDict = {}
callingPhoneDict = {}
receiveingPhoneDict = {}
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    
    for text in texts:
        if text[0] not in textPhoneDict :
            textPhoneDict[text[0]]=1
        else:
            textPhoneDict[text[0]]+=1
        if text[1] not in textPhoneDict:
            textPhoneDict[text[1]]=1
        else:
            textPhoneDict[text[1]]+=1
with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    for call in calls:
        if call[0] not in callingPhoneDict:
            callingPhoneDict[call[0]]=1
        else:
            callingPhoneDict[call[0]]+=1
        if call[1] not in receiveingPhoneDict:
            receiveingPhoneDict[call[1]]=1
        else:
            receiveingPhoneDict[call[1]]+=1

print("These numbers could be telemarketers: ")
for phone in sorted(callingPhoneDict):
    if phone not in receiveingPhoneDict and  phone not in textPhoneDict:
        print(phone)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

