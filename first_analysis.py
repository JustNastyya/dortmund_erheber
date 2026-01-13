import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from utils import numeric_vars, learning_materials_group, materials_that_i_use, allgemein, demog, faculty_generation, umnennen_materials
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


df_raw = pd.read_csv("results_survey_bear.csv")
# df_raw = pd.read_csv("results-survey_cleaned.csv")

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

df = faculty_generation(df)
faculty_counts = df["faculty_clean"].value_counts()

plt.figure(figsize=(10, 6))

plt.bar(faculty_counts.index, faculty_counts.values)
plt.title("Verteilung der Fakultäten")
plt.ylabel("Anzahl")
plt.xticks(rotation=45, ha="right")

plt.tight_layout()
plt.savefig("faculty_distribution.pdf")
plt.close()

edu_counts = df["edu_level"].value_counts().sort_index()
semester_data = df["semester_n"].dropna()


fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# --- Education level (bar plot)
# --- Education level (bar plot)
# --- Bildungsabschluss (Balkendiagramm)
axes[0].bar(
    edu_counts.index,
    edu_counts.values,
    edgecolor="black",
    linewidth=0.8
)

axes[0].set_title("Bildungsabschluss", fontsize=12, pad=10)
axes[0].set_xlabel("Abschluss", fontsize=10)
axes[0].set_ylabel("Anzahl", fontsize=10)

axes[0].tick_params(axis="x")
axes[0].grid(axis="y", linestyle="--", alpha=0.6)
axes[0].set_axisbelow(True)


# --- Semesterzahl (Histogramm)
bins = range(1, int(semester_data.max()) + 2)

axes[1].hist(
    semester_data,
    bins=bins,
    edgecolor="black",
    linewidth=0.8
)

axes[1].set_title("Anzahl der Semester", fontsize=12, pad=10)
axes[1].set_xlabel("Semester", fontsize=10)
axes[1].set_ylabel("Anzahl", fontsize=10)

axes[1].grid(axis="y", linestyle="--", alpha=0.6)
axes[1].set_axisbelow(True)


plt.tight_layout()
plt.savefig("bildungsabschluss_und_semester.pdf", dpi=300)
plt.close()
