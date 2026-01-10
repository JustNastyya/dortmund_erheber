import pandas as pd


df = pd.read_csv("results-survey478754.csv")

renaming_dict = {
    'Antwort ID': "answer_id",
    'Datum Abgeschickt': "date_sent",
    'Letzte Seite': "last_page",
    'Start-Sprache': "start_lang",
    'Zufallsstartwert': "random_value",
    'Wie zufrieden sind Sie mit ihrem aktuellen Lernerfolg?': "sat_edu_sucess",
    'Welcher Fakultät gehört Ihr Studiengang an?': "faculty",
    'Welcher Fakultät gehört Ihr Studiengang an? [Sonstiges]': "faculty_other",
    'Welchen Abschluss erhalten Sie in Ihrem aktuellen Studiengang?': "edu_level",
    'Welchen Abschluss erhalten Sie in Ihrem aktuellen Studiengang? [Sonstiges]': "edu_level_other",
    'Im wievielten Fachsemester studieren Sie?': "semester_n",
    'Wählen Sie bitte die passende Aussage aus. [Ich empfinde die wöchentlichen Übungsaufgaben als hilfreich.]': "uebung_helpful",
    'Wählen Sie bitte die passende Aussage aus. [Wenn Übungsaufgaben verpflichtend sind, hilft es mir am Ball zu bleiben.]': "uebung_required",
    'Wählen Sie bitte die passende Aussage aus. [Normalerweise finde ich die einem Kurs gestellten Materialien ausreichend und hilfreich.]': "materials_helpfull",
    'Wählen Sie bitte die passende Aussage aus. [Wenn ein Kurs keine Verpflichtungen oder Fristen vorgibt, schiebe ich vieles auf.]': "uebung_required_postpone",
    'Wählen Sie bitte die passende Aussage aus. [Effizientes Lernen in der Prüfungsvorbereitung ist mir wichtig]': "effective_learning",
    'Wie häufig nutzen Sie (falls gegeben) die folgenden Arten von Lernmaterialien? [Kurzskript]': "kurzscript_usage",
    'Wie häufig nutzen Sie (falls gegeben) die folgenden Arten von Lernmaterialien? [Vollständiges Skript]': "fullscript_usage",
    'Wie häufig nutzen Sie (falls gegeben) die folgenden Arten von Lernmaterialien? [Mitschriften aus der Vorlesung]': "notes_usage",
    'Wie häufig nutzen Sie (falls gegeben) die folgenden Arten von Lernmaterialien? [Videoaufzeichnungen der Vorlesung]': "videos_lecture_usage",
    'Wie häufig nutzen Sie (falls gegeben) die folgenden Arten von Lernmaterialien? [Übungsaufgaben mit Musterlösung]': "uebeung_sols_usage",
    'Wie häufig nutzen Sie (falls gegeben) die folgenden Arten von Lernmaterialien? [Bücher]': "books_usage",
    'Wie häufig nutzen Sie (falls gegeben) die folgenden Arten von Lernmaterialien? [Altklausuren]': "old_exams_usage",
    'Wie häufig nutzen Sie (falls gegeben) die folgenden Arten von Lernmaterialien? [Online-Videos (z.B. YouTube)]': "videos_online_usage",
    'Wie häufig nutzen Sie (falls gegeben) die folgenden Arten von Lernmaterialien? [KI-Chatbots (z.B. Chat-GPT, Gemini)]': "ai_usage",
    'Die Materialien, die ich benutze... [... fördern Verstehen statt Auswendiglernen.]': "material_understanding",
    'Die Materialien, die ich benutze... [... sind klar strukturiert und organisiert.]': "materials_orga",
    'Die Materialien, die ich benutze... [... sind nicht unnötig kompliziert dargestellt.]': "materials_complicated",
    'Die Materialien, die ich benutze... [... stehen rechtzeitig zur Verfügung.]': "materials_ontime",
    'Die Materialien, die ich benutze... [... erhöhen meine Arbeitsbelastung.]': "materials_workload",
    'Die Materialien, die ich benutze... [... erleichtern meinen Lernprozess.]': "materials_help",
    'Die Materialien, die ich benutze... [... geben mir Sicherheit, den Stoff zu schaffen.]': "materials_safety",
    'Die Materialien, die ich benutze... [... steigern meine Motivation.]': "materials_motivation",
    'Die Materialien, die ich benutze... [... unterstützen mein selbstständiges Lernen.]': "materials_independent_learning",
    'Die Materialien, die ich benutze... [... reduzieren meinen Prüfungsstress.]': "materials_learning_stress",
    'Die Materialien, die ich benutze... [... erhöhen meinen Zeitaufwand.]': "materials_timewaste",
    'Die Materialien, die ich benutze... [... geben mir Sicherheit über Prüfungsrelevanz.]': "materials_safety_exam",
    'Feedback zur Umfrage': "feedback"
}

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
