<h1 align="center">El Mehdi Ribahi</h1>

<p align="center">
  Élève-ingénieur en Intelligence Artificielle &amp; Data · Casablanca
</p>

<p align="center">
  <a href="https://linkedin.com/in/el-mehdi-ribahi"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn"></a>
  <a href="mailto:elmehdi.ribahi@gmail.com"><img src="https://img.shields.io/badge/elmehdi.ribahi@gmail.com-EA4335?style=flat-square&logo=gmail&logoColor=white" alt="Email"></a>
  <img src="https://img.shields.io/badge/Casablanca-Maroc-424242?style=flat-square&logo=googlemaps&logoColor=white" alt="Casablanca, Maroc">
</p>

<hr>

## Profil

4ᵉ année du cycle **Ingénieur d'État en Informatique & Réseaux**, spécialité **Intelligence Artificielle & Data** — EMSI Casablanca, promotion 2028.

Une alerte de fraude qui ne dit pas *pourquoi* est inutilisable par un analyste. Un contrôle de conformité qui ne trace pas sa décision est irrecevable par un auditeur. Un moteur de recherche qu'on n'évalue pas face à une baseline est une affirmation, pas un résultat.

C'est le fil conducteur de mon travail : **construire des systèmes d'IA dont chaque décision peut être expliquée et auditée.**

**Actuellement à la recherche d'un stage en IA / Data à Casablanca.**

<hr>

## Projets principaux

### [NovaBank](https://github.com/ribahi-dev/NovaBank) — Détection de fraude bancaire explicable

<p align="center">
  <img src="https://raw.githubusercontent.com/ribahi-dev/NovaBank/main/docs/screenshots/02-fraude-shap.png" alt="Détection de fraude : alerte, score de risque, explication en langage naturel et contribution SHAP de chaque variable" width="800">
</p>

Plateforme d'aide à la décision pour agence bancaire. Le modèle ne renvoie pas seulement un score de risque : **SHAP décompose la contribution de chaque variable**, le conseiller lit l'explication en langage naturel, et sa décision est réinjectée dans le modèle par une boucle de feedback.

Sécurité de bout en bout : authentification JWT, contrôle d'accès par rôles, journal d'audit. Déploiement en une commande via Docker Compose, intégration continue sur chaque push.

> Réalisé dans le cadre de mon stage chez **Attijariwafa Bank**.

**FastAPI · scikit-learn · SHAP · PostgreSQL · Alembic · React · Docker · GitHub Actions**

<br>

### [Recherche sémantique multilingue](https://github.com/ribahi-dev/recherche-semantique-multilingue) — FR · AR · EN

Moteur qui retrouve un article scientifique anglophone à partir d'une question posée en français, en arabe ou en anglais.

```
Corpus     8 520 articles arXiv, intégralement en anglais

Requête    كشف الاحتيال المصرفي باستخدام التعلم الآلي
           « détection de la fraude bancaire par apprentissage automatique »

Résultat   Shapley Value-Guided Adaptive Ensemble Learning for Explainable
           Financial Fraud Detection                           score  0,837

Baseline   aucun résultat — sur cette requête et sur les 19 autres
```

La question et le titre retrouvé ne partagent aucun caractère : pas même l'alphabet. Là où une recherche par mots-clés est structurellement incapable de répondre, la recherche vectorielle rapproche les sens plutôt que les chaînes.

Le dépôt contient le protocole d'évaluation complet et régénérable, pas uniquement le code.

**Python · embeddings multilingues · index vectoriel · NLP**

<br>

### [Agent de conformité KYC](https://github.com/ribahi-dev/agent-conformite-kyc) — Le modèle lit, les règles décident

Agent qui analyse une pièce justificative et rend un verdict motivé — **VALIDÉ, REJETÉ ou À VÉRIFIER** — avec la trace de chaque contrôle effectué.

Le modèle de langage extrait l'information : nom, dates, émetteur. Le code Python applique les règles métier et tranche. Le modèle ne juge jamais de la conformité lui-même.

| | Si le modèle décide | Si les règles décident |
|---|---|---|
| **Reproductibilité** | la même pièce peut varier | même entrée, même verdict |
| **Auditabilité** | « le modèle a estimé que… » | règle des 3 mois, `config.py:16` |
| **Modifier un seuil** | réécrire et retester un prompt | changer une constante |

**Python · LLM · moteur de règles métier · KYC / LBC-FT**

<hr>

## Autres projets

| Projet | Description | Stack |
|---|---|---|
| [stagematch-ai](https://github.com/ribahi-dev/stagematch-ai) | Recommandation de stages : analyse automatique du CV, matching NLP avec scoring explicable, scraping des offres marocaines | Django REST · React/TS · NLP |
| [emsi-booking](https://github.com/ribahi-dev/emsi-booking) | Réservation de salles : détection de conflits d'horaires, workflow de validation, Google OAuth, calendrier interactif | Django 5 · DRF · PostgreSQL |
| [StockFlow](https://github.com/ribahi-dev/StockFlow) | ERP et point de vente pour PME : stock en temps réel, facturation, suivi des dépenses et bénéfice net | React · TypeScript · Vite |
| [carepal](https://github.com/ribahi-dev/carepal) | Compagnon hybride matériel/logiciel de bien-être étudiant pendant les sessions de révision | JavaScript · IoT |

<hr>

## Compétences techniques

| | |
|---|---|
| **Langages** | Python · TypeScript · JavaScript · SQL |
| **IA & Data** | scikit-learn · pandas · NumPy · SHAP · NLP · RAG |
| **Backend** | FastAPI · Django / DRF · PostgreSQL · SQLAlchemy · REST · JWT |
| **Frontend** | React · Next.js · TypeScript · Tailwind CSS |
| **Outils** | Docker · Git · GitHub Actions · Linux · PlantUML |

<hr>

## Engagement associatif

Vice-président du bureau des étudiants et président du club de lecture de l'EMSI : organisation d'événements, animation de sessions et coordination d'équipe.

<hr>

<p align="center">
  <img height="160" src="https://github-readme-stats.vercel.app/api?username=ribahi-dev&show_icons=true&hide_border=true&theme=graywhite&include_all_commits=true&count_private=true&hide=issues" alt="Statistiques GitHub">
  <img height="160" src="https://github-readme-stats.vercel.app/api/top-langs/?username=ribahi-dev&layout=compact&hide_border=true&theme=graywhite&langs_count=8" alt="Langages les plus utilisés">
</p>

<p align="center">
  <b>Ouvert aux opportunités de stage et aux collaborations sur des projets IA / Data</b><br>
  <a href="mailto:elmehdi.ribahi@gmail.com">elmehdi.ribahi@gmail.com</a> · <a href="https://linkedin.com/in/el-mehdi-ribahi">LinkedIn</a>
</p>
