import random
import numpy
from matplotlib import pyplot
import pandas as pd

df = pd.read_csv("Ankereffekt.csv", sep=";")
df.columns
df.isna().sum() # eine na reihe, kann man aussschliessen
df = df[df.index != 25]

anker_l = [
    'Anker1', 'Anker2','Anker3', 'Anker4'
]
antwort_l = [
    'Antwort1', 'Antwort2', 'Antwort3', 'Antwort4'
]

# Aufgabe 2

# a) descriptive statistics. will be using mean difference to the anker value

df_difference = df.copy()
for i in range(4):    
    anker = anker_l[i]
    antwort = antwort_l[i]

    df_difference[antwort] = (df_difference[antwort] - df_difference[anker]).abs()

df[antwort_l].mean() # mean difference from the anker


# b)
# doing a istogramm for every answered question
for i in range(4):    
    antwort = antwort_l[i]
    
    pyplot.hist(df[antwort], alpha=0.5, label=antwort)
    pyplot.legend(loc='upper right')
    pyplot.savefig(f"{antwort}.png")
    pyplot.show()

# c)
# difference of means between different anker values

for i in range(4):    
    anker = anker_l[i]
    antwort = antwort_l[i]

    values = df.groupby([anker]).mean()[antwort].to_list()
    print(f"for {antwort} is the difference of means: {abs(values[0] - values[1])}")
    


# c) plotting the results. i am plotting 2 histograms simultaniously 
# with alpha = 0.5 to see the differences between values distributions

for i in range(4):    
    anker = anker_l[i]
    antwort = antwort_l[i]
    anker_values = df[anker].unique()
    
    x = df[df[anker] == anker_values[0]][antwort]
    y = df[df[anker] == anker_values[1]][antwort]
    
    max_value = max(x.max(), y.max())
    min_value = min(x.min(), y.min())
    bins = numpy.linspace(min_value, max_value, 100)
    
    pyplot.hist(x, alpha=0.5, label=anker_values[0])
    pyplot.hist(y, alpha=0.5, label=anker_values[1])
    pyplot.legend(loc='upper right')
    pyplot.savefig(f"{anker}_devided.png")
    pyplot.show()
    

# d)
# nein, nicht wirklich. es liegt nicht wirklich an den Einheiten (Temperatur, Hoehe), 
# sondern an den Groessen. Für eine sinnvolle Auswertung müsste man die Beobachtungsvektoren
# erstmal standartisieren