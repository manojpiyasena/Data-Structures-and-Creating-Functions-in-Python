#!/usr/bin/env python
# coding: utf-8

# ## Mission 3 - Exploratory Data Analysis (EDA) with the Sales Dataset using Pandas and d Matplotlib_Seaborn
# 
# New notebook

# # **Mission 3 - Exploratory Data Analysis (EDA) with the Sales Dataset using Pandas and d Matplotlib/Seaborn**
# 
# ### **Objective:**
# 
# The goal of this assignment is to help you apply your knowledge of Python for basic operations, Pandas for data manipulation, and Matplotlib/Seaborn for visualizations. You'll be working with a real-world dataset, and your tasks will include loading the data, performing EDA, and visualising the results.
# 
# ###  **Dataset**
# 
# The dataset represents transaction data from a retail business, specifically sales data for products sold in various stores. It contains multiple tables that provide insights into sales, invoices, and products. Let’s break down the tables and what they represent:
# 
# #### Sales Table:
# 
# InvoiceNo: The unique identifier for each invoice (or transaction).
# 
# StockCode: A unique identifier for each product.
# 
# Quantity: The number of units sold in each transaction.
# 
# UnitPrice: The price per unit of the product.
# 
# InvoiceDate: The date when the transaction occurred.
# 
# #### Invoice Table:
# 
# InvoiceNo: The same unique identifier for each invoice, linking the sales data with the invoice details.
# 
# Country: The country where the sale was made.
# 
# #### Product Table:
# 
# StockCode: A unique identifier for each product.
# 
# Description: The name or description of the product.
# 
# Product_Category: The category the product belongs to (e.g., "Gift", "Sign", "Mug").
# 
# 
# 
# You will need to merge them and perform the following tasks step by step.
# 

# ### Task 1: Load the Excel File
# #### Objective: Import the data from the provided Excel file into Python using Pandas.
# 
# Instructions:
# 
# 1. Upload the provided excel file into Fabric environment
# 2. Read each sheet of the excel file as a separate dataframe. 
# 3. Name the dataframe for sales as df_sales, the dataframe for invoice as df_invoice and the dataframe for product as df_product
# 4. Display the first few rows of each DataFrame to understand its structure.
# 
# 

# In[2]:


## Code Task 1 here

import pandas as pd
##2
df_sales = pd.read_excel(f"{notebookutils.nbResPath}/builtin/OnlineSalesRetailer.xlsx", sheet_name= 'Sales')
df_invoice = pd.read_excel(f"{notebookutils.nbResPath}/builtin/OnlineSalesRetailer.xlsx", sheet_name= 'Invoice')
df_product = pd.read_excel(f"{notebookutils.nbResPath}/builtin/OnlineSalesRetailer.xlsx", sheet_name= 'Product')
##3
display(df_sales.head(5))
display(df_invoice.head(5))
display(df_product.head(5))


# ### Task 2: Basic Python and Pandas Operations
# #### Objective: Perform basic Python and Pandas operations to manipulate the data.
# 
# <mark>Instructions:</mark>
# 
# 1. Create the Sales Column (Quantity * Unit Price) 
# 
# 2. Check for missing values in the Sales DataFrame.
# 
# 3. Replace any NaN values in the Sales and UnitPrice columns with 0.
# 
# 4. Calculate basic descriptive statistics for the Quantity and UnitPrice columns (mean, median, mode, standard deviation).

# In[6]:


## Code Task 2 here
##1
df_sales = pd.read_excel(f"{notebookutils.nbResPath}/builtin/OnlineSalesRetailer.xlsx", sheet_name= 'Sales')
df_sales['Sales'] = df_sales['Quantity'] * df_sales['UnitPrice']
display(df_sales)

##2
display(df_sales.isnull().sum())

##3
df_sales['Sales'] = df_sales['Sales'].fillna(0)
df_sales['UnitPrice'] = df_sales['UnitPrice'].fillna(0)

##4
mean_Quantity = df_sales['Quantity'].mean()  
median_Quantity = df_sales['Quantity'].median()  
mode_Quantity = df_sales['Quantity'].mode()[0]  
std_Quantity = df_sales['Quantity'].std()  

mean_UnitPrice = df_sales['UnitPrice'].mean()
median_UnitPrice = df_sales['UnitPrice'].median()
mode_UnitPrice = df_sales['UnitPrice'].mode()[0]
std_UnitPrice = df_sales['UnitPrice'].std()

print(f"Quantity - Mean : {mean_Quantity}, Median : {median_Quantity}, Mode: {mode_Quantity}, Std Dev: {std_Quantity}")

print(f"UnitPrice - Mean : {mean_UnitPrice}, Median : {median_UnitPrice}, Mode: {mode_UnitPrice}, Std Dev: {std_UnitPrice}")


# ### Task 3: Merging DataFrames
# #### Objective: Merge the Sales, Invoice, and Product tables based on common keys to perform a comprehensive analysis.
# 
# Instructions:
# 
# 1. Merge the Sales DataFrame with the Invoice DataFrame on InvoiceNo.
# 
# 2. Merge the result with the Product DataFrame on StockCode

# In[7]:


## Code Task 3 here
##1
df_merge = pd.merge(df_sales , df_invoice , on='InvoiceNo')
display(df_merge)

##2
df_merge = pd.merge(df_merge , df_product , on='StockCode')

display(df_merge)


# ## Task 4: Exploratory Data Analysis (EDA)
# ### Objective: Conduct EDA by analysing the data, identifying patterns, trends, and outliers.
# 
# Instructions:
# 
# Use describe() to calculate summary statistics for numeric columns.
# 
# Perform basic filtering, such as filtering out sales with Quantity equal to 0.
# 
# Check for outliers in the Sales column by using a scatter plot.

# In[10]:


## Code Task 4 here

df_sales_filtered = df_sales[df_sales['Quantity'] != 0]
display(df_sales_filtered)

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10, 5))

sns.scatterplot( x=df_merge.index, y=df_merge['Sales'])

plt.title('Scatter Plot to Identify Outliers in Sales')
plt.xlabel('Record Index')
plt.ylabel('Sales')
plt.show()


# ## Task 5: Data Visualisation – Scatter Plot, Histogram, and Line Chart
# ### Objective: Create scatter plots, histograms, and line charts to better understand the data.
# 
# Instructions:
# 
# Use a scatter plot to examine the relationship between Quantity and Sales.
# 
# Use a histogram to visualise the distribution of the Sales column.
# 
# Use a line chart to show the trend of Sales over time.
# 
# Write 1–2 sentences explaining the insights from each visualisation.

# In[8]:


## Code Task 5 here
## Use a scatter plot to examine the relationship between Quantity and Sales.
plt.scatter(df_merge['Quantity'], df_merge['Sales'])
plt.title('Relationship Between Quantity and Sales')
plt.xlabel('Quantity')
plt.ylabel('Sales')
plt.show()

##Use a histogram to visualise the distribution of the Sales column.

plt.figure(figsize=(8, 4))
sns.histplot(df_merge['Sales'], bins=5, color='purple', kde=True)
plt.title('Distribution of Sales')
plt.xlabel('Sales')
plt.ylabel('Frequency')
plt.show()

## Use a line chart to show the trend of Sales over time.

plt.figure(figsize=(8, 4))
sns.lineplot(df_merge, x='InvoiceDate', y='Sales', color='blue')
plt.title('trend of Sales over time')
plt.xlabel('InvoiceDate')
plt.ylabel('Sales in Millions')
plt.xticks(rotation=45)
plt.show()


## The scatter plot shows a positive relationship between Quantity and Sales. In general, orders with higher quantities generated higher sales. 
## However, a few unusually large orders, especially those with more than 500 units in February and March 2015, resulted in much higher sales than normal transactions.

## The histogram shows that the Sales data is heavily right-skewed. Most transactions between January and March 2015 had relatively low sales values, 
## while a small number of large orders generated much higher sales. These high-value transactions created a long tail on the right side of the distribution.

## The line chart shows that sales fluctuated between January and March 2015 rather than increasing steadily over time. 
## There were noticeable peaks in mid-January, late February, and early March. The largest increases occurred around 26–27 February and 5–6 March 2015, 
## mainly due to bulk purchases that generated unusually high sales.



# ## Task 6: Correlation and Data Insights
# ### Objective: Identify the relationship between different numerical columns in the dataset.
# 
# Instructions:
# 
# Calculate the correlation between Quantity and Sales.
# 
# Visualise the correlation matrix using a heatmap.
# 
# Write 1–2 sentences explaining the insights from the visualisation.

# In[9]:


## Code Task 6 here
## Calculate the correlation between Quantity and Sales.
correlation = df_merge[['Quantity', 'Sales']].corr()

# Display the correlation matrix
print(correlation)

# Create a heatmap for the correlation matrix
plt.figure(figsize=(6, 5))
sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Matrix between Profil and Sales')
plt.show()

## Write 1–2 sentences explaining the insights from the visualisation.

## The visualisation shows a very strong positive correlation like 0.98 between Quantity and Sales Quantity. 
## This indicates that as the quantity sold increases, the sales quantity also increases almost proportionally.


# Task 7: Grouping and Aggregating
# Objective: Perform grouping and aggregation operations to summarise the data.
# Instructions:
# 
# GroupBy operation: Group by Product_Category and calculate the total Sales per category.
# Create a Pivot Table to show Sales by Country and Product_Category.

# In[23]:


## Code Task 7 here

# Group by ProductCategory and calculate total Sales
sales_by_category = df_merge.groupby('Product_Category')['Sales'].sum().reset_index()
sales_by_category = sales_by_category.sort_values(by='Sales', ascending=False)
display(sales_by_category)

# Create a pivot table for Sales by StoreName and ProductCategory
pivot_table = df_merge.pivot_table(values='Sales', index='Country', columns='Product_Category', aggfunc='sum')
pivot_table = pivot_table.reset_index()
display(pivot_table)


# ## Submission Guidelines:
# Submit the Python notebook with all the tasks and visualisations.
# 
# Ensure that each task is clearly explained and that all steps are followed.
# 
# Include markdown explanations where necessary to explain your thought process.

# Good work

# In[ ]:




