import pandas as pd 
import os

#create a sample dataframe with column names
data={
    'Name': ['Pasam','Tharun','Chinna'],
    'Age': [25,22,35],
    'City': ['Hyderabad','Banglore','Chennai']
}

df=pd.DataFrame(data)

#adding new row to df for v2
new_row_loc={'Name':'Kav','Age':22,'City':'Mumbai'}
df.loc[len(df.index)]=new_row_loc

#adding new row to df fpr v3
#new_row_loc2={'Name':'Anu','Age':28,'City':'Pune'}
#df.loc[len(df.index)]=new_row_loc2

#Ensure the "data" directory exists at the root level
data_dir = 'data'
os.makedirs(data_dir,exist_ok=True)

#define the file path
file_path = os.path.join(data_dir,'sample_data.csv')

#save the dataframe to acsv file, including column names 
df.to_csv(file_path,index=False)

print(f"CSV file saved to {file_path}")