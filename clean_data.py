import pandas as pd
import numpy as np

# load data
def load_data(filename):
    return pd.read_csv(filename)

# Remove NaN values 
def remove_nan(df):
    df = df.dropna()  
    return df

# Correct datatypes
def fix_data_types(df):
    df['year'] = df['year'].astype(int) # switch year to integer
    df['population'] = df['population'].astype(int) # swithc population to integer
    return df

# Remove duplicate rows
def remove_dupes(df):
    df = df.drop_duplicates()
    return df

# Fix inconsistent categories
def inconsistent_categories(df):
    # replace all typos with the correct category
    income_fix = {
        'lower_middle_income_typo': 'lower_middle_income',
        'low_income_typo': 'low_income',
        'high_income_typo': 'high_income',
        'upper_middle_income_typo': 'upper_middle_income',
    }
    df['income_groups'] = df['income_groups'].replace(income_fix)
    df = df[df['gender'] != 3.0] # remove all 3s from gender
    return df

# Remove impossible future dates
def future_dates(df):
    df = df[df['year'] <= 2024] # keep only dates from 2024 and back
    return df

# Removing outliers
def remove_outliers(df): # using the IQR method to remove outliers 
    num_cols = df.select_dtypes(include=[np.number])

    # find the 25th and 75 quantiles
    Q1 = num_cols.quantile(0.25) 
    Q3 = num_cols.quantile(0.75)
    IQR = Q3 - Q1 # find the IQR
    
    # find the upper and lower bounds for outliers
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    # keep only values within the bounds
    df = df[~((num_cols < lower_bound) | (num_cols > upper_bound)).any(axis=1)]
    return df

# Save cleaned DataFrame to CSV
def save_data(df, output_file_path):
    df.to_csv(output_file_path, index=False)

def main():
    input_filename = 'messy_population_data.csv'
    output_filename = 'cleaned_population_data.csv'

    df = load_data(input_filename)
    df = remove_nan(df)
    df = fix_data_types(df)
    df = remove_dupes(df)
    df = inconsistent_categories(df)
    df = future_dates(df)
    df = remove_outliers(df)

    save_data(df, output_filename)

if __name__ == "__main__":
    main()