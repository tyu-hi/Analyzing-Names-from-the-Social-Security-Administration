import pandas as pd

# Load dataset
df = pd.read_csv('1989-2022.csv', header=None, names=['Name', 'Gender', 'Count', 'Year'])

def extract_name_rows(df, names, start_year, end_year):
    # Make sure we strip any leading/trailing whitespace from the name entries
    df['Name'] = df['Name'].str.strip()
    # Filter the dataframe for the rows where the name column matches the input names, gender is not specified,
    # and the year is between start_year and end_year (inclusive)
    result = df[(df['Name'].isin(names)) & (df['Year'].between(start_year, end_year))]
    return result

# Gender-neutral names to search for
names_to_search = ['Alex', 'Avery', 'Taylor', 'Jordan', 'Riley']
start_year = 1972
end_year = 2022
extracted_rows = extract_name_rows(df, names_to_search, start_year, end_year)

# Save the extracted rows to a new CSV file
extracted_rows.to_csv('extracted_data.csv', index=False)
