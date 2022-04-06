import difflib
from difflib import Differ

with open('file_1.cfg') as file_1:
    file_1_text = file_1.readlines()
  
with open('file_2.cfg') as file_2:
    file_2_text = file_2.readlines()

output2 = []

# Find and print the diff:
for line in difflib.unified_diff(
        file_1_text, file_2_text, fromfile='file1.txt', 
        tofile='file2.txt', lineterm=''):
    #print(line)
    output2.append(line)

i = 1

counter = False

for line2 in output2:
    #print(line2)
    if "---" in line2 or "+++" in line2 or "@@" in line2 or "# Built" in line2 or "# Configuration format version" in line2 or "# Generated" in line2 or '# Finished' in line2 or 'UTC:' in line2:
        continue
    elif line2[0] == '+':
        counter = True
        #line3 = line2.split('+')
        #print(f"The differences in file_2: \n {line3[1]}")
        output = f"{i}. difference in file_2: \n {line3[1]}\n{'-'*80}\n"
        with open("differences.txt", "a") as f:
            f.write(output)
        i = i + 1
    elif line2[0] == '-':
        counter = True
        line3 = line2.split('-')
        #print(f"The differences in file_1: \n {line3[1]}")
        output = f"{i}. difference in file_1: \n {line3[1]}\n"
        with open("differences.txt", "a") as f:
            f.write(output)
        i = i + 1
    # print(line2)

if counter == False:
    print("No differences observed between two config files.")
else:
    print("There are differences between two config files. Please check 'differences.txt' file to see differences. This may give you a hint regarding to issue.")
