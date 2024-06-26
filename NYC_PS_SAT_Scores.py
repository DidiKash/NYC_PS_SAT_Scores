import pandas as pd

# Read in the data
schools = pd.read_csv("/Users/thenkashamas/Downloads/NYC_Public_School_SAT_Scores/schools.csv")

# Preview the data
print(schools)

df1 = schools[["school_name", "average_math"]]
print(df1.isna().any())        # Checking for missing values

best_math_result_min = 800 * 8 / 10
print("The best math results are at least " + str(best_math_result_min))
df2 = df1[df1["average_math"] >= best_math_result_min]      # Subsetting rows
df3 = df2.sort_values(by="average_math", ascending=False)   # Sorting the new DataFrame
best_math_schools = df3
print("The NYC schools that have the best math results are : ")
print(best_math_schools)

# adding the column "total_SAT"
schools["total_SAT"] = schools["average_math"] + schools["average_reading"] + schools["average_writing"]
# print(schools.head())
# Subsetting the schools DataFrame
schools0 = schools[["school_name", "total_SAT"]]
schools1 = schools0.sort_values("total_SAT", ascending=False)
top_10_schools = schools1.sort_values(by="total_SAT", ascending=False)[:10]
print(top_10_schools)

# Code for the borough with the largest standard deviation
schools2 = schools.groupby("borough")["total_SAT"].agg(["count", "mean", "std"]).round(2)
# print(schools2)
max_val_std = schools2["std"].max()
schools3 = schools2[schools2["std"] == max_val_std]
largest_std_dev = schools3
# print(largest_std_dev)
largest_std_dev = largest_std_dev.rename(columns={"count": "num_schools", "mean": "average_SAT", "std": "std_SAT"})
print(largest_std_dev)
print("The borough that has the largest standard deviation is Manhattan.")
