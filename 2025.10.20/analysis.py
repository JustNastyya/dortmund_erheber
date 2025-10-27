import pandas as pd
import openpyxl as op
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# read and open and convert
wb = op.load_workbook("Nachtweial._2018_ProfPraef-Studie1_Datensatz_N3403_Studierende.xlsx", 
    read_only=True, data_only=True)

wb.sheetnames
data = pd.DataFrame(wb["2 Datensatz"].values)
data.columns = data.loc[0]
data = data[data.ID != "ID"]

# ready for c)
data.isna().sum()[data.isna().sum() != 0]

# c)
"""
ID                    27
zeit                  27
kritN                 27
zuver                 27
freund                27
empath                27
enth                  27
hilf                  27
fair                  27
humor                 27
hoef                  27
resp                  27
unterh                27
offen                 27
erreich               27
komm                  27
exp_in                27
exp_out               27
logstr                27
var_lehr              27
beruf_rel             27
team                  27
feed                  27
orient                27
sonst               3192
gender_off            40
gender_kod            40
age                   85
hochsch_off           40
hochsch_kod           40
fach_off             139
fach_kod             139
sem                   97
abschluss_off         41
abschluss_kod         41
note                 986
note_kod             986
arbeit               415
zufrie                51
fuehrung              50
fuehrung_kod          50
selbststaend          57
selbststaend_kod      57
anmerk              3306
"""

# d)
data[data.isna().sum(axis=1) == 0] # 5 studierende


# aufgabe 3
# a

# art der hochschule
fig = px.histogram(data, x="hochsch_off")
fig.show()

# semerster
data["sem"].mean() # 3.8
data["sem"].median() # 3

# note
# data[~data.note.isna()].note.mean()

data_note_float = pd.to_numeric(data['note'], errors='coerce')
data_note_float.mean() # 2.18
data_note_float.median() # 2.0

# arbeit
data["arbeit"].mean() # 10
data["arbeit"].median() # 8.0
data["arbeit"].max() # 80


# actuall 3
vars = [
    "zuver",
    "enth",
    "exp_in",
    "feed"
]
stats = ["min", "max", "median", "mean"]

results = data[vars].agg({
    var: stats
    for var in vars
})
results

df = data[vars].apply(lambda x: x.value_counts().reindex(list(range(0, 7)), fill_value=0))
df = df.T
fig = px.bar(df, x=df.index, y=df.columns)
fig.show()
data