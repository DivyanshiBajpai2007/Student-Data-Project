import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))


from load_data import load_data
from clean_data import clean_data
from transform import transform_data
from analyze import analyze_data
from report import generate_report

print("=" * 50)
print("  STUDENT PERFORMANCE ANALYSIS SYSTEM")
print("=" * 50)




df = load_data()


df = clean_data(df)


df = transform_data(df)


df = analyze_data(df)


generate_report(df)

print("\n" + "=" * 50)
print("✅ PROJECT COMPLETE!")
print("=" * 50)