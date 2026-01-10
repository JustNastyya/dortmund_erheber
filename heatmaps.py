import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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