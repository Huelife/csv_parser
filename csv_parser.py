#csv_parser.py: Simple CSV/TSV parser

import csv

#user input to open .csv/.tsv file and print to console
with open(input('Input: '),'r') as fin,open(input('Output: '),'w')) as fout:
  read_data = csv.reader(fin)
  write_data = csv.writer(fout)
  for row in read_data:
    print(row) #remove print command for quicker parsing
    write_data.writerow(row)
