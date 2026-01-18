import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from utils import umnennen_bar_plot, learning_materials_group, materials_that_i_use, allgemein, umnennen_der_variablen_usage, umnennen_materials, umnennen_allgemein
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import textwrap

def wrap_labels(labels, width=40):
    return ["\n".join(textwrap.wrap(label, width=width)) for label in labels]

df = pd.read_csv("results_survey_bear.csv")

target_var = "sat_edu_sucess"

vars_to_correlate = learning_materials_group.copy()
vars_to_correlate.extend(materials_that_i_use)
vars_to_correlate.extend(allgemein)

corr = df[[target_var] + vars_to_correlate].corr(method="spearman")

# Nur Korrelationen mit sat_edu_sucess
corr_target = corr[[target_var]].drop(index=target_var)

# threshold = 0.3
# corr_target_filtered = corr_target[corr_target[target_var].abs() >= threshold]

# Optional: sortieren (stärkste oben)
corr_target_filtered = corr_target.sort_values(
    by=target_var, ascending=True
)



corr_plot = corr_target_filtered.copy()
corr_plot.columns = ["Spearman ρ"]

corr_plot.index = corr_plot.index.map(lambda x: umnennen_bar_plot.get(x, x))
corr_plot.index = wrap_labels(corr_plot.index, width=50)



plt.figure(figsize=(10, max(6, len(corr_plot) * 0.5)))

colors = corr_plot["Spearman ρ"].apply(
    lambda x: "steelblue" if x > 0 else "indianred"
)

plt.barh(
    corr_plot.index,
    corr_plot["Spearman ρ"],
    color=colors
)

plt.axvline(0, color="black", linewidth=1)
plt.axvline(0.3, color="gray", linestyle="--", linewidth=1)
plt.axvline(-0.3, color="gray", linestyle="--", linewidth=1)

plt.xlabel("Spearman-Korrelation (ρ)", fontsize=14)
plt.title(
    "Zusammenhang mit Lernerfolg",
    fontsize=16,
    pad=15
)

plt.gca().invert_yaxis()
plt.grid(axis="x", alpha=0.3)

plt.tight_layout()
plt.savefig(
    "graphs/barplot_sat_edu_success_correlations.pdf",
    bbox_inches="tight"
)


plt.figure(figsize=(7, 5))

# Count of each category

df.loc[df["sat_edu_sucess"].isna(),"sat_edu_sucess"] = "Nicht angegeben"
df.loc[df["sat_edu_sucess"] == 1.0,"sat_edu_sucess"] = "1"
df.loc[df["sat_edu_sucess"] == 2.0,"sat_edu_sucess"] = "2"
df.loc[df["sat_edu_sucess"] == 3.0,"sat_edu_sucess"] = "3"
df.loc[df["sat_edu_sucess"] == 4.0,"sat_edu_sucess"] = "4"
df.loc[df["sat_edu_sucess"] == 5.0,"sat_edu_sucess"] = "5"

sns.countplot(
    x="sat_edu_sucess",
    data=df,
    palette="pastel",
    order=sorted(df["sat_edu_sucess"].unique())  # ensures 1-5 order
)

# Add counts on top of bars
for p in plt.gca().patches:
    plt.gca().annotate(
        f'{int(p.get_height())}', 
        (p.get_x() + p.get_width() / 2, p.get_height()), 
        ha='center', 
        va='bottom',
        fontsize=11
    )

plt.xlabel("Lernerfolg", fontsize=12)
plt.ylabel("Anzahl der Teilnehmenden", fontsize=12)
plt.title("Verteilung des Lernerfolgs", fontsize=14, pad=15)
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()

plt.savefig(
    "graphs/barplot_edu_sucess.pdf",
    bbox_inches="tight"
)
# plt.show()
