#csv_parser.py: Simple CSV/TSV parser

import csv

#user input to open .csv/.tsv file and print to console
with open(input('.csv/.tsv file name: '),'r') as csvfile:
  read_data = csv.reader(csvfile)
  for row in read_data:
    print(row)
