#Isaiah Corrales
#Program 4, CMPS-4143-102
#October 28th, 2024
#This program will

import re

with open('alice.txt','r') as file:
    content = file.read()
    res = re.findall(r'\(([^)]+)\)', content)
    matches_sorted = sorted(res, key = lambda x: x[0])

with open('output.txt', 'w') as outfile:
    outfile.write("#Isaiah Corrales\n")
    outfile.write("#Program 4 Output, CMPS-4143-102\n")
    outfile.write("#October 28th, 2024\n\n")
    outfile.write("Extracted and Processed data:\n\n")
    line_count = 0
    for match in matches_sorted:
        word_count = len(match.split())
        outfile.write(f"{match} (words: {word_count})\n")
        line_count += 1
    outfile.write(f"\n Total lines (excluding header): {line_count}\n")



print(f"Results written to 'output.txt' with {line_count} lines (excluding header).")
