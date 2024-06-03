### Main Goal of the Program :
This program automates the process of searching the NCBI protein database for a specified term, downloading a specified number of results, saving each result to a file, and logging the search details in a CSV file.

### Information About the Code:
- Import Required Modules: sys, os, datetime, and Bio from Biopython.
- search_input Function: Validates that the script is called with exactly two arguments, TERM and NUMBER, ensuring NUMBER is numeric.
- search_ncbi Function: Uses Biopython's Entrez module to search the NCBI protein database for a term and retrieves the specified number of matches.
- fetch_ncbi Function: Retrieves detailed data for each protein ID from the search results and stores it in a list.
- file_saver Function: Saves each fetched protein data to a separate file in the 'output' directory and returns a list of filenames.
- csv_creator Function: Appends a log entry to search.csv : This log helps track what searches were performed and their results.
- main Function: Manages the entire workflow: handling input, querying NCBI, fetching data, saving files, and logging search details.
- To run the script with the term "Orchid" and download 3 matches, use: python ncbi.py Orchid 3.
-  To run the script with the term "cauliflower" and download 7 matches, use: python ncbi.py cauliflower 7.
