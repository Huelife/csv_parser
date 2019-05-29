#csv_parser.py: Simple CSV parser

import csv

with open(input('.csv file: '),'r') as csvfile:
  read_data = csv.reader(csvfile)
  for row in read_data:
    print(row)
