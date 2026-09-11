<p align="center">
  <img src="./profile.svg" alt="elmehdi@ribahi-dev" width="820">
</p>

<h3 align="center">Je construis des systèmes d'IA dont chaque décision peut être expliquée.</h3>

<p align="center">
  <a href="https://linkedin.com/in/el-mehdi-ribahi"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"></a>
  <a href="mailto:elmehdi.ribahi@gmail.com"><img src="https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"></a>
  <img src="https://img.shields.io/badge/Casablanca-Maroc-2E7D32?style=for-the-badge" alt="Casablanca, Maroc">
  <img src="https://komarev.com/ghpvc/?username=ribahi-dev&style=for-the-badge&color=6366F1&label=VUES" alt="Vues du profil">
</p>

---

```
4ᵉ année  ·  Ingénieur d'État en Informatique & Réseaux  ·  spécialité IA & Data
EMSI Casablanca  ·  promotion 2028
```

Une alerte de fraude qui ne dit pas *pourquoi* est inutilisable par un analyste. Un agent de
conformité qui ne trace pas ses décisions est irrecevable par un auditeur. Un moteur de recherche
qu'on n'évalue pas face à une baseline est une affirmation, pas un résultat.

C'est le fil rouge de ce que je construis : **de l'IA qui rend des comptes.**

<br>

<div align="center">
  <b>Disponible pour un stage en IA / Data · Casablanca</b>
</div>

---

# Projets principaux

## 🏦 [novabank](https://github.com/ribahi-dev/novabank)
### Détection de fraude bancaire explicable

<!-- Remplace ce chemin si ta capture est ailleurs, ou mets un GIF de démo -->
<p align="center">
  <img src="https://raw.githubusercontent.com/ribahi-dev/novabank/main/docs/screenshots/02-fraude-shap.png" alt="Page de détection de fraude : alerte, score IA, explication en langage naturel et graphique SHAP" width="780">
</p>

Plateforme d'aide à la décision pour agence bancaire. Le modèle ne renvoie pas qu'un score de
risque : **SHAP décompose la contribution de chaque variable**, le conseiller lit l'explication en
langage naturel, et sa décision est réinjectée dans le modèle par une boucle de feedback.

Sécurité de bout en bout — JWT, contrôle d'accès par rôles, journal d'audit. Démarrage en une
commande via Docker Compose, intégration continue sur chaque push.

<sub>**Stack** · FastAPI · scikit-learn · SHAP · PostgreSQL · Alembic · React 18 · Docker · GitHub Actions</sub>
<br><sub>🎓 Réalisé pendant mon stage chez <b>Attijariwafa Bank</b>.</sub>

<br>

## 🔎 [recherche-semantique-multilingue](https://github.com/ribahi-dev/recherche-semantique-multilingue)
### Poser la question en arabe, trouver l'article en anglais

```
Corpus    8 520 articles arXiv, intégralement en anglais

Requête   كشف الاحتيال المصرفي باستخدام التعلم الآلي
          « détection de la fraude bancaire par apprentissage automatique »

Résultat  Shapley Value-Guided Adaptive Ensemble Learning for Explainable
          Financial Fraud Detection                            score 0,837

Baseline  aucun résultat — sur cette requête et sur les 19 autres
```

La question et le titre trouvé ne partagent **aucun caractère** : pas même l'alphabet. Là où une
recherche par mots-clés est structurellement incapable de répondre, la recherche vectorielle
rapproche les sens plutôt que les chaînes.

Le dépôt contient le protocole d'évaluation complet et régénérable, pas seulement le code.

<sub>**Stack** · Python · embeddings multilingues · index vectoriel · NLP</sub>

<br>

## ⚖️ [agent-conformite-kyc](https://github.com/ribahi-dev/agent-conformite-kyc)
### Le LLM lit. Les règles décident.

Agent qui analyse une pièce justificative (CIN, justificatif de domicile) et rend un verdict motivé :
**VALIDÉ · REJETÉ · À VÉRIFIER**, avec la trace de chaque contrôle.

Le modèle de langage extrait l'information — nom, dates, émetteur. Le code Python applique les règles
et tranche. Le LLM ne juge **jamais** de la conformité lui-même.

|  | Si le LLM décide | Si les règles décident |
|---|---|---|
| **Reproductibilité** | la même pièce peut varier | même entrée → même verdict |
| **Auditabilité** | « le modèle a estimé que… » | `règle des 3 mois · config.py:16` |
| **Changer un seuil** | réécrire et retester un prompt | changer une constante |

<sub>**Stack** · Python · LLM · moteur de règles métier · KYC / LBC-FT</sub>

---

# Autres projets

<table>
<tr>
<td width="50%" valign="top">

### [stagematch-ai](https://github.com/ribahi-dev/stagematch-ai)
Recommandation de stages : analyse automatique du CV, matching NLP avec scoring explicable, scraping des offres marocaines.
<br><sub><code>Django REST</code> <code>React/TS</code> <code>NLP</code></sub>

</td>
<td width="50%" valign="top">

### [emsi-booking](https://github.com/ribahi-dev/emsi-booking)
Réservation de salles : algorithme de détection de conflits, workflow de validation, Google OAuth, calendrier interactif.
<br><sub><code>Django 5</code> <code>DRF</code> <code>PostgreSQL</code></sub>

</td>
</tr>
<tr>
<td width="50%" valign="top">

### [StockFlow](https://github.com/ribahi-dev/StockFlow)
ERP et point de vente pour PME : stock en temps réel, facturation, suivi des dépenses, bénéfice net calculé automatiquement.
<br><sub><code>React</code> <code>TypeScript</code> <code>Vite</code> <code>Tailwind</code></sub>

</td>
<td width="50%" valign="top">

### [carepal](https://github.com/ribahi-dev/carepal)
Compagnon hybride matériel/logiciel de bien-être étudiant pendant les sessions de révision.
<br><sub><code>JavaScript</code> <code>IoT</code></sub>

</td>
</tr>
</table>

---

# Stack

<table>
<tr><td><b>Langages</b></td><td>

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)
![SQL](https://img.shields.io/badge/SQL-4479A1?style=flat-square&logo=postgresql&logoColor=white)

</td></tr>
<tr><td><b>IA & Data</b></td><td>

![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikitlearn&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-150458?style=flat-square&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white)
![SHAP](https://img.shields.io/badge/SHAP-8B5CF6?style=flat-square)
![NLP RAG](https://img.shields.io/badge/NLP%20%C2%B7%20RAG-0EA5E9?style=flat-square)

</td></tr>
<tr><td><b>Backend</b></td><td>

![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=flat-square&logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=flat-square&logo=sqlalchemy&logoColor=white)

</td></tr>
<tr><td><b>Frontend</b></td><td>

![React](https://img.shields.io/badge/React-61DAFB?style=flat-square&logo=react&logoColor=black)
![Next.js](https://img.shields.io/badge/Next.js-000000?style=flat-square&logo=nextdotjs&logoColor=white)
![Tailwind](https://img.shields.io/badge/Tailwind-06B6D4?style=flat-square&logo=tailwindcss&logoColor=white)

</td></tr>
<tr><td><b>Outils</b></td><td>

![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black)

</td></tr>
</table>

---

# En dehors du code

**Vice-président du bureau des étudiants** et **président du club de lecture** de l'EMSI.
J'organise, j'anime, et je lis beaucoup trop.

---

<div align="center">

<img height="165" src="https://github-readme-stats.vercel.app/api?username=ribahi-dev&show_icons=true&hide_border=true&theme=github_dark&include_all_commits=true&count_private=true&hide=issues" alt="Statistiques GitHub">
<img height="165" src="https://github-readme-stats.vercel.app/api/top-langs/?username=ribahi-dev&layout=compact&hide_border=true&theme=github_dark&langs_count=8" alt="Langages les plus utilisés">

<br><br>

### Parlons-en

Stage IA / Data · collaboration sur un projet · ou juste une question sur un dépôt

[**elmehdi.ribahi@gmail.com**](mailto:elmehdi.ribahi@gmail.com) · [**LinkedIn**](https://linkedin.com/in/el-mehdi-ribahi)

</div>
