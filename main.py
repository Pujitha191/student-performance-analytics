"""Run the Student Performance Analytics System."""

from pathlib import Path

from functions import (
    calculate_student_results,
    get_class_summary,
    get_subject_summary,
    get_top_performers,
    load_student_data,
)

DATA_FILE = Path(__file__).with_name("students.csv")


def main():
    try:
        data = load_student_data(DATA_FILE)
    except (OSError, ValueError, KeyError) as error:
        print(f"Could not load student data: {error}")
        return

    results = calculate_student_results(data)
    summary = get_class_summary(results)
    subject_summary = get_subject_summary(data)
    top_students = get_top_performers(results)

    print("=" * 72)
    print("STUDENT PERFORMANCE ANALYTICS SYSTEM")
    print("=" * 72)

    print("\n1. STUDENT DATASET")
    print(data.to_string(index=False))

    print("\n2. STUDENT-WISE RESULTS")
    columns = [
        "Student_ID", "Name", "Total_Marks", "Average_Marks",
        "Grade", "Result", "Attendance"
    ]
    print(results[columns].to_string(index=False))

    print("\n3. CLASS SUMMARY")
    print(f"Number of students : {summary['student_count']}")
    print(f"Class average      : {summary['class_average']}")
    print(f"Highest average    : {summary['highest_average']}")
    print(f"Lowest average     : {summary['lowest_average']}")
    print(f"Students passed    : {summary['pass_count']}")
    print(f"Students failed    : {summary['fail_count']}")

    print("\n4. SUBJECT-WISE PERFORMANCE")
    print(subject_summary.to_string())

    best_subject = subject_summary["Average"].idxmax()
    print(f"Best-performing subject by average: {best_subject}")

    print("\n5. TOP FIVE PERFORMERS")
    print(
        top_students[["Student_ID", "Name", "Average_Marks", "Grade"]]
        .to_string(index=False)
    )

    print("\nAnalysis completed successfully.")


if __name__ == "__main__":
    main()
