import pandas as pd
import numpy as np
import random

np.random.seed(42)

rows = 12000

names = ["Ali Khan","Sara Ahmed","Imran Raza","Ayesha Noor","Usman Ali",
         "Hina Shah","Bilal Khan","Zainab Ali","Faizan Ahmed","Nida Malik",
         "Nasir Khan","Sana Iqbal"]

departments = ["IT","HR","Finance","Sales","Marketing","Operations","Support"]
job_roles = ["Analyst","Engineer","Manager","Executive","Officer","Assistant"]
cities = ["Karachi","Lahore","Islamabad","Peshawar","Quetta","Multan"]
countries = ["Pakistan"]
education = ["Matric","Intermediate","Bachelor","Master","PhD"]
work_mode = ["Onsite","Remote","Hybrid"]
gender = ["Male","Female"]
marital = ["Single","Married"]

df = pd.DataFrame({
    "Employee_ID": np.arange(1, rows + 1),
    "Name": np.random.choice(names, rows),
    "Gender": np.random.choice(gender, rows),
    "Age": np.random.randint(18, 65, rows),
    "Marital_Status": np.random.choice(marital, rows),
    "Education": np.random.choice(education, rows),

    "Department": np.random.choice(departments, rows),
    "Job_Role": np.random.choice(job_roles, rows),
    "Experience_Years": np.random.randint(0, 40, rows),
    "Joining_Year": np.random.randint(2000, 2024, rows),
    "Promotion_Count": np.random.randint(0, 6, rows),

    "Salary": np.random.randint(20000, 300000, rows),
    "Bonus": np.random.randint(0, 50000, rows),
    "Allowance": np.random.randint(0, 30000, rows),
    "Tax": np.random.randint(0, 40000, rows),
    "Net_Salary": np.nan,

    "Attendance_Percent": np.random.randint(40, 101, rows),
    "Absents": np.random.randint(0, 30, rows),
    "Late_Days": np.random.randint(0, 20, rows),
    "Performance_Score": np.round(np.random.uniform(1, 5, rows), 1),
    "Overtime_Hours": np.random.randint(0, 80, rows),

    "Skill_Level": np.random.choice(["Beginner","Intermediate","Advanced"], rows),
    "Training_Hours": np.random.randint(0, 200, rows),
    "Manager_Rating": np.round(np.random.uniform(1, 5, rows), 1),

    "City": np.random.choice(cities, rows),
    "Country": np.random.choice(countries, rows),
    "Work_Mode": np.random.choice(work_mode, rows),
    "Project_Count": np.random.randint(0, 15, rows),
    "Satisfaction_Score": np.round(np.random.uniform(1, 10, rows), 1),
    "Attrition": np.random.choice(["Yes","No"], rows)
})

# Calculate Net Salary (with errors intentionally)
df["Net_Salary"] = df["Salary"] + df["Bonus"] + df["Allowance"] - df["Tax"]

# 🔴 Introduce MASSIVE data issues (for cleaning)
for col in df.columns:
    df.loc[df.sample(frac=0.08).index, col] = np.nan

# Wrong ages
df.loc[df.sample(50).index, "Age"] = [-5, 120] * 25

# Duplicate rows
df = pd.concat([df, df.sample(200)], ignore_index=True)

# Save
df.to_csv("big_company_dirty_dataset.csv", index=False)

print("Dataset shape:", df.shape)
print(df.head())

# Find the missing values
print(df.isna().sum())

# convert str into the number
df["Age"] = pd.to_numeric(df["Age"], errors="coerce")

# handle the missing values
df["Name"].fillna(df["Name"].mode()[0], inplace=True)
df["Gender"].fillna(df["Gender"].mode()[0], inplace=True)
df["Employee_ID"].fillna(df["Employee_ID"].mean(), inplace=True)

df["Allowance"].fillna(df["Allowance"].mean(), inplace=True)
df["Bonus"].fillna(df["Bonus"].mean(), inplace=True)
df["Net_Salary"].fillna(df["Net_Salary"].mean(), inplace=True)
df["Tax"].fillna(df["Tax"].median(), inplace=True)
df["Salary"].fillna(df["Salary"].min(), inplace=True)
df["Age"].fillna(df["Age"].median(), inplace=True)
df["Marital_Status"].fillna(df["Marital_Status"].mode()[0], inplace=True)
df["Education"].fillna(df["Education"].mode()[0], inplace=True)
df["Department"].fillna(df["Department"].mode()[0], inplace=True)
df["Job_Role"].fillna(df["Job_Role"].mode()[0], inplace=True)
df["Experience_Years"].fillna(df["Experience_Years"].min(), inplace=True)
df["Joining_Year"].fillna(2020, inplace=True)
df["Promotion_Count"].fillna(df["Promotion_Count"].median(), inplace=True)
df["Attendance_Percent"].fillna(df["Attendance_Percent"].mean(), inplace=True)
df["Absents"].fillna(df["Absents"].min(),inplace=True)
df["Late_Days"].fillna(df["Late_Days"].max(), inplace=True)
df["Manager_Rating"].fillna(df["Manager_Rating"].mean(), inplace=True)
df["Training_Hours"].fillna(df["Training_Hours"].mean(), inplace=True)
df["Performance_Score"].fillna(df["Performance_Score"].min(), inplace=True)
df["City"].fillna(df["City"].mode()[0], inplace=True)
df["Country"].fillna(df["Country"].mode()[0], inplace=True)
df["Work_Mode"].fillna(df["Work_Mode"].mode()[0], inplace=True)
df["Project_Count"].fillna(df["Project_Count"].median(), inplace=True)
df["Satisfaction_Score"].fillna(df["Satisfaction_Score"].median(), inplace=True)
df["Overtime_Hours"].fillna(df["Overtime_Hours"].mean(), inplace=True)
df["Attrition"].fillna(df["Attrition"].mode()[0], inplace=True)
df["Skill_Level"].fillna(df["Skill_Level"].mode()[0], inplace=True)



print(df.isna().sum())

# Remove the duplicates 
df.drop_duplicates(inplace=True)

df["Salary"].sort_values()
print(df["Salary"].head(20))

Total_Salary = df["Salary"] + df["Bonus"] + df["Allowance"] - df["Tax"]
df["Net_Salary"] = Total_Salary
print(df["Net_Salary"].head())

# Handle outliers

def salary_level(salary):
    if salary > 250000:
        return "High Salary"
    elif salary > 150000:
        return "Medium Salary"
    else:
        return "Low Salary"
df["Salary_Level"] = df["Salary"].apply(salary_level)

def level(job):
    if job > 25:
        return "Senior"
    elif job > 10:
        return "Mid_level"
    else:
        return "Junior"
df["Job_level"] = df["Experience_Years"].apply(level)


import matplotlib.pyplot as plt
import seaborn as sns

avg_year_salary = df.groupby("Experience_Years")["Net_Salary"].mean()
plt.figure(figsize=(8, 8))
sns.scatterplot(x=avg_year_salary, y=avg_year_salary.index)
plt.show()


# ✔ Handle missing values
# ✔ Fix wrong ages
# ✔ Remove duplicates
# ✔ Fix salary calculations
# ✔ Handle outliers
# ✔ Encode categorical data
# ✔ Validate ranges
# ✔ Feature engineering
# ✔ EDA & visualization