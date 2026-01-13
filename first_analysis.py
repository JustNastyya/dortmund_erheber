import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from utils import numeric_vars, learning_materials_group, materials_that_i_use, allgemein, demog
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


df_raw = pd.read_csv("results_survey_bear.csv")

df_raw = df_raw.drop(columns="Unnamed: 0")
df_raw.columns

# nan values

df = df_raw[df_raw.isna().sum(axis=1) < 30]

len(df.columns)

# fuck metadata

df = df.drop(columns=["answer_id", "date_sent", "last_page", "start_lang", "random_value"])

# descr methods

desc = df[numeric_vars].describe().T
desc[['mean', 'std', 'min', '25%', '50%', '75%', 'max']]

# idea: for a groupof questions e.g. with the lerning materials visualize as a bunch of boxplots

# boxplots

# now lets do some demogr analysis

# by that are ment variables:
demog = [
    "faculty",
    "faculty_other",
    "edu_level",
    "semester_n"
]

df["faculty"]
df["faculty_other"]

df["edu_level"]

df["semester_n"]


# ##################### demographics


import matplotlib.pyplot as plt

faculty_combined = df["faculty"].copy()
mask = faculty_combined == "Sonstiges"
faculty_combined[mask] = df.loc[mask, "faculty_other"]

faculty_counts = faculty_combined.value_counts()

plt.figure(figsize=(10, 6))

plt.bar(faculty_counts.index, faculty_counts.values)
plt.title("Faculty Distribution")
plt.ylabel("Count")
plt.xticks(rotation=45, ha="right")

plt.tight_layout()
plt.savefig("faculty_distribution.pdf")
plt.close()

edu_counts = df["edu_level"].value_counts().sort_index()
semester_data = df["semester_n"].dropna()


fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# --- Education level (bar plot)
axes[0].bar(edu_counts.index, edu_counts.values)
axes[0].set_title("Education Level")
axes[0].set_ylabel("Count")
axes[0].set_xlabel("Level")

# --- Semester number (histogram)
axes[1].hist(
    semester_data,
    bins=range(1, int(semester_data.max()) + 2),
    edgecolor="black"
)
axes[1].set_title("Semester Number")
axes[1].set_xlabel("Semester")
axes[1].set_ylabel("Count")

plt.tight_layout()
plt.savefig("education_and_semester.pdf")
plt.close()
