# pandas.exam.practice
This repository is for the Unit 1 - Activity 3 - Practice Exam
Below this are the things to do:

1. Missing values
Which instruction creates a new column sales_filled where missing sales values
are replaced with 0? Provide the full line of code.
2. Cleaning
You see the DataFrame below showing rows where discount is negative:
index order_date region sales discount
6 2025-07-07 East 100.0 -5.0
10 2025-07-11 East NaN -10.0
Which command would you use to replace negative discount values with NaN for the
entire column?
3. Cleaning
What is the result of dropping rows where both sales and discount are missing (use
one command)? Show the resulting DataFrame.
4. Filtering
The DataFrame below shows rows where region is "West" but sales is missing:
index order_date region sales discount
7 2025-07-08 West NaN 20.0
Which command produces this subset?

5. Filling
After setting negative discount to NaN, and then filling all remaining missing
discount values with the mean of the non-missing discount column, what would be
the new discount value at index 2? Use the mean of the column to fill them. Show the
single line of code for filling missing discount values.
6. New columns
You want to create a column net_sales calculated as sales * (1 -
discount/100) but only for rows where both sales and discount are nonmissing.
Which command (using loc) ensures net_sales is only computed where neither is
NaN, leaving other rows as NaN?
7. Filtering
What is the DataFrame resulting from filtering rows where sales is greater than or
equal to 200 and discount is less than or equal to 10? Show the resulting DataFrame.
8. Dates and Sorting
The DataFrame below shows rows sorted by order_date descending where sales is
not NaN:
index order_date region sales discount
11 2025-07-12 West 275.0 15.0
9 2025-07-10 South 220.0 NaN
8 2025-07-09 North 180.0 5.0
5 2025-07-06 South 200.0 0.0
3 2025-07-04 West 300.0 10.0
Which pandas commands (chain) produce that result?
9. Value conversion
If you want to convert the order_date column to datetime and then extract the
weekday name into a new column weekday, what two lines of code would you use?
10. Dropping
After cleaning and filling missing values, you want to drop any column that has all values
missing. Which command do you run?