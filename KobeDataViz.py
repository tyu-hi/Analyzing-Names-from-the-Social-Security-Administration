import pandas as pd

# Load dataset
df = pd.read_csv('1989-2022.csv', header=None, names=['Name', 'Gender', 'Frequency', 'Year'])

def extract_name_rows(df, name):
    # Strip any leading/trailing whitespace from the name entries
    df['Name'] = df['Name'].str.strip()
    # Filter the dataframe for the rows where the Name column matches the input name exactly
    result = df[(df['Name'] == name) & (df['Gender'] != 'F')]
    # Further filter the rows to include only those with years between 1998 and 2022
    result = result[(result['Year'] >= 1990) & (result['Year'] <= 2022)]
    return result

name_to_search = 'Kobe'
extracted_rows = extract_name_rows(df, name_to_search)
print(extracted_rows)
# Save the extracted rows to a new CSV file
extracted_rows.to_csv('extracted_kobe.csv', index=False)
