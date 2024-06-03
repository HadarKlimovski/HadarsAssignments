


import sys
import os
from datetime import datetime
from Bio import Entrez

# Set your email address
Entrez.email = "hadarkli123@gmail.com"

def search_input():
    if len(sys.argv) != 3:
        exit(f"Usage: {sys.argv[0]} TERM NUMBER")
    if not sys.argv[2].isnumeric():
        raise Exception("NUMBER needs to be a number")
    term = sys.argv[1]
    number_of_matches = int(sys.argv[2])
    return term, number_of_matches

def search_ncbi(term, number_of_matches):
    search = Entrez.esearch(db="protein", term=term, idtype="acc", retmax=number_of_matches)
    record = Entrez.read(search)
    return record

def fetch_ncbi(record):   
    data = []
    try:
        for Id in record["IdList"]:
            fetch = Entrez.efetch(db="protein", id=Id, rettype="gb", retmode="text")
            data.append(fetch.read())
    except UnboundLocalError:
        print("There is no such known protein")
        exit()
    return data

def file_saver(data, term):
    if not os.path.exists('output'):
        os.makedirs('output')
    
    filenames = []
    for i in range(len(data)):
        filename = f"output/{term}_match_{i+1}.gb"
        with open(filename, 'w') as fh:
            fh.write(data[i])
        filenames.append(filename)
        print(f"Saved: {filename}")   
    return filenames

def csv_creator(term, number_of_matches, count):
    filename = 'search.csv'
    with open(filename, 'a') as f:
        f.write(f"{datetime.now().strftime('%d/%m/%Y %H:%M:%S')},{term},{number_of_matches},{count}\n")

def main():
    term, number_of_matches = search_input()
    record = search_ncbi(term, number_of_matches)
    data = fetch_ncbi(record)
    files = file_saver(data, term)
    csv_creator(term, number_of_matches, record['Count'])

if __name__ == "__main__":
    main()
