# Student Performance Analytics System

## Project Overview
The **Student Performance Analytics System** is a Python-based data analysis project that processes student marks and attendance and produces student-wise and class-level performance summaries. It uses Pandas to organize the dataset and NumPy for numerical calculations.

## Objectives
- Calculate each student's total and average marks.
- Assign grades using the grading rules defined in the program.
- Determine pass/fail status.
- Summarize overall class performance.
- Compare subject-wise average marks.
- Identify the top five performers.

## Technologies Used
- **Python 3** — program logic and calculations.
- **Pandas** — loading and analyzing the CSV dataset.
- **NumPy** — numerical calculations.
- **CSV** — storing student records.

## Dataset Description
The `students.csv` file contains 20 fictional sample student records. It includes student ID, name, department, marks in Python, Mathematics and AI, and attendance percentage. The data is for demonstration and does not represent real students.

## Key Features
1. Loads student records from a CSV file.
2. Calculates total and average marks for each student.
3. Assigns grades based on average marks.
4. Identifies pass/fail status.
5. Calculates class statistics and subject-wise averages.
6. Lists the top five performers.

## Calculation Rules
- Each subject is treated as being marked out of 100.
- A student passes if they score at least 35 in every subject.
- Grade by average: A = 90–100; B = 80–below 90; C = 70–below 80; D = 60–below 70; E = 50–below 60; F = below 50.

These are sample rules for this project, not official college grading rules.

## How the Project Works
1. The program loads student records from `students.csv` into a Pandas DataFrame.
2. It calculates student totals and averages.
3. It applies the defined grading and pass/fail rules.
4. It summarizes class performance and compares subject averages.
5. It ranks students by average marks and displays the top five performers.
6. It prints the results in the terminal.

## Project Structure
```text
student-performance-analytics/
├── main.py
├── functions.py
├── students.csv
├── requirements.txt
├── README.md
└── Project_Documentation.md
```

## How to Run
### Prerequisites
- Python 3 installed on your computer.
- Project files saved in the same folder.

### Install dependencies
Open a terminal in the project folder and run:
```bash
python -m pip install -r requirements.txt
```

### Run the program
```bash
python main.py
```

On some Windows systems, use `py` instead of `python` if needed.

## Expected Output
When the program runs, it displays student records and calculated results, class statistics, subject-wise averages, pass/fail counts, and the top five performers. Exact values are calculated from the included CSV dataset.

## Project Outcome
The project demonstrates how Python, NumPy, and Pandas can be used to process student records and generate academic performance summaries. It brings together CSV data handling, numerical calculations, conditional logic, and basic data analysis.

## Learning Outcomes
This project provides practice with Python functions, loops and conditions; reading CSV files; working with Pandas DataFrames; using NumPy for calculations; and interpreting data analysis results.

## Conclusion
The Student Performance Analytics System provides a practical example of analyzing sample student data with Python libraries and presenting the results in a clear, structured form.
