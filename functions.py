"""Reusable calculations for the Student Performance Analytics System."""

import numpy as np
import pandas as pd

SUBJECT_COLUMNS = ["Python", "Mathematics", "AI"]
PASS_MARK = 35


def assign_grade(average):
    """Return a grade using the grading bands documented in README.md."""
    if average >= 90:
        return "A"
    if average >= 80:
        return "B"
    if average >= 70:
        return "C"
    if average >= 60:
        return "D"
    if average >= 50:
        return "E"
    return "F"


def load_student_data(csv_path):
    """Load and validate the student CSV dataset."""
    data = pd.read_csv(csv_path)
    required = ["Student_ID", "Name", "Department", *SUBJECT_COLUMNS, "Attendance"]
    missing = [column for column in required if column not in data.columns]
    if missing:
        raise ValueError(f"Missing required column(s): {', '.join(missing)}")
    if data.empty:
        raise ValueError("The student dataset is empty.")
    if data[required].isnull().any().any():
        raise ValueError("The dataset contains blank values in required columns.")

    for subject in SUBJECT_COLUMNS:
        data[subject] = pd.to_numeric(data[subject], errors="raise")
        if not data[subject].between(0, 100).all():
            raise ValueError(f"Marks in {subject} must be between 0 and 100.")

    data["Attendance"] = pd.to_numeric(data["Attendance"], errors="raise")
    if not data["Attendance"].between(0, 100).all():
        raise ValueError("Attendance must be between 0 and 100.")
    return data


def calculate_student_results(data):
    """Return a copy with total, average, grade, and pass/fail status."""
    results = data.copy()
    marks = results[SUBJECT_COLUMNS].to_numpy(dtype=float)
    results["Total_Marks"] = np.sum(marks, axis=1)
    results["Average_Marks"] = np.round(np.mean(marks, axis=1), 2)

    grades = []
    statuses = []
    for _, student in results.iterrows():
        grades.append(assign_grade(student["Average_Marks"]))
        passed = all(student[subject] >= PASS_MARK for subject in SUBJECT_COLUMNS)
        statuses.append("Pass" if passed else "Fail")

    results["Grade"] = grades
    results["Result"] = statuses
    return results


def get_class_summary(results):
    """Calculate overall class-level statistics."""
    return {
        "student_count": int(len(results)),
        "class_average": round(float(results["Average_Marks"].mean()), 2),
        "highest_average": round(float(results["Average_Marks"].max()), 2),
        "lowest_average": round(float(results["Average_Marks"].min()), 2),
        "pass_count": int((results["Result"] == "Pass").sum()),
        "fail_count": int((results["Result"] == "Fail").sum()),
    }


def get_subject_summary(data):
    """Return mean, maximum, and minimum marks for each subject."""
    summary = data[SUBJECT_COLUMNS].agg(["mean", "max", "min"]).T
    summary.columns = ["Average", "Highest", "Lowest"]
    return summary.round(2)


def get_top_performers(results, count=5):
    """Return up to `count` students ranked by average marks."""
    return results.sort_values(
        by=["Average_Marks", "Name"], ascending=[False, True]
    ).head(count)
