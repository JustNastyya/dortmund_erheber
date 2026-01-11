import pandas as pd
from utils import renaming_dict


df = pd.read_csv("results-survey478754.csv")

df_new = df.rename(columns=renaming_dict)

answer_mapping = {
    "Stimme voll und ganz zu": 5,
    "Stimme eher zu": 4,
    "Neutral":3,
    "Stimme eher nicht zu": 2,
    "Stimme überhaupt nicht zu": 1
}

zufr_mapping = {
    "Sehr unzufrieden": 5,
    "Eher unzufrieden": 4,
    "Neutral": 3,
    "Eher zufrieden": 2,
    "Sehr zufrieden": 1
}

time_mapping = {
    "Immer": 5,
    "Selten": 4,
    "Oft": 3,
    "Manchmal": 2,
    "Gar nicht": 1
}

df_end = df_new.copy()
df_end = df_end.replace(answer_mapping)
df_end = df_end.replace(time_mapping)
df_end = df_end.replace(zufr_mapping)

df_end.to_csv("results_survey_bear.csv")

df_end.columns
