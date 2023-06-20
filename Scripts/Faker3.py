import argparse
import pandas as pd
from faker import Faker

# Function to replace column values with fake data
#  py Faker3.py config.txt

def replace_columns_with_fake_data(dataframe, column_mappings):
    fake = Faker()

    for column, fake_data_type in column_mappings.items():
        if fake_data_type == "name":
            dataframe[column] = dataframe[column].apply(lambda x: fake.name())
        elif fake_data_type == "random_int":
            dataframe[column] = dataframe[column].apply(lambda x: fake.random_int())
        elif fake_data_type == "city":
            dataframe[column] = dataframe[column].apply(lambda x: fake.city())
        elif fake_data_type == "state":
            dataframe[column] = dataframe[column].apply(lambda x: fake.state())
        else:
            print(f"Invalid fake data type for column {column}!")

    return dataframe

# Parse command-line arguments
parser = argparse.ArgumentParser(description='Replace column values with fake data.')
parser.add_argument('config_file', type=str, help='the name of the configuration file')
args = parser.parse_args()

# Read the configuration file
config = []
with open(args.config_file, 'r') as file:
    for line in file:
        config.append(line.strip().split())

# Process each configuration entry
for entry in config:
    input_file, *column_mappings, output_file = entry

    # Read the input file into a dataframe
    df = pd.read_csv(input_file)

    # Create a dictionary to store column and fake data type mappings
    mapping_dict = {}
    for i in range(0, len(column_mappings), 2):
        mapping_dict[column_mappings[i]] = column_mappings[i + 1]

    # Replace the specified columns with fake data
    df = replace_columns_with_fake_data(df, mapping_dict)

    # Save the modified dataframe to the output file
    df.to_csv(output_file, index=False)

    print(f"Modified dataframe saved to {output_file}")
