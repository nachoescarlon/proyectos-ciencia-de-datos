# Portafolio de Ciencia de Datos | Ignacio Escarlon

Hola, Soy estudiante de la Licenciatura en Ciencia de Datos. Este repositorio documenta mis proyectos prácticos de análisis, extracción de datos, SQL y Machine Learning, siempre con el foco en resolver problemas mediante el ciclo de vida del dato.

---

# Proyectos Destacados

# 1. Predicción de Taquilla Cinematográfica (Regresión)
**Objetivo:** Estimar la recaudación global de proyectos de Hollywood basándonos en presupuestos históricos y géneros cinematográficos.
* **Tecnologías:** Python, Pandas, Scikit-Learn (Random Forest Regressor), SQL (MySQL), SQLAlchemy, Seaborn.
* **Proceso Técnico:** 
  * Parseo de estructuras web JSON para extracción de variables categóricas (`MultiLabelBinarizer`).
  * Limpieza de sesgos financieros (eliminación de presupuestos e ingresos en cero).
  * Inyección automatizada del dataset limpio a una base de datos relacional (MySQL).
* **Resultados:** Modelo predictivo iterado que logró explicar el **73.60%** ($R^2$) del éxito financiero en la taquilla.

# 2. Supervivencia en el Titanic (Clasificación - Kaggle)
**Objetivo:** Determinar la probabilidad de supervivencia de pasajeros sobre datos ciegos en la competencia oficial de Kaggle.
* **Tecnologías:** Python, Pandas, Scikit-Learn (Random Forest Classifier).
* **Proceso Técnico:** Imputación algorítmica de valores nulos e Ingeniería de Características (*Feature Engineering*) para identificar viajeros solitarios vs. familias.
* **Resultados:** Empaquetado de predicciones con un acierto empírico del **77.27%** en el *Leaderboard* público de Kaggle.

---

# Stack Tecnológico Base
* **Lenguajes:** Python, R, SQL.
* **Ingeniería & Análisis:** Pandas, Scikit-Learn, BeautifulSoup, Requests.
* **Bases de Datos & Entornos:** MySQL, SQLite, GitHub, Visual Studio Code.