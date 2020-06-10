import pandas as pd
import numpy as np

retailers_data = pd.read_csv('retailersperzip.csv')
density_data = pd.read_csv('densities.csv')

retailers_data.sort_values(by=['zip'])
retailers_data.replace('', np.nan, inplace=True)

retailers_data.dropna(subset=['zip'], inplace=True)

retailers_counts = retailers_data['zip'].value_counts()

retailers_per_zip = retailers_counts.reset_index(name='zip')
retailers_per_zip = retailers_per_zip[retailers_per_zip['index'] !='No zipcode listed']
retailers_per_zip['index'] = [i.split("-")[0]  if "-" in i else i for i in retailers_per_zip['index']]

density_data = density_data.drop(density_data.index[:1104])

comparison_data = pd.DataFrame(columns=['zip', 'enrollees', 'retailer'])
comparison_data['zip'] = retailers_per_zip['index']


for i in range(len(retailers_per_zip['index'])):
    if(retailers_per_zip['index'][i] in comparison_data['zip'].values):
        comparison_data['retailer'][i] == comparison_data['zip'][i]
print(comparison_data)