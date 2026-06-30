import pandas as pd

#inspection

def clean_data(df):
    print("=" * 50)
    print("Module 2 & 3: DATA INSPECTION & CLEANING")
    print("=" * 50)

    print("\nMISING VALUES:")
    print(df.isnull().sum())

    print("\nDUPLICATE RECORDS:")
    print(df.duplicated().sum())

    print("\nDESCRIPTIVE STATISTICS:")
    print(df.describe())

    print("\nMEMORY USAGE;")
    print(df.memory_usage())

    print("\nSUMMARY INFO;")
    print(df.info())

    #cleaning

    df = df.drop_duplicates()
    print("\n Duplicates Removed!")

    mean_marks = df["Marks"].mean()
    df["Marks"] = df["Marks"].fillna(mean_marks)
    print(f" Missing Marks filled with mean: {mean_marks:.2f}")

    df = df[df["Attendance"] <= 100]
    df = df[df["Attendance"] >=0]
    print("Attendance validated (0-100)!")

    df = df[df["StudyHours"] >= 0]
    df = df[df["StudyHours"] <=24]
    print("Study Hours validated (0-24)!")

    df = df[df["Marks"] >=0]
    df = df[df["Marks"] <= 100]
    print("Marks validated (0-100)!")

    df.to_csv("output/cleaned_data.csv", index=False)
    print("Cleaned data saved to output/cleaned_data.csv!")
    return df
