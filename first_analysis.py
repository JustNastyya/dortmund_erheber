import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("results_survey_bear.csv")

df = df.drop(columns="Unnamed: 0")
df.columns

# nan values