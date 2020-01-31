"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    print("First record of texts, {} texts {} at time {}".format(texts[0][0],texts[0][1],texts[0][2]))
with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    count = 0
    for call in calls:
        count+=1
    print("Last record of calls, {} calls {} at time {}, lasting {} seconds".format(calls[count-1][0],calls[count-1][1],calls[count-1][2],calls[count-1][3]))

"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

