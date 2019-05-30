#csv_parser.py: Simple CSV parser

import csv

#user input to open .csv file and print to console
with open(input('.csv file name: '),'r') as csvfile:
  read_data = csv.reader(csvfile)
  for row in read_data:
    print(row)
