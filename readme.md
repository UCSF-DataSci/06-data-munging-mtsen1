# Data Issues and Fixes

## Missing Values
- Description: all of the columns of the dataframe have several thousand missing values
- Columns affected: income_groups, age, gender, year, population
- Example: columns have several NaN values
- Potential impact: leaving the missing values can impact statisical analyses that require complete data.

### Removing Missing Values
- Removed all NaN values using ```df.dropna()```
- This is the simplest way to remove NaN values. Filling NaN values with the average for numerical variables was possible but may not be the best option without knowing what the data is used for.
- Several thousand rows were removed from this step due to sheer amount of NaNs in the data

## Duplicate Rows
- Description: 2950 rows are duplicates of each other
- Columns affected: all columns are affected 
- Example:
    - Duplicates include:
    ```
    [high_income, 11.0, 1.0, NaN, NaN]
    [high_income, 11.0, 1.0, NaN, NaN]
    ```
- Potential impact: if the rows are duplicates by mistake, this can skew the data and provide misinformation.

### Removing Duplicate Rows
- Removed all duplicate rows with ```df.drop_duplicates()```
- This was also the simplest way to remove duplicate rows
- Around 2000 rows were removed
- Assumptions: the duplicate rows were from error and not conincidence

## Incorrect Datatypes
- Description: columns may not be in the correct datatype. (Checking the type of data on this data frame revealed that all of the types were correct)
- Columns affected: None, but based on the dirty-data.py, year and population should be incorrectly categorized as str
- Example: years and population appear as strings instead of integers
- Potential impact: numerical analysis and specific functions will not work if the datatype is incorrect

### Fixing Datatypes
- Converted the year and population columns to integers with ```df['year'].astype(int)```
- This was the most direct way to convert the two columns to integers
- Assumptions: we assume that year should be an integer rather than a date type

## Outliers
- Description: outliers and extreme values may be present in the data (Checking for outliers through the IQR method found no outliers)
- Columns affected: all the numeric columns may be affected
- Example: no outliers were found but hypothetically, there may be a population value of <100 which would be an outlier
- Potential impact: several outliers can skew analysis towards the outlier which can cause misrepresentations of the data.

### Removing Outliers
- Removed all outliers by finding the IQR and then removing all values below and above the standard criteria
- The Z-score method was considered but was uncertain how many standard deviations away should be considered an outlier. Additionally, the Z-score method assumes normality.
- In this dataset, no outliers were found
- Assumptions: the IQR method assumes the data points are independent of each other

## Inconsistant Categories
- Description: there are multiple typos in the income_groups category and errors in the gender category
- Columns affected: income_groups and gender
- Example: there are values such as 'low_income' and 'low_income_typo' in the income_groups category and '1', '2', '3' for the gender category (assuming '1' and '2' are the original categories)
- Potential impact: groups will not be analyzed properly if groups such as 'low_income' and 'low_income_typo' are considered different groups.  

### Fixing Inconsistant Categories
- Replaced all income groups with the "_typo" with the correct groups and removed category 3 in gender. For instance, "low_income_typo" became "low_income."
- For the income groups, this method is simple and is ok when there are not many incorrect groups. Excluding all 3s is necessary if 3 is an unknown value.
- Several rows with the typo income groups were switched to the correct income group and about 6000 3s were removed.
- Assumptions: we assume that the typos such as "low_income_typo" are supposed to be "low_income" and not another category.

## Incorrect Dates
- Description: there are some years that are in the future and should be excluded
- Columns affected: years
- Example: some years such as 2115 and 2110 are in the column
- Potential impact: impossible dates are likely errors and will skew the data if not removed.

### Fixing Future Dates
- Removed all future years by only including years from 2024 and below: ```df[df['year'] <= 2024]```
- This is was a simple way to remove years that are seemingly impossible
- Several rows were removed from this method
- Assumptions: we assume that any year above 2024 is invalid

## Conclusion
The cleaned dataset should have no missing values, impossible values, incorrect categories, etc. There are approximately 40,000 rows compared to the ~122,000 in the original data. The most difficult part was identifying the issues and finding the best way to solve each problem. However, this could be overcome by taking the time to go through each potential problem and finding available pandas and numpy functions.

From this project, I learned that data cleaning can be variable depending on the person cleaning. For instance, there are multiple ways to deal with one problem and picking the best solution depends on the project goals and/or the person's preferences. For potential future steps, I would like to explore ways to clean the data that would preserve more data since my cleaned data ended up being much smaller than the original. 

