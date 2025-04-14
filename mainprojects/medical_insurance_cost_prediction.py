from urllib.request import urlretrieve
import pandas as pd

# Use raw GitHub URL for proper CSV download
csv_url = 'https://raw.githubusercontent.com/stedy/Machine-Learning-with-R-datasets/master/insurance.csv'

# Download and print the CSV
urlretrieve(csv_url, 'insurance.csv')
medical_df = pd.read_csv('insurance.csv')

print (medical_df.info())
