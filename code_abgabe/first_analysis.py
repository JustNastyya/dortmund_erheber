import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from utils import numeric_vars, faculty_generation


df_raw = pd.read_csv("results_survey_bear.csv")

df = df_raw.drop(columns="Unnamed: 0")
df.columns

len(df.columns)

# drop metadata
df = df.drop(columns=["answer_id", "date_sent", "last_page", "start_lang", "random_value"])

# descr methods

desc = df[numeric_vars].describe().T
desc[['mean', 'std', 'min', '25%', '50%', '75%', 'max']]

# ##################### demographics

"""
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

axes[0].bar(
    edu_counts.index,
    edu_counts.values,
    edgecolor="black",
    linewidth=0.8
)

axes[0].set_title("Bildungsabschluss", fontsize=14, pad=10)
axes[0].set_xlabel("Abschluss", fontsize=14)
axes[0].set_ylabel("Anzahl", fontsize=14)

axes[0].tick_params(axis="x")
axes[0].grid(axis="y", linestyle="--", alpha=0.6)
axes[0].set_axisbelow(True)


bins = range(1, int(semester_data.max()) + 2)

axes[1].hist(
    semester_data,
    bins=bins,
    edgecolor="black",
    linewidth=0.8
)

axes[1].set_title("Anzahl der Semester", fontsize=14, pad=10)
axes[1].set_xlabel("Semester", fontsize=14)
axes[1].set_ylabel("Anzahl", fontsize=14)

axes[1].grid(axis="y", linestyle="--", alpha=0.6)
axes[1].set_axisbelow(True)


plt.tight_layout()
plt.savefig("bildungsabschluss_und_semester.pdf", dpi=300)
plt.close()
"""



#       abschluss und semester
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# ----------------------
# Plot 1: Education level
# ----------------------
edu_order = df["edu_level"].value_counts().index

sns.countplot(
    x="edu_level",
    data=df,
    order=edu_order,
    palette="pastel",
    ax=axes[0]
)

axes[0].set_title("Bildungsabschluss", fontsize=14, pad=10)
axes[0].set_xlabel("")
axes[0].set_ylabel("Anzahl", fontsize=14)

# Add counts + headroom
y_max = max(p.get_height() for p in axes[0].patches)
for p in axes[0].patches:
    axes[0].annotate(
        f"{int(p.get_height())}",
        (p.get_x() + p.get_width() / 2, p.get_height()),
        ha="center",
        va="bottom",
        fontsize=14
    )

axes[0].set_ylim(0, y_max * 1.1)
axes[0].grid(axis="y", alpha=0.3)
axes[0].set_axisbelow(True)
axes[0].tick_params(axis="x", labelsize=14)


# ----------------------
# Plot 2: Number of semesters
# ----------------------

df.loc[df["semester_n"] == 1.0,"semester_n"] = "1"
df.loc[df["semester_n"] == 2.0,"semester_n"] = "2"
df.loc[df["semester_n"] == 3.0,"semester_n"] = "3"
df.loc[df["semester_n"] == 4.0,"semester_n"] = "4"
df.loc[df["semester_n"] == 5.0,"semester_n"] = "5"
df.loc[df["semester_n"] == 6.0,"semester_n"] = "6"
df.loc[df["semester_n"] == 7.0,"semester_n"] = "7"
df.loc[df["semester_n"] == 10.0,"semester_n"] = "10"
df.loc[df["semester_n"] == 12.0,"semester_n"] = "12"

semester_order = df["semester_n"].value_counts().sort_index().index

sns.countplot(
    x="semester_n",
    data=df,
    order=semester_order,
    palette="pastel",
    ax=axes[1]
)

axes[1].set_title("Anzahl der Semester", fontsize=14, pad=10)
axes[1].set_xlabel("")
axes[1].set_ylabel("Anzahl", fontsize=14)

# Add counts + headroom
y_max = max(p.get_height() for p in axes[1].patches)
for p in axes[1].patches:
    axes[1].annotate(
        f"{int(p.get_height())}",
        (p.get_x() + p.get_width() / 2, p.get_height()),
        ha="center",
        va="bottom",
        fontsize=14,
    )

axes[1].set_ylim(0, y_max * 1.1)
axes[1].grid(axis="y", alpha=0.3)
axes[1].set_axisbelow(True)
axes[1].tick_params(axis="x", labelsize=14)


plt.tight_layout()
plt.savefig(
    "graphs/bildungsabschluss_und_semester_v2.pdf",
    dpi=300,
    bbox_inches="tight"
)
plt.close()


# ------------- demographics 2.0
df = faculty_generation(df)

order = df["faculty_clean"].value_counts().index

sns.countplot(
    x="faculty_clean",
    data=df,
    palette="pastel",
    order=order
)

ax = plt.gca()

# Add counts on top of bars
for p in ax.patches:
    ax.annotate(
        f'{int(p.get_height())}',
        (p.get_x() + p.get_width() / 2, p.get_height()),
        ha='center',
        va='bottom',
        fontsize=14
    )

# Add headroom so labels don't get cut off
y_max = max(p.get_height() for p in ax.patches)
ax.set_ylim(0, y_max * 1.1)

plt.title("Verteilung der Fakultäten", fontsize=14)
plt.ylabel("Anzahl", fontsize=14)
plt.xlabel("", fontsize=14)
plt.xticks(rotation=45, ha="right", fontsize=14)
plt.grid(axis="y", alpha=0.3)

plt.tight_layout()
plt.savefig(
    "graphs/faculty_distribution_v2.pdf",
    bbox_inches="tight"
)

# plt.show()
plt.close()

