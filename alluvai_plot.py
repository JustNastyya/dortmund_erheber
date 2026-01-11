import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from utils import numeric_vars, learning_materials_group, materials_that_i_use, allgemein, demog
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.graph_objects as go

likert_colors = {
    1: "#d73027",  # strong disagree
    2: "#fc8d59",
    3: "#fee08b",
    4: "#91bfdb",
    5: "#4575b4"   # strong agree
}


df_raw = pd.read_csv("results_survey_bear.csv")

df_raw = df_raw.drop(columns="Unnamed: 0")
df_raw.columns

# nan values

df = df_raw[df_raw.isna().sum(axis=1) < 30]

len(df.columns)

# fuck metadata

df = df.drop(columns=["answer_id", "date_sent", "last_page", "start_lang", "random_value"])


def likert_alluvial(
    df,
    var_left,
    var_right,
    title=None
):

    # drop missing values and ensure integer
    data = (
        df[[var_left, var_right]]
        .dropna()
        .astype(int)
    )

    # count transitions
    counts = (
        data
        .value_counts()
        .reset_index(name="count")
    )

    # node labels
    left_labels = [f"{var_left}: {i}" for i in range(1, 6)]
    right_labels = [f"{var_right}: {i}" for i in range(1, 6)]
    labels = left_labels + right_labels

    # index mapping
    source_map = {i: idx for idx, i in enumerate(range(1, 6))}
    target_map = {i: idx + 5 for idx, i in enumerate(range(1, 6))}

    sources = counts[var_left].map(source_map)
    targets = counts[var_right].map(target_map)
    values = counts["count"]

    # create sankey plot
    fig = go.Figure(go.Sankey(
        arrangement="snap",
        node=dict(
            pad=15,
            thickness=15,
            label=labels
        ),
        link=dict(
            source=sources,
            target=targets,
            value=values
        )
    ))

    fig.update_layout(
        title=title or f"{var_left} → {var_right}",
        font_size=11
    )

    plt.savefig(f"graphs/alluvai_{var_left}-{var_right}.pdf", format="pdf", bbox_inches="tight")



likert_alluvial(df, "kurzscript_usage", "material_understanding")