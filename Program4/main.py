#Isaiah Corrales
#Program 4, CMPS-4143-102
#October 28th, 2024
#This program will read in a txt file, it will find all text within parentheses using regex combinations,
#after it sorts the results it will output the results into a txt file.

import re

#opens the file we read from ("alice.txt")
with open('alice.txt','r') as file:
    #saves the text to a variable
    content = file.read()
    #res is the results we get after using findall and a regex combination to find all text within parentheses
    res = re.findall(r'\(([^)]+)\)', content)
    #the sorted function used here sorts the entries (A-Z) based on the first word 
    matches_sorted = sorted(res)

#output formatting
with open('output.txt', 'w') as outfile:
    outfile.write("#Isaiah Corrales\n")
    outfile.write("#Program 4 Output, CMPS-4143-102\n")
    outfile.write("#October 28th, 2024\n\n")
    outfile.write("Formatted Results\n\n")
    line_count = 0
    #this is a for loop that calls every element that is found a "match"
    for match in matches_sorted:
        # .split is used to split the lines into their own sepreate words, and len counts how many elements are in the list
        word_count = len(match.split())
        outfile.write(f"{match} (words: {word_count})\n")
        line_count += 1
    outfile.write(f"\n Total lines (excluding header): {line_count}\n")



print(f"Results written to 'output.txt' with {line_count} lines (excluding header).")
