#pip install pytest
import pytest
from data_analysis import load_data, compute_statistics

def test_compute_statistics():
    filepath = '/Users/hadarklimovski/Desktop/git/HadarsAssignments/protein_clinical_thresold_402.xlsx'
    data = load_data(filepath)
    stats = compute_statistics(data)

    # Use a few specific proteins as examples
    # Replace 'Protein1', 'Protein2', etc., with actual protein names from your output
    expected_means = {'IGLV4-69': -10.727607, 'IGLV8-61': -10.518967, 'C1QA_1': -10.742491}
    expected_medians = {'IGLV4-69': -10.731334, 'IGLV8-61': -10.513980, 'C1QA_1': -10.728861}
    expected_stds = {'IGLV4-69': 0.091738, 'IGLV8-61': 0.078919, 'C1QA_1': 0.075402}

    # Assert conditions to check if the calculated statistics match the expected values
    assert abs(stats['means']['IGLV4-69'] - expected_means['IGLV4-69']) < 0.001, "Mean calculation is incorrect for IGLV4-69"
    assert abs(stats['medians']['IGLV4-69'] - expected_medians['IGLV4-69']) < 0.001, "Median calculation is incorrect for IGLV4-69"
    assert abs(stats['std_devs']['IGLV4-69'] - expected_stds['IGLV4-69']) < 0.001, "Standard deviation calculation is incorrect for IGLV4-69"

  
