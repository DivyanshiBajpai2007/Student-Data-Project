import pandas as pd
import matplotlib.pyplot as plt

def analyze_data(df):
    
    print("=" * 50)
    print("MODULE 5 & 6: DATA FILTERING & ANALYSIS")
    print("=" * 50)
    
    # ── FILTERING ───────────────────────────────
    
    toppers = df[df["Marks"] >= 80]
    toppers.to_csv("output/toppers.csv", index=False)
    print(f"\n Top performers: {len(toppers)} students")
    
    failed = df[df["Marks"] < 40]
    failed.to_csv("output/failed_students.csv", index=False)
    print(f"Failed students: {len(failed)} students")
    
    low_attendance = df[df["Attendance"] < 75]
    low_attendance.to_csv("output/low_attendance.csv", index=False)
    print(f"Low attendance: {len(low_attendance)} students")
    
    
    high_study = df[df["StudyHours"] > 8]
    high_study.to_csv("output/high_study_hours.csv", index=False)
    print(f"High study hours: {len(high_study)} students")
    
    # ANALYSIS 
    
    print("\n" + "=" * 50)
    print("  BASIC ANALYSIS")
    print("=" * 50)
    
    print(f"\nAverage Marks     : {df['Marks'].mean():.2f}")
    print(f"Highest Marks     : {df['Marks'].max():.2f}")
    print(f"Lowest Marks      : {df['Marks'].min():.2f}")
    print(f"Average Attendance: {df['Attendance'].mean():.2f}%")
    print(f"Average StudyHours: {df['StudyHours'].mean():.2f} hrs")
    
    total = len(df)
    passed = len(df[df["Result"] == "Pass"])
    failed_count = len(df[df["Result"] == "Fail"])
    print(f"\nPass Percentage   : {(passed/total*100):.2f}%")
    print(f"Fail Percentage   : {(failed_count/total*100):.2f}%")
    
    print("\nGRADE DISTRIBUTION:")
    print(df["Grade"].value_counts())
    
    # SORTING
    
    print("\n" + "=" * 50)
    print("  SORTING")
    print("=" * 50)
    
    print("\nTOP 5 BY MARKS:")
    print(df.sort_values("Marks", ascending=False)
          [["Name","Marks"]].head())
    
    print("\nTOP 5 BY ATTENDANCE:")
    print(df.sort_values("Attendance", ascending=False)
          [["Name","Attendance"]].head())
    
    print("\nTOP 5 BY STUDY HOURS:")
    print(df.sort_values("StudyHours", ascending=False)
          [["Name","StudyHours"]].head())
    
    #  GROUPING 
    
    print("\n" + "=" * 50)
    print("  GROUPING BY GRADE")
    print("=" * 50)
    
    print("\nAverage Marks by Grade:")
    print(df.groupby("Grade")["Marks"].mean().round(2))
    
    print("\nNumber of Students per Grade:")
    print(df.groupby("Grade")["Name"].count())
    
    print("\nAverage Attendance by Grade:")
    print(df.groupby("Grade")["Attendance"].mean().round(2))
    
    # STATISTICAL ANALYSIS
    
    print("\n" + "=" * 50)
    print("  STATISTICAL ANALYSIS")
    print("=" * 50)
    
    print(f"\nMean Marks    : {df['Marks'].mean():.2f}")
    print(f"Median Marks  : {df['Marks'].median():.2f}")
    print(f"Mode Marks    : {df['Marks'].mode()[0]:.2f}")
    print(f"Std Deviation : {df['Marks'].std():.2f}")
    print(f"Variance      : {df['Marks'].var():.2f}")
    
    print("\nCORRELATION MATRIX:")
    print(df[["Marks","Attendance","StudyHours"]].corr().round(2))

    print("\n" + "=" * 50)
    print("   TOP 10 STUDENTS BY PERFORMANCE SCORE")
    print("=" * 50)
    
    top10 = df.sort_values("PerformanceScore", ascending=False).head(10)
    print(top10[["Name", "Marks", "Attendance", "StudyHours", "PerformanceScore"]])
    
    top10.to_csv("output/top10_performers.csv", index=False)
    print("\nTop 10 performers saved to output/top10_performers.csv!")

   
    print("\n" + "=" * 50)
    print("  BONUS: GENERATING VISUALIZATIONS")
    print("=" * 50)
    
   #Chart 1
    grade_counts = df["Grade"].value_counts().sort_index()
    plt.figure(figsize=(8, 5))
    plt.bar(grade_counts.index, grade_counts.values, color="steelblue")
    plt.title("Grade Distribution")
    plt.xlabel("Grade")
    plt.ylabel("Number of Students")
    plt.savefig("output/chart_grade_distribution.png")
    plt.close()
    print("Saved chart_grade_distribution.png")
    
    # Chart 2 
    plt.figure(figsize=(8, 5))
    plt.hist(df["Marks"], bins=20, color="seagreen", edgecolor="black")
    plt.title("Distribution of Marks")
    plt.xlabel("Marks")
    plt.ylabel("Number of Students")
    plt.savefig("output/chart_marks_distribution.png")
    plt.close()
    print("Saved chart_marks_distribution.png")
    
    # Chart 3 
    plt.figure(figsize=(8, 5))
    plt.scatter(df["Attendance"], df["Marks"], alpha=0.4, color="darkorange")
    plt.title("Attendance vs Marks")
    plt.xlabel("Attendance (%)")
    plt.ylabel("Marks")
    plt.savefig("output/chart_attendance_vs_marks.png")
    plt.close()
    print(" Saved chart_attendance_vs_marks.png")
    return df


    
    