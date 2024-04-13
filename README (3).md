#Amazon Sale Report


This report provides a summary of sales orders for the Amazon marketplace, including order details, fulfillment, sales channel, courier status, quantity, currency, and amount.

Order Summary

The report contains 60 orders, with a total of 60 items sold.

Order Details

The following table shows the order details for each order:

| Index | Order ID | Date | Status | Fulfillment | Sales Channel | Ship Service Level | Category | Size | Courier Status | Qty | Currency | Amount | Ship City | Ship State | Ship Postal Code | Ship Country | B2B | Fulfilled By | New | PendingS |

About data

The dataset is a CSV file named "Amazon Sale Report.csv" containing information about sales orders on Amazon.

The file includes various data points such as the order ID, date, status, fulfillment, sales channel, ship service level, category, size, courier status, quantity, currency, amount, ship city, ship state, ship postal code, ship country, B2B, fulfilled by, new, and pendings.

The dataset contains 60 orders, with a total of 60 items sold. The orders were made on the 30th of April, 2022. 

Purposes Of The Project

This dataset can be used for various purposes, such as tracking sales performance, monitoring order status, and identifying trends in customer orders.

It can also be used to analyze sales patterns, identify popular products, and optimize shipping and delivery processes.

The dataset can be useful for sellers, merchants, and Amazon itself to improve their sales, customer service, and overall business performance.

Approach Used

In the initial step of data analysis, data wrangling is performed to identify and handle missing or null values in the dataset. This is followed by exploratory data analysis (EDA), which involves utilizing various commands to extract valuable insights from the dataset. The commands used in this project include:

head(): This function displays the first N rows of the dataframe, with N being 5 by default.

shape: This attribute provides the total number of rows and columns in the dataframe.

index: This attribute displays the index of the dataframe.
columns: This attribute displays the names of each column in the dataframe.

dtypes: This attribute displays the data type of each column in the dataframe.

unique(): This function displays all unique values in a single column, and can only be applied to one column at a time.

nunique(): This function displays the total number of unique values in each column, and can be applied to either a single column or the entire dataframe.

count: This function displays the total number of non-null values in each column, and can be applied to either a single column or the entire dataframe.

value_counts: This function displays all unique values in a single column along with their count, and can only be applied to one column at a time.

info(): This function provides basic information about the dataframe, including the data types, memory usage, and number of non-null values in each column.

In this project, the dataset used is the Amazon Sale Report, which contains 60 rows and 19 columns. The dataframe includes information about each sale, such as the order ID, date, status, fulfillment method, sales channel, ship service level, category, size, courier status, quantity, currency, amount, shipping information, and whether the sale was B2B. The dataset was analyzed using Python libraries such as pandas, matplotlib, and seaborn.

Future scope

Popular Products and Categories: By analyzing the sales data, trends in popular products and categories can be identified. This can help predict which products are likely to perform well in the future.

Seasonal Trends: Looking at the sales data over different time periods, seasonal trends can be observed. For example, certain products may sell more during specific seasons or holidays.

Geographical Trends: Analyzing sales data based on the location of customers can reveal geographical trends. This information can be used to tailor marketing strategies to specific regions.

Order Fulfillment Trends: Understanding trends in order fulfillment, such as shipping times and service levels, can help predict customer satisfaction levels and optimize logistics processes.

Cancellation and Return Trends: Monitoring trends in order cancellations and returns can provide insights into customer behavior and product satisfaction levels.

Sales Channel Performance: Analyzing sales data across different sales channels can help predict the performance of each channel and guide decisions on where to focus marketing efforts.