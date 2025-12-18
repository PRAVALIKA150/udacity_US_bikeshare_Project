## Project: Bikeshare Data Exploration By Pravalika N S

### 1. Project Overview
This project loads and analyzes bikeshare trip data for three major US cities (Chicago, New York City, and Washington). It computes and displays descriptive statistics on the trip durations, popular travel times, common stations and routes, and user demographics.

### 2. File and Data
* **bikeshare.py**: The main Python script containing functions to load data, filter it, calculate statistics, and display output to the user.
* **chicago.csv, new_york_city.csv, washington.csv**: The raw data files provided for analysis.

### 3. External Resources and Documentation
The core structure and data analysis tasks were provided by the Udacity Data Analyst Nanodegree program.

**To ensure the highest quality, readability, and user experience, the following external resources and documentation were referenced for implementation details outside the core curriculum:**

* **Pandas Documentation (pandas.pydata.org):** Referenced for detailed syntax on methods like `.mode()`, `.value_counts()`, `.dt.day_name()`, `.nlargest()`, and handling data types (e.g., converting floats to integers when necessary).
* **Python Documentation (docs.python.org):** Referenced for using the `time` module (for tracking execution speed) and formatting f-strings.
* **Custom UI/UX Implementation:** The interactive prompts (e.g., 'New York City' city input, integer vs. abbreviation day input) and the custom output formatting (e.g., line breaks, specific statistic labels, and the vertical raw data display) were implemented based on iterative user testing and specific formatting requirements developed for an enhanced user experience.

---

### 4. How to Run the Script
1.  Ensure Python 3 is installed.
2.  Ensure you have the pandas library installed (`pip install pandas`).
3.  Place `bikeshare.py` and the three CSV data files in the same directory.
4.  Run the script from your terminal: `python bikeshare.py` (or `ipython solution.py` if you renamed it).