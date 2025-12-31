import pandas as pd
import numpy as np
import random

np.random.seed(42)

rows = 8000

names = [
    "Ali Khan", "Sara Ahmed", "Imran Raza", "Ayesha Noor",
    "Usman Ali", "Hina Shah", "Bilal Khan", "Zainab Ali",
    "Faizan Ahmed", "Nida Malik", "Nasir Khan", "Sana Iqbal"
]

departments = ["IT", "HR", "Finance", "Sales", "Marketing", "Operations"]
genders = ["Male", "Female"]
cities = ["Karachi", "Lahore", "Islamabad", "Peshawar", "Quetta", "Multan"]

data = {
    "Employee_ID": np.arange(1, rows + 1),
    "Name": np.random.choice(names, rows),
    "Department": np.random.choice(departments, rows),
    "Gender": np.random.choice(genders, rows),
    "Age": np.random.randint(20, 60, rows),
    "Experience_Years": np.random.randint(0, 35, rows),
    "Salary": np.random.randint(25000, 250000, rows),
    "Performance_Score": np.round(np.random.uniform(1, 5, rows), 1),
    "Attendance_Percent": np.random.randint(60, 100, rows),
    "City": np.random.choice(cities, rows)
}

df = pd.DataFrame(data)

# 🔹 Introduce missing (blank) values randomly
for col in ["Department", "Age", "Salary", "Performance_Score", "Attendance_Percent"]:
    df.loc[df.sample(frac=0.05).index, col] = np.nan

# Save to CSV
df.to_csv("company_employee_data.csv", index=False)

print(df.head())
print("\nMissing values:\n")
print(df.isna().sum())
print(df["Age"])
# Convert  str into number
df["Age"] = pd.to_numeric(df["Age"], errors="coerce")

# Handle the missing values
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Department"] = df["Department"].fillna(df["Department"].mode()[0])
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())
df["Attendance_Percent"] = df["Attendance_Percent"].fillna(df["Attendance_Percent"].mean())
df["Performance_Score"] = df["Performance_Score"].fillna(df["Performance_Score"].median())


# Make the outliers for salary
def salary_level(salary):
    if salary > 200000:
        return "High Salary"
    elif salary > 100000:
        return "Medium Salary"
    else:
        return "Low Salary"
    
df["Salary_level"] = df["Salary"].apply(salary_level)

print(df.head())
        
# Compare salary by department

Avg_salary_department = df.groupby("Department")["Salary"].mean()
print(Avg_salary_department)


import matplotlib.pyplot as plt 
import seaborn as sns

# Using the graph


plt.figure(figsize=(10,6))
sns.barplot(x=Avg_salary_department.index, y=Avg_salary_department.values)
plt.title("Average Salary by Department")
plt.xticks(rotation=45)
plt.show()
# Attendance vs performance graph


plt.figure(figsize=(8,8))
sns.scatterplot(x="Attendance_Percent", y="Performance_Score", data=df, palette="viridis")
plt.title("Attendance and performance")
plt.show()




# ✔ Find missing values
# ✔ Fill blanks (mean, median, mode)
# ✔ Remove outliers from Salary
# ✔ Compare salary by department
# ✔ Attendance vs performance graph