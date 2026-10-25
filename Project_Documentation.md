# Project Documentation: Student Performance Analytics System

## 1. Project Title and Student Details
**Project Title:** Student Performance Analytics System  
**Student Name:** [Enter your full name]  
**Course:** Python with AI  
**Training Provider:** EWB Courses  
**GitHub Repository:** [Paste your repository URL after uploading]

## 2. Objective
The objective is to build a Python program that reads student marks and attendance from a CSV dataset, analyzes student and class performance, assigns grades, identifies pass/fail status, summarizes each subject, and lists the top performers.

## 3. Technologies Used
- Python 3
- NumPy for numerical calculations
- Pandas for CSV loading, DataFrames, and data analysis
- Git and GitHub for version control and project submission

## 4. Dataset Description
The included `students.csv` file contains 20 fictional sample records. Columns are Student_ID, Name, Department, Python, Mathematics, AI, and Attendance. Marks and attendance are represented on a 0–100 scale. Replace or adapt the sample data if your trainer requires a different dataset.

## 5. Implementation
1. The program loads `students.csv` using `pandas.read_csv()`.
2. It checks required columns, missing values, and valid numeric ranges.
3. NumPy converts the subject marks into a numeric array and calculates each student's total and mean.
4. Reusable functions calculate grades, pass/fail results, class summary statistics, subject-wise statistics, and top performers.
5. A loop processes student rows and checks whether every subject mark meets the pass threshold.
6. Pandas operations calculate subject averages, highest marks, lowest marks, and rank students by average.
7. The main program prints the dataset and the analysis in clearly labelled sections.

## 6. Key Features
- Reads and validates student records from CSV
- Calculates total and average marks
- Assigns grades using defined grade bands
- Identifies pass/fail status
- Displays highest, lowest, and overall class average
- Analyzes each subject's average, maximum, and minimum
- Lists the top five students by average
- Uses functions, loops, conditions, NumPy, and Pandas

## 7. Output / Screenshots
Run `python main.py` and take screenshots of:
- The student-wise results table
- The class summary
- Subject-wise performance
- Top five performers

Insert your own screenshots here after running the project.

## 8. Final Outcome
The program produces a readable analysis of the included student dataset, including individual results, class-level statistics, subject comparisons, and top performers. The reported values are calculated from the CSV when the program runs.

## 9. Challenges and Learning
Edit this section to describe your real experience after testing the project. Possible topics to reflect on:
- Reading structured data from a CSV file
- Choosing NumPy and Pandas operations for calculations
- Defining and testing grade and pass/fail conditions
- Organizing reusable code into functions
- Running a project and correcting errors
- Uploading project files to GitHub

Only include challenges you actually faced and learning you can explain.

## 10. GitHub Repository
**Repository URL:** [Paste your public GitHub repository URL here]

## Rules and assumptions
- Each subject is marked out of 100.
- A student passes only when they score at least 35 in every subject.
- Grades use the average: A = 90–100, B = 80–<90, C = 70–<80, D = 60–<70, E = 50–<60, F = below 50.
- These are example rules selected for this project and are not official college grading rules.
- The dataset is fictional and used for demonstration.
