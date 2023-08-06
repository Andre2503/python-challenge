# Python Challenge: PyBank and PyPoll Analysis

In this assignment, I was asked to tackled two real-world scenarios using Python scripting: PyBank and PyPoll analysis.

## Project Structure

The project is organized into two folders, `PyBank` and `PyPoll`, each containing the following files:

1. `main.py`: The main Python script that performs the financial analysis for PyBank or the vote-counting analysis for PyPoll.

2. `Resources`: A folder containing the input CSV files needed for the analysis.

3. `Analysis`: A folder containing the output text files that store the analysis results.

## PyBank Analysis

In the `PyBank` folder, we've created a Python script `main.py` that analyzes financial records from the dataset `budget_data.csv`. The script calculates the following values:

- Total number of months included in the dataset
- Net total amount of "Profit/Losses" over the entire period
- Changes in "Profit/Losses" over the entire period, and the average of those changes
- Greatest increase in profits (date and amount) over the entire period
- Greatest decrease in profits (date and amount) over the entire period

The results of the analysis are displayed in the terminal and exported to the `Analysis` folder in the file `financial_analysis.txt`.

## PyPoll Analysis

In the `PyPoll` folder, you'll find the Python script `main.py` that analyzes poll data from the dataset `election_data.csv`. The script calculates the following values:

- Total number of votes cast
- Complete list of candidates who received votes
- Percentage of votes each candidate won
- Total number of votes each candidate won
- Winner of the election based on popular vote

The analysis results are printed to the terminal and exported to the `Analysis` folder in the file `election_results.txt`.

## How to Run

To run the analysis for PyBank or PyPoll, follow these steps:

1. Clone this repository to your local machine.
2. Navigate to the respective `PyBank` or `PyPoll` folder.
3. Run the `main.py` script using a Python interpreter.
4. The analysis results will be displayed in the terminal, and a text file will be generated in the `Analysis` folder.

## Summary

This Python Challenge project demonstrates how Python scripting can be used to analyze data efficiently. The scripts provided in the `PyBank` and `PyPoll` folders perform the required analyses and generate required results.

For any questions or further assistance, feel free to reach out.
