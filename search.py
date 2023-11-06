import sys
import set_generator
import logging

def load_numbered_words(filename):
    word_dict = {}
    with open(filename, 'r') as f:
        for line in f:
            word, number = line.strip().split(": ")
            word_dict[word] = number
    
    # Sort words by the length of their number, longest first
    sorted_words = dict(sorted(word_dict.items(), key=lambda item: len(item[1]), reverse=True))
    return sorted_words


def print_results_table(columns):
    if not columns:
        print("Empty table")
        return
    
    print("A result:")
    # Find the maximum number of rows
    max_rows = max(len(column) for column in columns)
    columns = [sorted(lst, key=len) for lst in columns]

    
    # Find the maximum width of each column
    column_widths=[]
    for column in columns: 
        length=len(max(column, key =len))
        column_widths.append(length)
    # Print the table
    for row_index in range(min(max_rows,40)):
        formatted_row = [str(column[row_index]).ljust(width) if row_index < len(column) else ''.ljust(width) for column, width in zip(columns, column_widths)]
        print(" | ".join(formatted_row))

    
