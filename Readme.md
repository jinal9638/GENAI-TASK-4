# Python File I/O Operations: Sales Data Analysis

This project demonstrates how to perform fundamental file handling operations in Python using a practical example of managing sales data records (sales_data.txt).

# Table of Contents

Overview

Tasks & Implementation

Task 1: Write Sales Records to a File

Task 2: Read File in Different Ways

Task 3: Append New Sales Data

How to Run

# Tasks & Implementation

# Task 1: Write Sales Records to a File

Define Initial Sales Data: Create a list of sales amounts: sales = [1200, 450, 980, 1500, 3000].

Write Data (Line by Line): Open sales_data.txt in write mode (w+) and write each integer value on a new line.

Reopen and Verify: Read the file back in standard read mode (r) to display the written items.

Extra (Optional): Format the sales data into a single comma-separated string (",".join(...)) and write it to the file.

# Task 2: Read File in Different Ways

Using sales_data.txt:

Read Entire File: Use .read() to retrieve and print all content.

Read First Line: Use .readline() to display only the first entry.

Read All Lines & Convert Types: Use .readlines() and iterative looping with .strip() to clean newline characters (\n) and convert string elements back into an integer list ([1200, 450, 980, 1500, 3000]).

# Task 3: Append New Sales Data

Append Entries: Open sales_data.txt in append mode (a) and add new sales entries: 5000, 2500, and 1700.

Display Updated File: Reopen in read mode (r) and output the updated content.

Extra (Optional): Calculate and print the total count of lines present in the file after appending.

# How to Run

1.Make sure Python 3.10+ is installed on your system.
2.Download the project ZIP file.
3.Extract this downloaded ZIP file to a folder on your computer.
4.Open the extracted folder with Visual studio code. 
5.Press F5 (or click the Run/Play button) in VS Code to run the file.


Note : A file named sales_data.txt will be automatically generated and updated in the same folder.

# GitHub Link

Github repo link :

[https://github.com/jinal9638/GENAI-TASK-4.git]