import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from utils import materials_that_i_use, learning_materials_group, umnennen_heatmap
import numpy as np
import textwrap

def wrap_labels(labels, width=25):
    return ["\n".join(textwrap.wrap(label, width)) for label in labels]


df = pd.read_csv("results_survey_bear.csv")

df.columns

variables_to_correlate = [
    'sat_edu_sucess', 'semester_n', 'uebung_helpful', 'uebung_required',
    'materials_helpfull', 'uebung_required_postpone', 'effective_learning',
    'kurzscript_usage', 'fullscript_usage', 'notes_usage',
    'videos_lecture_usage', 'uebeung_sols_usage', 'books_usage',
    'old_exams_usage', 'videos_online_usage', 'ai_usage',
    'material_understanding', 'materials_orga', 'materials_complicated',
    'materials_ontime', 'materials_workload', 'materials_help',
    'materials_safety', 'materials_motivation',
    'materials_independent_learning', 'materials_learning_stress',
    'materials_timewaste', 'materials_safety_exam'
]

plt.figure(figsize=(20, 20))
sns.heatmap(df[variables_to_correlate].corr(), annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.3)
# plt.show()

plt.savefig("heatmap_all_vars.pdf")

korr_all = df[variables_to_correlate].corr()

korr_hoch = korr_all[korr_all.abs() >= 0.3] 

plt.figure(figsize=(20, 20))
sns.heatmap(korr_hoch, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.3)

plt.savefig("heatmap_only_big.pdf")
plt.show()


korr_hoch = korr_all[korr_all.abs() >= 0.3] 

for col in korr_hoch.columns:
    if sum(korr_hoch[col].isna()) == len(korr_hoch[col]) - 1: 
        korr_hoch = korr_hoch.drop(columns=col, index=col)

korr_hoch.columns


# lets see a heatmap only for variables of learning_materials_group and materials_that_i_use
vars_to_correlate = learning_materials_group.copy()
vars_to_correlate.extend(materials_that_i_use)

threshold = 0.4

corr = df[vars_to_correlate].corr()

# Bool-Matrix: starke Korrelationen (Diagonale ignorieren)
strong_corr = corr.abs() >= threshold
np.fill_diagonal(strong_corr.values, False)

# Variablen behalten, die mindestens eine starke Korrelation haben
vars_keep = strong_corr.any(axis=1)

corr_filtered = corr.loc[vars_keep, vars_keep]

corr_filtered = corr_filtered.where(corr_filtered.abs() >= threshold)
corr_filtered = corr_filtered.rename(
    index=umnennen_heatmap,
    columns=umnennen_heatmap
)
corr_filtered.index = wrap_labels(corr_filtered.index, width=28)
corr_filtered.columns = wrap_labels(corr_filtered.columns, width=28)

plt.figure(figsize=(22, 22))

ax = sns.heatmap(
    corr_filtered,
    annot=True,
    cmap="coolwarm",
    fmt=".2f",
    linewidths=0.3,
    square=True,
    vmin=-1,
    vmax=1,
    center=0,
    annot_kws={"size": 22}   # 🔹 Zahlen größer
)
ax.tick_params(
    axis="both",
    which="major",
    labelsize=23
)

plt.xticks(rotation=45, ha="right")
plt.yticks(rotation=0)


plt.savefig("heatmap_only_big_only_materials.pdf", bbox_inches="tight")
plt.show()
