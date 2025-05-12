import json
import pandas as pd

# Carrega o JSON
with open("resultados_gqm.json", "r") as f:
    data = json.load(f)

# Cria uma lista de DataFrames
dataframes = {}

# --- Question 1: metrica_1_1 ---
metrica_1_1 = data["question1"]["metrica_1_1"]
df_1_1 = pd.DataFrame(metrica_1_1.items(), columns=["Métrica", "Valor"])
dataframes["metrica_1_1"] = df_1_1

# --- Question 1: metrica_1_2 ---
metrica_1_2 = data["question1"]["metrica_1_2"]
df_1_2 = pd.DataFrame(metrica_1_2.items(), columns=["Métrica", "Valor"])
dataframes["metrica_1_2"] = df_1_2

# --- Question 3: metrica_3_1 - por categoria ---
llm_cat = data["question3"]["metrica_3_1"]["llm_por_categoria"]
sonar_cat = data["question3"]["metrica_3_1"]["sonarqube_por_categoria"]
categorias = list(data["categorias"])

df_3_1 = pd.DataFrame({
    "Categoria": categorias,
    "LLM": [llm_cat.get(cat, 0) for cat in categorias],
    "SonarQube": [sonar_cat.get(cat, 0) for cat in categorias]
})
dataframes["metrica_3_1"] = df_3_1

# Exportar para um arquivo Excel com várias abas
with pd.ExcelWriter("metrica_resultados.xlsx") as writer:
    for nome, df in dataframes.items():
        df.to_excel(writer, sheet_name=nome, index=False)

print("Arquivo Excel criado com sucesso!")
