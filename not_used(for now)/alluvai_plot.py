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

LIKERT_COLORS = {
    1: "#d73027",  # strongly disagree
    2: "#fc8d59",
    3: "#fee08b",
    4: "#91bfdb",
    5: "#4575b4"   # strongly agree
}
def hex_to_rgba(hex_color, alpha=0.6):
    hex_color = hex_color.lstrip("#")
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)
    return f"rgba({r},{g},{b},{alpha})"



df_raw = pd.read_csv("results_survey_bear.csv")

df_raw = df_raw.drop(columns="Unnamed: 0")
df_raw.columns

# nan values

df = df_raw[df_raw.isna().sum(axis=1) < 30]

len(df.columns)

# fuck metadata

df = df.drop(columns=["answer_id", "date_sent", "last_page", "start_lang", "random_value"])




def likert_alluvial(df, var_left, var_right, title=None):
    data = (
        df[[var_left, var_right]]
        .dropna()
        .astype(int)
    )

    likert_order = [5, 4, 3, 2, 1]

    counts = (
        data
        .value_counts()
        .reindex(
            pd.MultiIndex.from_product(
                [likert_order, likert_order],
                names=[var_left, var_right]
            ),
            fill_value=0
        )
        .reset_index(name="count")
    )

    source_map = {v: i for i, v in enumerate(likert_order)}
    target_map = {v: i + 5 for i, v in enumerate(likert_order)}

    sources = counts[var_left].map(source_map)
    targets = counts[var_right].map(target_map)
    values = counts["count"]

    # y = 0 is TOP → keep 5 at the top
    y_positions = [i / 4 for i in range(5)]
    node_y = y_positions + y_positions
    node_x = [0.0] * 5 + [1.0] * 5

    node_colors = (
        [hex_to_rgba(LIKERT_COLORS[v], 0.9) for v in likert_order] +
        [hex_to_rgba(LIKERT_COLORS[v], 0.9) for v in likert_order]
    )

    link_colors = counts[var_left].map(
        lambda v: hex_to_rgba(LIKERT_COLORS[v], 0.45)
    )

    fig = go.Figure(go.Sankey(
        arrangement="fixed",
        node=dict(
            x=node_x,
            y=node_y,
            pad=25,
            thickness=20,
            label=[""] * 10,      # no labels at all
            color=node_colors,
            hoverinfo="none"      # no hover numbers
        ),
        link=dict(
            source=sources,
            target=targets,
            value=values,
            color=link_colors,
            hoverinfo="none"      # no hover numbers
        )
    ))

    fig.update_layout(
        title=title or f"{var_left} → {var_right}",
        showlegend=False,
        margin=dict(l=40, r=40, t=60, b=40)
    )

    fig.write_image(f"graphs/alluvai_{var_left}-{var_right}.pdf", format="pdf")


likert_alluvial(df, "kurzscript_usage", "materials_workload")
