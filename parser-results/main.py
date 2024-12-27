import csv
import re

def extract_and_save_emails(input_file, output_file):
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = set() 

    
    delimiter = ','

    with open(input_file, 'r', encoding='utf-8') as infile, \
         open(output_file, 'w', encoding='utf-8') as outfile:
        reader = csv.reader(infile, delimiter=delimiter)
        for row in reader:
            for item in row:
                matches = re.findall(email_pattern, item)
                emails.update(matches)

        for email in emails:
            outfile.write(email + '\n')

input_filename = 'kz-pars1.csv'
output_filename = 'pars-mail-1.txt'

extract_and_save_emails(input_filename, output_filename)