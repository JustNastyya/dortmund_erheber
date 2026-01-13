import pandas as pd
import numpy as np


numeric_vars = [
    'sat_edu_sucess', 'semester_n', 'uebung_helpful', 'uebung_required',
    'materials_helpfull', 'uebung_required_postpone', 'effective_learning',
    'kurzscript_usage', 'fullscript_usage', 'notes_usage',
    'videos_lecture_usage', 'uebeung_sols_usage', 'books_usage',
    'old_exams_usage', 'videos_online_usage', 'ai_usage',
    'material_understanding', 'materials_orga', 'materials_complicated',
    'materials_ontime', 'materials_workload', 'materials_help',
    'materials_safety', 'materials_motivation',
    'materials_independent_learning', 'materials_learning_stress',
    'materials_timewaste', 'materials_safety_exam'
]

learning_materials_group = [
    "kurzscript_usage",
    "fullscript_usage",
    "notes_usage",
    "videos_lecture_usage",
    "uebeung_sols_usage",
    "books_usage",
    "old_exams_usage",
    "videos_online_usage",
    "ai_usage"
]

materials_that_i_use = [
    "material_understanding",
    "materials_orga",
    "materials_complicated",
    "materials_ontime",
    "materials_workload",
    "materials_help",
    "materials_safety",
    "materials_motivation",
    "materials_independent_learning",
    "materials_learning_stress",
    "materials_timewaste",
    "materials_safety_exam"
]

allgemein = [
    "uebung_helpful",
    "uebung_required",
    "materials_helpfull",
    "uebung_required_postpone",
    "effective_learning",
    "sat_edu_sucess"
]

demog = [
    "faculty",
    "faculty_other",
    "edu_level",
    "edu_level_other",
    "semester_n"
]



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


umnennen_der_variablen_usage = {
    "kurzscript_usage": "Kurzskript",
    "fullscript_usage": "Vollständiges Skript",
    "notes_usage": "Mitschriften aus der Vorlesung",
    "videos_lecture_usage": "Videoaufzeichnungen der Vorlesung",
    "uebeung_sols_usage": "Übungsaufgaben mit Musterlösung",
    "books_usage": "Bücher",
    "old_exams_usage": "Altklausuren",
    "videos_online_usage": "Online-Videos",
    "ai_usage": "KI-Chatbots"
}

umnennen_materials = {
    "material_understanding": "fördern Verstehen statt Auswendiglernen",
    "materials_orga": "sind klar strukturiert und organisiert",
    "materials_complicated": "sind nicht unnötig kompliziert dargestellt",
    "materials_ontime": "stehen rechtzeitig zur Verfügung",
    "materials_workload": "erhöhen meine Arbeitsbelastung",
    "materials_help": "erleichtern meinen Lernprozess",
    "materials_safety": "geben mir Sicherheit, den Stoff zu schaffen",
    "materials_motivation": "steigern meine Motivation",
    "materials_independent_learning": "unterstützen mein selbstständiges Lernen",
    "materials_learning_stress": "reduzieren meinen Prüfungsstress",
    "materials_timewaste": "erhöhen meinen Zeitaufwand",
    "materials_safety_exam": "geben mir Sicherheit über Prüfungsrelevanz",
}

umnennen_allgemein = {
    "sat_edu_sucess": "Wie zufrieden sind Sie mit ihrem aktuellen Lernerfolg?",
    "uebung_helpful": "Ich empfinde die wöchentlichen Übungsaufgaben als hilfreich",
    "uebung_required": "Wenn Übungsaufgaben verpflichtend sind, hilft es mir am Ball zu bleiben.",
    "materials_helpfull": "Normalerweise finde ich die einem Kurs gestellten Materialien ausreichend und hilfreich.",
    "uebung_required_postpone": "Wenn ein Kurs keine Verpflichtungen oder Fristen vorgibt, schiebe ich vieles auf.",
    "effective_learning": "Effizientes Lernen in der Prüfungsvorbereitung ist mir wichtig.",
}

umnennen_heatmap = {
    "kurzscript_usage": "Nutzung: Kurzskript",
    "fullscript_usage": "Nutzung: Vollständiges Skript",
    "notes_usage": "Nutzung: Mitschriften",
    "videos_lecture_usage": "Nutzung: Videoaufzeichnungen der Vorlesung",
    "uebeung_sols_usage": "Nutzung: Übungsaufgaben mit Musterlösung",
    "books_usage": "Nutzung: Bücher",
    "old_exams_usage": "Nutzung: Altklausuren",
    "videos_online_usage": "Nutzung: Online-Videos",
    "ai_usage": "Nutzung: KI-Chatbots",
    "material_understanding": "Materialien: fördern Verstehen",
    "materials_orga": "Materialien: klar strukturiert",
    "materials_complicated": "Materialien: nicht kompliziert",
    "materials_ontime": "Materialien: rechtzeitig",
    "materials_workload": "Materialien: erhöhen die Arbeitsbelastung",
    "materials_help": "Materialien: erleichtern das Lernprozess",
    "materials_safety": "Materialien: geben Sicherheit",
    "materials_motivation": "Materialien: steigern die Motivation",
    "materials_independent_learning": "Materialien: selbstständiges Lernen",
    "materials_learning_stress": "Materialien: reduzieren das Prüfungsstress",
    "materials_timewaste": "Materialien: erhöhen das Zeitaufwand",
    "materials_safety_exam": "Materialien: geben mir Sicherheit",
}


FACULTY_MAP = {
    # Informatik / IT
    "informatik": "Informatik",
    "bci": "Informatik",

    # Mathematik / Statistik
    "mathematik": "Mathematik",
    "statistik": "Statistik",
    "statistik/ sport": "Statistik",

    # Physik / Chemie
    "physik": "Physik",
    "chemie/chemische biologie": "Chemie",
    "chemische biologie": "Chemie",

    # Maschinenbau / Bau
    "maschinenbau": "Maschinenbau",
    "maschinenbau ": "Maschinenbau",
    "maschienenbau": "Maschinenbau",
    "bauingenieurwesen": "Bauingenieurwesen",
    "bauwesen": "Bauingenieurwesen",
    "architektur und städtebau": "Architektur",
    "raumplanung": "Raumplanung",

    # Wirtschaft
    "wirtschaftswissenschaften": "Wirtschaftswissenschaften",
    "wiwi": "Wirtschaftswissenschaften",
    "economics": "Wirtschaftswissenschaften",
    "wirtschafts- und sozialwissenschaften": "Wirtschaftswissenschaften",

    # Sozial / Erziehungswissenschaften
    "soziologie": "Sozialwissenschaften",
    "sozialwissenschaften": "Sozialwissenschaften",
    "erziehungswissenschaft": "Erziehungswissenschaften",
    "erziehungswissenschaften": "Erziehungswissenschaften",
    "erziehungswissenschaft und anglistik": "Erziehungswissenschaften",
    "rehabilitationswissenschaften": "Rehabilitationswissenschaften",
    "rehawissenschaften": "Rehabilitationswissenschaften",

    # Lehramt
    "lehramt": "Lehramt",
    "lehramt / kulturwissenschaften": "Lehramt",
    "sachunterricht": "Lehramt",
}


def normalize_text(x):
    if pd.isna(x):
        return np.nan
    x = x.lower()
    x = x.strip()
    x = " ".join(x.split())
    return x


def faculty_generation(df):
    df["faculty_raw"] = df["faculty"]

    mask = df["faculty"].isna() | (df["faculty"] == "Sonstiges")
    df.loc[mask, "faculty_raw"] = df.loc[mask, "faculty_other"]
    df["faculty_norm"] = df["faculty_raw"].apply(normalize_text)
    
    df["faculty_clean"] = df["faculty_norm"].map(FACULTY_MAP)
    df["faculty_clean"] = df["faculty_clean"].fillna("Sonstiges")
    
    df[df["faculty_clean"] == "Sonstiges"] = "Fakultät nicht angegeben"
    return df
