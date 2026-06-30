# Student Performance Data Handling and Analysis System

A complete data pipeline built using Python and Pandas to load, clean, transform, analyze, and report on student performance data.

## Project Structure

    Student_Data_Project/
    data/
        student_dataset_v2.csv
    output/
        cleaned_data.csv
        toppers.csv
        failed_students.csv
        low_attendance.csv
        high_study_hours.csv
        grade_distribution.csv
        report.csv
    src/
        load_data.py
        clean_data.py
        transform.py
        analyze.py
        report.py
    main.py
    requirements.txt
    README.md

## Modules

load_data.py - Loads the CSV file, displays first/last rows, shape, columns, and data types.

clean_data.py - Checks missing values and duplicates, fills missing Marks with mean, validates Attendance/StudyHours/Marks ranges, saves cleaned dataset.

transform.py - Creates Grade, Result, and PerformanceScore columns using custom logic and formulas.

analyze.py - Filters toppers/failed/low-attendance/high-study-hours students, computes statistics, sorts and groups data by grade.

report.py - Generates a final summary report with totals, averages, and grade distribution.

## How to Run

    pip install -r requirements.txt
    python main.py

## Technologies Used

- Python 3.14
- Pandas

## Author

Divyanshi Bajpai