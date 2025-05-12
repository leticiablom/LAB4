# Análise Comparativa: LLMs vs SonarQube na Detecção de Code Smells

**Alunos:** Arthur Capanema Bretas, Gabriel Vitor Oliveira, Júlia Borges Araújo, Letícia Rodrigues Blom

Este projeto tem como objetivo comparar a eficácia de modelos de linguagem de larga escala (LLMs), como o GPT-4, com a ferramenta de análise estática SonarQube na detecção de *code smells* em repositórios Java.

---

## Sobre o Dataset

O dataset foi construído a partir da análise de um ou mais repositórios Java. Para cada repositório, foram coletadas métricas relacionadas à quantidade e tipos de *smells* detectados por cada ferramenta.

### Informações presentes no dataset:
- Número total de *code smells* detectados por ferramenta.
- Diferenças absolutas e relativas entre os resultados.
- *Smells* exclusivos de cada ferramenta.
- Sobreposição por categoria.
- Categorias de *smells* analisadas:  
  - Duplicate Code  
  - Exception Handling  
  - Feature Envy  
  - Long Method  
  - Magic Numbers

---

## Ferramentas Utilizadas

- SonarQube – Análise estática tradicional.
- OpenAI GPT-4 – Modelo LLM utilizado para análise semântica.
- Scripts em Python – Para tratamento e organização dos dados.
- Google Data Studio – Para visualização interativa dos resultados.
- VS Code + extensões – Para análise de código-fonte.

---

## Painéis e Gráficos

O projeto inclui visualizações para facilitar a compreensão dos resultados, divididos em sessões:

### 1. Introdução ao Dataset
- Número de repositórios analisados.
- Ferramentas utilizadas.
- Tamanho dos repositórios (LOC, arquivos, classes).
- Tecnologias/frameworks utilizados.

### 2. Métricas Gerais
- Total de *code smells* por ferramenta.
- Diferença absoluta e percentual.
- Arquivos afetados.

### 3. Sobreposição e Exclusividade
- Smells comuns entre ferramentas.
- Smells exclusivos do GPT-4 e do SonarQube.
- Taxa de similaridade e exclusividade por categoria.

### 4. Análise por Categoria
- Frequência por tipo de *code smell*.
- Gráficos de barras e pizza mostrando distribuição por categoria.
- Percentual de sobreposição e exclusividade por categoria.

---

## Objetivos da Pesquisa

- Avaliar a qualidade da detecção automática por LLMs em comparação com ferramentas tradicionais.
- Identificar pontos fortes e fracos de cada abordagem.
- Investigar a complementaridade entre as ferramentas.

---
