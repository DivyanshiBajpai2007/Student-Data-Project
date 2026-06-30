import pandas as pd

def generate_report(df):
    
    print("=" * 50)
    print("MODULE 10: REPORT GENERATION")
    print("=" * 50)
    
    
    
    total = len(df)
    passed = len(df[df["Result"] == "Pass"])
    failed = len(df[df["Result"] == "Fail"])
    
    report = {
        "Total Students":    [total],
        "Passed Students":   [passed],
        "Failed Students":   [failed],
        "Highest Marks":     [df["Marks"].max()],
        "Lowest Marks":      [df["Marks"].min()],
        "Average Marks":     [df["Marks"].mean().round(2)],
        "Average Attendance":[df["Attendance"].mean().round(2)],
        "Average StudyHours":[df["StudyHours"].mean().round(2)],
    }
    
    report_df = pd.DataFrame(report)
      
    
    grade_dist = df.groupby("Grade")["Name"].count()
    grade_df   = grade_dist.reset_index()
    grade_df.columns = ["Grade", "Number of Students"]
    
    
    
    print("\nFINAL REPORT SUMMARY:")
    print(f"  Total Students   : {total}")
    print(f"  Passed Students  : {passed}")
    print(f"  Failed Students  : {failed}")
    print(f"  Highest Marks    : {df['Marks'].max():.2f}")
    print(f"  Lowest Marks     : {df['Marks'].min():.2f}")
    print(f"  Average Marks    : {df['Marks'].mean():.2f}")
    print(f"  Average Attendance: {df['Attendance'].mean():.2f}%")
    print(f"  Average StudyHours: {df['StudyHours'].mean():.2f} hrs")
    
    print("\n GRADE WISE DISTRIBUTION:")
    print(grade_df)
    
    #SAVE REPORT 
    
    report_df.to_csv("output/report.csv", index=False)
    grade_df.to_csv("output/grade_distribution.csv", index=False)
    print("\n Report saved to output/report.csv!")
    print(" Grade distribution saved!")
    
    return report_df