# Bioinfo_Task_TSV
Write me a program in python that will take a TSV (tab-delimited text file) as input and to the following: 
1. extract the last column
2. remove any header if it is there 
3. sort the value 
4. print in the terminal


python programming language

This program reads a tab-separated values (TSV) file named expmat.tsv, performs the following operations on its content, and outputs the result in the terminal:

read_tsv function: This function reads the contents of the file and stores them in a list of lists, where each inner list represents a row in the file and each element in the inner list represents a column. The function returns this data.

extract_last_column function: This function takes the data from the read_tsv function and extracts the last column, which is represented as the last element in each inner list. The function returns this last column as a separate list.

remove_header function: This function removes the header row from the data if it is present. The header is assumed to be the first row in the file and is removed using the remove method. The function returns the data without the header.

sort_values function: This function sorts the values in the last column list in ascending order using the sorted function. The function returns the sorted list.

print_values function: This function prints each value in the sorted last column list.

The if __name__ == '__main__' block: This block is executed only when the program is run as the main program and not imported as a module. It sets the file name to be expmat.tsv, calls the read_tsv function, stores the result in a variable named data, calls the extract_last_column function and stores the result in a variable named last_column, calls the remove_header function to remove the header if present, calls the sort_values function to sort the values, and finally calls the print_values function to print the sorted values in the terminal.

I hope this program is helpful for your bioinformatics tasks. I would like to extend my sincere gratitude for the opportunity to work on this project. Additionally, I am highly interested in joining your lab to further my knowledge and skills in the field of bioinformatics.
