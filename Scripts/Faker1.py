#to run python fake_data_script.py data.csv Name name City city Region region output.csv
#python faker1.py input_file.csv Name name Region state "Customer ID" random_int output_file_name23.csv

import argparse
import pandas as pd
from faker import Faker
from faker.providers.person.en_GB import Provider as EnGBProvider

# Function to replace column values with fake data
def replace_columns_with_fake_data(dataframe, column_mappings):
    fake = Faker('en_GB')
    fake.add_provider(EnGBProvider)
    fake = Faker()

    for column, fake_data_type in column_mappings.items():
        if fake_data_type == "name":
            dataframe[column] = dataframe[column].apply(lambda x: fake.name())
        elif fake_data_type == "address":
            dataframe[column] = dataframe[column].apply(lambda x: fake.address().replace("\n", ", "))
        elif fake_data_type == "email":
            dataframe[column] = dataframe[column].apply(lambda x: fake.email())
        elif fake_data_type == "phone_number":
            dataframe[column] = dataframe[column].apply(lambda x: fake.phone_number())
        elif fake_data_type == "date":
            dataframe[column] = dataframe[column].apply(lambda x: fake.date())
        elif fake_data_type == "company":
            dataframe[column] = dataframe[column].apply(lambda x: fake.company())
        elif fake_data_type == "job":
            dataframe[column] = dataframe[column].apply(lambda x: fake.job())
        elif fake_data_type == "text":
            dataframe[column] = dataframe[column].apply(lambda x: fake.text())
        elif fake_data_type == "random_int":
            dataframe[column] = dataframe[column].apply(lambda x: fake.random_int())
        elif fake_data_type == "random_element":
            dataframe[column] = dataframe[column].apply(lambda x: fake.random_element())
        elif fake_data_type == "random_digit":
            dataframe[column] = dataframe[column].apply(lambda x: fake.random_digit())
        elif fake_data_type == "random_letter":
            dataframe[column] = dataframe[column].apply(lambda x: fake.random_letter())
        elif fake_data_type == "city":
            dataframe[column] = dataframe[column].apply(lambda x: fake.city())
        elif fake_data_type == "state":
            dataframe[column] = dataframe[column].apply(lambda x: fake.state())
        elif fake_data_type == "firstname":
            dataframe[column] = dataframe[column].apply(lambda x: fake.first_name())
        elif fake_data_type == "lastname" or fake_data_type == "surname":
            dataframe[column] = dataframe[column].apply(lambda x: fake.last_name())
        else:
            print(f"Invalid fake data type for column {column}!")

    return dataframe

# Parse command-line arguments
parser = argparse.ArgumentParser(description='Replace column values with fake data.')
parser.add_argument('file', type=str, help='the name of the file containing the dataframe')
parser.add_argument('column_mappings', nargs='+', type=str, help='column and fake data type pairs')
parser.add_argument('output_file', type=str, help='the name of the output file')
args = parser.parse_args()

# Read the file into a dataframe
df = pd.read_csv(args.file)

# Parse column and fake data type mappings
column_mappings = {}
for i in range(0, len(args.column_mappings), 2):
    column_mappings[args.column_mappings[i]] = args.column_mappings[i + 1]

# Replace the specified columns with fake data
df = replace_columns_with_fake_data(df, column_mappings)

# Save the modified dataframe to the output file
df.to_csv(args.output_file, index=False)

print(f"Modified dataframe saved to {args.output_file}")
