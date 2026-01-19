import pandas as pd
import matplotlib.pyplot as plt
from utils import numeric_vars, learning_materials_group, materials_that_i_use, allgemein, umnennen_der_variablen_usage, umnennen_materials, umnennen_allgemein
import numpy as np
import textwrap

def wrap_labels(labels, width=40):
    return ["\n".join(textwrap.wrap(label, width=width)) for label in labels]

likert_colors = {
    1: "#d73027",
    2: "#fc8d59",
    3: "#fee08b",
    4: "#91bfdb",
    5: "#4575b4"
}

def sort_by_agreement(df, variables):
    agreement = (
        df[variables]
        .apply(lambda x: (x >= 4).mean())
        .sort_values()
        .index
    )
    return list(agreement)


def likert_stacked_bar(df, variables, title, filename, renaming):
    counts = (
        df[variables]
        .apply(lambda x: x.value_counts(normalize=True))
        .T
        .fillna(0)
    )

    counts = counts.reindex(columns=[1, 2, 3, 4, 5], fill_value=0)
    y_labels = [renaming.get(var, var) for var in counts.index]
    y_labels = wrap_labels(y_labels, width=45)

    fig, ax = plt.subplots(figsize=(8, 0.6 * len(variables)))

    left = np.zeros(len(counts))
    
    # counts.index = y_labels

    for value in counts.columns:
        ax.barh(
            y_labels,
            counts[value],
            left=left,
            color=likert_colors[value],
            label=str(value)
        )
        left += counts[value].values

    ax.set_title(title)
    ax.set_xlabel("[%] der Befragten")
    ax.set_xlim(0, 1)

    ax.legend(
        title="Antwort",
        bbox_to_anchor=(1.05, 1),
        loc="upper left"
    )

    plt.tight_layout()
    if filename:
        plt.savefig(filename, format="pdf", bbox_inches="tight")

df_raw = pd.read_csv("results_survey_bear.csv")

df = df_raw.drop(columns="Unnamed: 0")
df.columns

# drop metadata

df = df.drop(columns=["answer_id", "date_sent", "last_page", "start_lang", "random_value"])

# descr methods

desc = df[numeric_vars].describe().T
desc[['mean', 'std', 'min', '25%', '50%', '75%', 'max']]

learning_materials_group_sorted = sort_by_agreement(df, learning_materials_group)
likert_stacked_bar(
    df,
    variables=learning_materials_group_sorted,
    title="Wie häufig nutzen Sie die folgenden Arten von Lernmaterialien?",
    filename="graphs/learning_materials_group_sorted.pdf",
    renaming=umnennen_der_variablen_usage
)

materials_that_i_use_sorted = sort_by_agreement(df, materials_that_i_use)
likert_stacked_bar(
    df,
    variables=materials_that_i_use_sorted,
    title="Die Materialien, die ich benutze...",
    filename="graphs/materials_that_i_use_sorted.pdf",
    renaming=umnennen_materials
)

allgemein_sorted = sort_by_agreement(df, allgemein)
likert_stacked_bar(
    df,
    variables=allgemein_sorted,
    title="Allgemein",
    filename="graphs/allgemein_sorted.pdf",
    renaming=umnennen_allgemein
)

