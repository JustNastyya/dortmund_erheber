import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from utils import numeric_vars, learning_materials_group, materials_that_i_use, allgemein, demog
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

likert_colors = {
    1: "#d73027",  # strong disagree
    2: "#fc8d59",
    3: "#fee08b",
    4: "#91bfdb",
    5: "#4575b4"   # strong agree
}

def sort_by_agreement(df, variables):
    agreement = (
        df[variables]
        .apply(lambda x: (x >= 4).mean())
        .sort_values()
        .index
    )
    return list(agreement)


def likert_stacked_bar(df, variables, title, filename):
    # count responses
    counts = (
        df[variables]
        .apply(lambda x: x.value_counts(normalize=True))
        .T
        .fillna(0)
    )

    # ensure full 1–5 scale exists
    counts = counts.reindex(columns=[1, 2, 3, 4, 5], fill_value=0)

    # plot
    fig, ax = plt.subplots(figsize=(8, 0.6 * len(variables)))

    left = np.zeros(len(counts))

    for value in counts.columns:
        ax.barh(
            counts.index,
            counts[value],
            left=left,
            color=likert_colors[value],
            label=str(value)
        )
        left += counts[value].values

    ax.set_title(title)
    ax.set_xlabel("Share of responses")
    ax.set_xlim(0, 1)

    ax.legend(
        title="Response",
        bbox_to_anchor=(1.05, 1),
        loc="upper left"
    )

    plt.tight_layout()
    if filename:
        plt.savefig(filename, format="pdf", bbox_inches="tight")

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

learning_materials_group_sorted = sort_by_agreement(df, learning_materials_group)
likert_stacked_bar(
    df,
    learning_materials_group_sorted,
    "Usage of Learning Materials",
    filename="graphs/learning_materials_group_sorted.pdf"
)

materials_that_i_use_sorted = sort_by_agreement(df, materials_that_i_use)
likert_stacked_bar(
    df,
    materials_that_i_use_sorted,
    "Perceived Usage of Learning Materials",
    filename="graphs/materials_that_i_use_sorted.pdf"
)

allgemein_sorted = sort_by_agreement(df, allgemein)
likert_stacked_bar(
    df,
    allgemein_sorted,
    "Generall",
    filename="graphs/allgemein_sorted.pdf"
)

# idea: like a floating plot from learning_materials_group to materials_that_i_use