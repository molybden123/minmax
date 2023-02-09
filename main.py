# Importera Pandas
import pandas as pd

# Läs in CSV filen
df = pd.read_csv('Automobile_data.csv')

# Skapa en funktion som normaliserar datan i CSV filen
def normalize(df):
# Läs in CSV filen som en kopia
    result = df.copy()
# Välj alla kolumner som innehåller tal, exkludera index kolumnen
    for feature_name in df[df.columns[~df.columns.isin(['index'])]].select_dtypes(include=['int', 'float']).columns:
# Läs in värdena från dessa kolumner
        max_value = df[feature_name].max()
        min_value = df[feature_name].min()
# Normalisera alla värden
        result[feature_name] = (df[feature_name] - min_value) / (max_value - min_value)
# Returnera resultatet
    return result

# Skapa en variabel som innehåller hela resultatet
df2 = normalize(df)

# Spara den nya normaliserade filen
df2.to_csv('Automobile_data_normalized')

