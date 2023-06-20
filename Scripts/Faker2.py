import argparse
import csv
import pandas as pd
from faker import Faker

# Function to mask specified fields with fake data
def mask_fields(dataframe, masked_fields):
    fake = Faker()
    
    for field in masked_fields:
        dataframe[field] = dataframe[field].apply(lambda x: fake.name())
    
    return dataframe

# Parse command-line arguments
parser = argparse.ArgumentParser(description='Mask specified fields in a CSV file with fake data.')
parser.add_argument('config_file', type=str, help='the name of the configuration file')
args = parser.parse_args()

# Read the configuration file
config = []
with open(args.config_file, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        config.append(row)

# Process each configuration entry
for entry in config:
    input_file, *masked_fields, output_file = entry

    # Read the input file into a dataframe
    df = pd.read_csv(input_file)

    # Mask the specified fields with fake data
    df = mask_fields(df, masked_fields)

    # Save the modified dataframe to the output file
    df.to_csv(output_file, index=False)

    print(f"Masked dataframe saved to {output_file}")
