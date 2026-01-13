#Hier ein paar Plots für die Fragen in Erhebungstechniken 


#Library installieren 
install.packages("tidyverse", dependencies = TRUE)
library(tidyverse)

#Reinladen der Umfrage ins global Enviorment
survey.data <- read.csv("results-survey_cleaned.csv")

#Frage 1 - Bevorzugen Studenten Strukturiertes oder Unstrukturiertes Lernen? 

#Unterscheidung: Wer ist sturkturiert und wer schiebt auf?

survey.data <- survey.data %>%
  mutate(
    Lerntyp = case_when(
      #1. Bedingung  Strukturierte Menschen bevorzugen Pflichtaufgaben
      Einstellung_Pflicht_Ball_Num >= 4 ~ "Strukturiert",
      
      #2. Bedingung Strukturierte die neutral zu Pflicht aufgaben 
      # stehen aber trotzdem nicht aufschieben
      Einstellung_Pflicht_Ball_Num == 3 & Einstellung_Aufschieben_Num <= 2 ~ "Strukturiert",
      
      #Alle anderen gelten als weniger/unstrukturiert 
      TRUE ~ "Unstrukturiert"
    )
  )

ggplot(data = survey.data, aes(x = Lerntyp)) +
  geom_bar() 


#Frage 2 - Welche Materialien bringen die höchste Zufriedenheit?


#Aufbereiten der Daten 
material.data <- survey.data %>% 
  #Aus dem Datensatz den zufriendenheitsscore und alle Lernmaterialen extrahieren 
  select(Zufriedenheit_Score, starts_with("Nutzung_"))  %>%
  
  #Verschiebung der Daten damit andere Funktionen später besser Funktionieren
  pivot_longer(
    cols = starts_with("Nutzung_"),
    names_to = "Material",
    values_to = "Nutzungshaeufigkeit"
  )

#"Aufhübschen" der Namensdaten für die Finale Darstellung im Plot
material.data <- material.data %>% 
  mutate(
    Material = str_remove(Material, "Nutzung_"),
    Material = str_remove(Material, "_Num")
  )

# Jetzt werten wir die Daten aus 
# Wir sortieren nach Leuten mit intensiver Nutzung (Score >= 4) 
# Nehmen deren Zufriedenheitswerte und errechnen daraus einen Durchschnitt
# Dann vergleichen wir diese 
satisfaction.analysis <- material.data %>%
  
  #Filtern nach leuten die das Material häufig nutzen
  filter(Nutzungshaeufigkeit >= 4) %>%
  
  #Gruppieren dieser Personen nach Gruppen
  group_by(Material) %>% 
  
  #Für jede Gruppe dann die Durchschnittliche Zufriedenheit ausrechnen
  summarise(
    avg.satisfaction = mean(Zufriedenheit_Score, na.rm = TRUE)
  ) %>%
  
  #Sortieren nach größe (Sieht später schöner aus)
  arrange(desc(avg.satisfaction))


#Erstellen eines Basic-Plots
ggplot(data = satisfaction.analysis, aes(x = Material, y = avg.satisfaction)) +
  geom_col() +
  
  #Damit drehen wir den Plot einmal auf die Seite ist einfach schöner zum ansehen 
  coord_flip()

#Frage 3 - Welche Materialien werden als am effizientesten/besten
#für die Prüfungsvorbereitung empfunden´

#Dazu werden wir einen "Erfolgsscore" erstellen wir addieren die Werte zu den Themen 
#Effizienz, Motivation, Sicherheit und Zeitaufwand und kategorisieren die Leute nach
#Erfolg und schauen dann welche Gruppen welche Materialien am Häufigsten Nutzen

survey.data <- survey.data %>%
  mutate(
    #Drehen des Zeitaufwand Scores damit er richtig  eingerechnet wird:
    Effizienz_Score = 6 - Effekt_Zeitaufwand_Num,
    
    #Jetzt einfach alle Zusammenaddieren(Höchste PunktZahl ist 20)
    Erfolgs_Score = Effekt_Sicherheit_Num + Effekt_Motivation_Num + Effizienz_Score + Effekt_Relevanz_Num
  )

#Labeling der Personen nach Erfolgsscore
survey.data <- survey.data  %>%
  mutate(
    Erfolgs_Label = case_when(
      Erfolgs_Score >= 17 ~  "Sehr Erfolgreich"   ,
      Erfolgs_Score >= 14 ~  "Erfolgreich"        ,
      Erfolgs_Score >= 9  ~  "Weniger Erfolgreich",
      TRUE ~ "Unerfolgreich"
    )
  )

succes.analysis <- survey.data %>%
  # 1. Datensatz wieder Langziehen für die funktion
  pivot_longer(
    cols = starts_with("Nutzung_"),
    names_to = "Material",
    values_to = "Nutzung"
  ) %>%
  
  #Wieder für die Tabelle  die namen "Säubern"
  mutate(
    Material = str_remove(Material, "Nutzung_"),
    Material = str_remove(Material, "_Num")
  )

succes.material.analysis <- succes.analysis  %>%
  
  #Gruppieren nach  Erfolgslabel und nach Material
  group_by(Material, Erfolgs_Label) %>%
  
  #Erechnen der Durchschnittlichen Nutzung in jeder Lerngruppe für jedes Material 
  summarise(
    Durchschnitt_Nutzung = mean(Nutzung, na.rm = TRUE)
  )
  
#Erstellen eines Gruppierten Barplots
ggplot(data = succes.material.analysis,
       aes(x = Erfolgs_Label,
           y = Durchschnitt_Nutzung,
           fill = Material)) +
  
  geom_col(position = "dodge") +

  coord_flip() +
  
  labs(
    title = "Materialnutzung nach Erfolgstyp",
    x = "Erfolgsgruppen",
    y = "avg Nutzungshäufigkeit (1-5)",
    fill =  "Lernmaterial"
  )







