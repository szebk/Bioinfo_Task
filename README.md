# Bioinfo_Task_TSV
Write me a program in python that will take a TSV (tab-delimited text file) as input and to the following: 
1. extract the last column
2. remove any header if it is there 
3. sort the value 
4. print in the terminal


python programming language

import sys

def extract_sort_print(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
        
    # remove header if it exists
    if len(lines) > 0 and "\t" in lines[0]:
        lines = lines[1:]
        
    # extract the last column
    last_column = [line.strip().split("\t")[-1] for line in lines]
    
    # sort the values
    last_column.sort()
    
    # print the values
    for value in last_column:
        print(value)

if __name__ == "__main__":
    filename = sys.argv[1]
    extract_sort_print(filename)

We can run the program by passing the filename as an argument:


$ python program.py input.tsv
