import pandas as pd

def transform_data(df):
    
    print("=" * 50)
    print("MODULE 4: DATA TRANSFORMATION")
    print("=" * 50)
    
    def assign_grade(marks):
        if marks >= 90:   return "A"
        elif marks >= 80: return "B"
        elif marks >= 70: return "C"
        elif marks >= 60: return "D"
        else:             return "F"
    
    df["Grade"] = df["Marks"].apply(assign_grade)
    print("\n✅ Grade column created!")
    
    df["Result"] = df["Marks"].apply(
        lambda marks: "Pass" if marks >= 40 else "Fail"
    )
    print("Result column created!")
    
    df["PerformanceScore"] = (
        (df["Marks"] * 0.6) +
        (df["Attendance"] * 0.3) +
        (df["StudyHours"] * 0.1)
    ).round(2)
    print("Performance Score column created!")
    
    print("\nSAMPLE WITH NEW COLUMNS:")
    print(df[["Name", "Marks", "Grade",
              "Result", "PerformanceScore"]].head())
    
    return df