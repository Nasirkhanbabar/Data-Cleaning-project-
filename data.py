import pandas as pd
import random
import numpy as np

np.random.seed(42)
rows = 8000

names = ["Ali Khan", "Sara Ahmed", "Imran Raza", "Ayesha Noor",
         "Usman Ali", "Hina Shah", "Bilal Khan", "Zainab Ali",
         "Faizan Ahmed", "Nida Malik", "Nasir Khan", "Nasir babar"]


departments = ["IT", "HR", "Finance", "Marketing", "Sales", "Operations"]
genders = ["Male", "Female"]

data = []

for i in range(1, rows + 1):
    # Age can be missing, numeric, or invalid string
    age = random.choice([random.randint(20, 60), None, "thirty"])
    
    # Salary can be missing, normal, or extremely high
    salary = random.choice([random.randint(30000, 150000), None, 500000, "invalid"])
    
    # Attendance percentage can be missing
    attendance = random.choice([random.randint(35, 99), None])
    
    # Joining dates in mixed formats or missing
    joining_date = random.choice([
        "2022-01-15",
        "15-02-2021",
        "2020/03/10",
        "2020-02-02",
        None
    ])
    
    # Some random misalignments: string attached to number
    if random.random() < 0.02:
        salary = str(salary) + "USD"
    
    data.append([
        i,
        random.choice(names),
        age,
        random.choice(genders),
        random.choice(departments),
        salary,
        attendance,
        joining_date
    ])

df = pd.DataFrame(data, columns=[
    "Employee_ID", "Name", "Age", "Gender", "Department",
    "Salary", "Attendance_Percent", "Joining_Date"
])

# Save to CSV
df.to_csv("employee_data_messy.csv", index=False)
print("Messy dataset with 800 rows created as 'employee_data_messy.csv'")

# it's print our dataset
print(df.head())

# Lit's change Age and Salary String
df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
df["Salary"] = pd.to_numeric(df["Salary"], errors="coerce")

# Find the missing values 
print(df.isna().sum())

# Now handel the missing values

df["Age"].fillna(df["Age"].mean(), inplace=True)
df["Salary"].fillna(df["Salary"].mean(), inplace=True)
df["Attendance_Percent"].fillna(df["Attendance_Percent"].mean(), inplace=True)
df["Joining_Date"].fillna("2020-01-19", inplace=True)

print(df)

# Lit's Joining_Date change into datatime format
df["Joining_Date"] = pd.to_datetime(df["Joining_Date"], errors="coerce")

print(df)

# Now find the averaged salary of every department.

Avg_salary_department = df.groupby("Department")["Salary"].mean()
print(Avg_salary_department)

# Now show this in chart or graphic 
import matplotlib.pyplot as plt
import seaborn as sns


# Chart
plt.figure(figsize=(8,8))
plt.pie(Avg_salary_department, labels=Avg_salary_department.index, autopct="%1.1f%%")
plt.title("Averaged Salary By Department")
plt.show()

# Sceond chart which is barplot

plt.figure(figsize=(8, 8))
sns.barplot(x=Avg_salary_department.index, y=Avg_salary_department, palette="viridis")
plt.title("Averaged Salary By Department")
plt.xlabel("Department Names")
plt.ylabel("Amount of Salary")
plt.show()

# Now find the Attendance percent by Department

Avg_attendance_department = df.groupby("Department")["Attendance_Percent"].mean()
print(Avg_attendance_department)

# lit's make a chart for this

plt.figure(figsize=(8, 8))
plt.pie(Avg_attendance_department, labels=Avg_attendance_department.index, autopct="%1.1f%%")
plt.title("Averaged Attendance by Department")
plt.show()

# Barplot 

plt.figure(figsize=(8, 8))
sns.barplot(x=Avg_attendance_department.index, y=Avg_attendance_department, palette="viridis")
plt.title("Averaged Attendance by Department")
plt.ylabel("Percent of Attendance by Department")
plt.xlabel("Department Names")
plt.show()


