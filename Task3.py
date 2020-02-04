"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    areaCodes = {}
    count = 0
    for call in calls:
      if "(080)" in call[0]:
        if "(0" in call[1]:
          if call[1][1:4] not in areaCodes:
            areaCodes[call[1][1:4]]=1
          else:
            areaCodes[call[1][1:4]]+=1
        if " " in call[1]:
          if call[1][0:4] not in areaCodes:
            areaCodes[call[1][0:4]]=1
          else:
            areaCodes[call[1][0:4]]+=1
        if call[1].startswith("140"):
          if call[1][0:3] not in areaCodes:
            areaCodes[call[1][0:3]]=1
          else:
            areaCodes[call[1][0:3]]+=1
    print("The numbers called by people in Bangalore have codes:")
    
    sortedAreaCodes = {}
    sortedAreaCodes.update()
    for i in range(10000):
      for areaCode in areaCodes: 
        if int(areaCode)==i:
          print(areaCode)
    totalBangalore=0
    for areaCode in areaCodes: 
      totalBangalore+=areaCodes[areaCode]

    print("{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(round(int(areaCodes['080'])/totalBangalore*100,2)))
    
"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

""" Review
I think the previous reviewer accidentally missed pointing this out. As mentioned in the instructions below on line55 in this file, the area codes for fixed lines vary in length but always start with a 0 and is enclosed between brackets. Currently, the solution just considers the first three digits as the area code for such numbers whereas they can be of any length depending on the number of digits enclosed between the brackets. Like, as can be seen in the calls.csv file, there are fixed line numbers such as:
(04344)316423 for which the area code will be 04344
(04546)267875 for which the area code will be 04546

You might find the built-in split() method helpful here.

I can't mark this for re-submission now because the previous reviewer already passed this task, but would highly encourage you to make this correction.
"""