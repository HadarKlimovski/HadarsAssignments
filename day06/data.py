pip install pandas
import pandas as pd

def load_data(filepath):
    """ Load the Excel file. """
    return pd.read_excel(filepath)

def main():
    filepath = '/Users/hadarklimovski/Desktop/git/HadarsAssignments/protein_clinical_thresold_402.xlsx'
    data = load_data(filepath)
    
    # Exclude the first column (sample names) and the last two columns (survival time and event)
    protein_data = data.iloc[:, 1:-2]
    
    # Calculate statistics
    means = protein_data.mean()
    medians = protein_data.median()
    std_devs = protein_data.std()
    
    print("Means:\n", means)
    print("Medians:\n", medians)
    print("Standard Deviations:\n", std_devs)

if __name__ == "__main__":
    main()
