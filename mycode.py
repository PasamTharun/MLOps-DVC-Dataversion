import pandas as pd 
import os

#create a sample dataframe with column names
data={
    'Name': ['Pasam','Tharun','Chinna'],
    'Age': [25,22,35],
    'City': ['Hyderabad','Banglore','Chennai']
}

df=pd.DataFrame(data)

#Ensure the "data" directory exists at the root level
data_dir = 'data'
os.makedirs(data_dir,exist_ok=True)

#define the file path
file_path = os.path.join(data_dir,'sample_data.csv')

#save the dataframe to acsv file, including column names 
df.to_csv(file_path,index=False)

print(f"CSV file saved to {file_path}")