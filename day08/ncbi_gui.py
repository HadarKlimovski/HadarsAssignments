import sys
import os
import ssl
from datetime import datetime
from Bio import Entrez
import tkinter as tk
from tkinter import messagebox

# Set your email address
Entrez.email = "hadarkli123@gmail.com"

# Disable SSL certificate verification
ssl._create_default_https_context = ssl._create_unverified_context

def test_ncbi_access():
    try:
        # Perform a simple search
        handle = Entrez.esearch(db="protein", term="hemoglobin", retmax=1)
        record = Entrez.read(handle)
        handle.close()
        
        # Check if the search was successful
        if "IdList" in record and len(record["IdList"]) > 0:
            return True
        else:
            return False
    except Exception as e:
        print(f"Error accessing NCBI Entrez API: {e}")
        return False

def search_ncbi(term, db):
    try:
        search = Entrez.esearch(db=db, term=term, idtype="acc", retmax=100)
        record = Entrez.read(search)
        return record
    except Exception as e:
        print(f"Error during NCBI search: {e}")
        return None

def fetch_ncbi(record, db, file_format, number_of_matches):
    data = []
    try:
        for Id in record["IdList"][:number_of_matches]:
            fetch = Entrez.efetch(db=db, id=Id, rettype=file_format, retmode="text")
            data.append(fetch.read())
    except UnboundLocalError:
        return None
    except Exception as e:
        print(f"Error during fetching data from NCBI: {e}")
        return None
    return data

def file_saver(data, term, file_format):
    if not os.path.exists('output'):
        os.makedirs('output')
    
    filenames = []
    for i in range(len(data)):
        ext = "gb" if file_format == "gb" else "fasta"
        filename = f"output/{term}_match_{i+1}.{ext}"
        with open(filename, 'w') as fh:
            fh.write(data[i])
        filenames.append(filename)
        print(f"Saved: {filename}")   
    return filenames

def csv_creator(term, number_of_matches, count):
    filename = 'search.csv'
    with open(filename, 'a') as f:
        f.write(f"{datetime.now().strftime('%d/%m/%Y %H:%M:%S')},{term},{number_of_matches},{count}\n")

def download_data(term, number_of_matches, db, file_format):
    record = search_ncbi(term, db)
    if record is None:
        return None, 0
    data = fetch_ncbi(record, db, file_format, number_of_matches)
    if data is None:
        return None, int(record['Count'])
    files = file_saver(data, term, file_format)
    csv_creator(term, number_of_matches, record['Count'])
    return files, int(record['Count'])

def main():
    def on_search():
        if not test_ncbi_access():
            result_label.config(text="NCBI Entrez API is not accessible. Please check your network connection or try again later.", fg="red")
            return
        
        term = term_entry.get()
        db = db_var.get()

        if not term:
            messagebox.showerror("Input Error", "Please fill in the search term.")
            return

        record = search_ncbi(term, db)
        if record is None:
            result_label.config(text="Error during search. Please check the term or try again later.", fg="red")
            return
        
        count = int(record['Count'])
        if count > 0:
            result_label.config(text=f"Found {count} matches.", fg="green")
        else:
            result_label.config(text="No matches found.", fg="red")
    
    def on_download():
        term = term_entry.get()
        number_of_matches = download_entry.get()

        if not term or not number_of_matches:
            messagebox.showerror("Input Error", "Please fill in all fields.")
            return

        try:
            number_of_matches = int(number_of_matches)
        except ValueError:
            messagebox.showerror("Input Error", "Number of matches to download must be an integer.")
            return

        db = db_var.get()
        file_format = format_var.get()
        files, count = download_data(term, number_of_matches, db, file_format)
        if files is None:
            messagebox.showerror("Error", f"No matches found or an error occurred during download. Matches found: {count}")
        else:
            messagebox.showinfo("Download Complete", f"Downloaded {len(files)} files.")

    root = tk.Tk()
    root.title("NCBI Data Downloader")

    tk.Label(root, text="Search Term or Accession Number:").grid(row=0, column=0, padx=10, pady=5)
    term_entry = tk.Entry(root)
    term_entry.grid(row=0, column=1, padx=10, pady=5)

    search_button = tk.Button(root, text="Search", command=on_search)
    search_button.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

    result_label = tk.Label(root, text="", font=("Helvetica", 12))
    result_label.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

    tk.Label(root, text="How Many to Download:").grid(row=3, column=0, padx=10, pady=5)
    download_entry = tk.Entry(root)
    download_entry.grid(row=3, column=1, padx=10, pady=5)

    tk.Label(root, text="Database:").grid(row=4, column=0, padx=10, pady=5)
    db_var = tk.StringVar(root)
    db_var.set("protein")
    db_options = ["protein", "nucleotide"]
    db_menu = tk.OptionMenu(root, db_var, *db_options)
    db_menu.grid(row=4, column=1, padx=10, pady=5)

    tk.Label(root, text="File Format:").grid(row=5, column=0, padx=10, pady=5)
    format_var = tk.StringVar(root)
    format_var.set("gb")
    format_options = ["gb", "fasta"]
    format_menu = tk.OptionMenu(root, format_var, *format_options)
    format_menu.grid(row=5, column=1, padx=10, pady=5)

    download_button = tk.Button(root, text="Download Data", command=on_download)
    download_button.grid(row=6, column=0, columnspan=2, padx=10, pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()
