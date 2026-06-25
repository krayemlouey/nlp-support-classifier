





<img width="1917" height="768" alt="Capture d&#39;écran 2026-06-25 081239" src="https://github.com/user-attachments/assets/eaf72f71-0640-49f7-9a6d-69428e172a19" />
<img width="1919" height="804" alt="Capture d&#39;écran 2026-06-25 081228" src="https://github.com/user-attachments/assets/e8663967-94dd-43a8-860f-fc87b5882df0" />
<img width="1904" height="758" alt="Capture d&#39;écran 2026-06-25 081216" src="https://github.com/user-attachments/assets/f214a01a-6b52-488b-b478-6d548c75bd7d" />
<img width="1917" height="800" alt="Capture d&#39;écran 2026-06-25 081345" src="https://github.com/user-attachments/assets/669d2d3e-9103-41f2-9fa4-588925a72278" />
<img width="1918" height="744" alt="Capture d&#39;écran 2026-06-25 081329" src="https://github.com/user-attachments/assets/95d7a9a0-a085-433a-ab8d-8000fc81bb7e" />



# NLP Support Classifier 

Un système de classification automatique de messages clients basé sur un modèle Transformer fine-tuné (DistilBERT), avec une interface web Streamlit et une API REST FastAPI.

## Fonctionnalités


- **Classification en 6 catégories** :
  -  Remboursement
  -  Problème technique
  -  Positif
  -  Livraison
  -  Achat / Commande
  -  Autre
- **Interface client** (Streamlit) pour soumettre des messages
- **Espace RH** pour visualiser les messages classés
- **API REST** (FastAPI) pour intégrer la prédiction dans d'autres systèmes

## Stack Technique

| Composant | Technologie |
|:---|:---|
| Modèle NLP | `distilbert-base-uncased` (Hugging Face Transformers) |
| Fine-tuning | PyTorch + Hugging Face `Trainer` |
| Métriques | Accuracy & F1-score (pondéré) |
| Interface Web | Streamlit |
| API REST | FastAPI + Uvicorn |
| Stockage | JSON (data_store.py) |

## Installation

```bash
# 1. Cloner le dépôt
git clone https://github.com/<votre-username>/nlp-support-classifier.git
cd nlp-support-classifier

# 2. Créer et activer l'environnement virtuel
python -m venv venv
venv\Scripts\Activate.ps1   # Windows PowerShell

# 3. Installer les dépendances
pip install -r requirements.txt
```

## Entraînement du Modèle

> Le fichier des poids du modèle (`model.safetensors`) est trop volumineux pour GitHub.
> Vous devez relancer l'entraînement après le clonage.

```bash
python train.py
```

L'entraînement dure environ **2-3 minutes** sur CPU. Le modèle est sauvegardé automatiquement dans le dossier `./model`.

## Lancement

### Interface Streamlit (Client + RH)
```bash
streamlit run app.py
```
Ouvre automatiquement `http://localhost:8501`

### API FastAPI
```bash
uvicorn app.main:app --reload
```
Documentation interactive disponible sur `http://localhost:8000/docs`

## Exemple d'utilisation de l'API

```bash
curl -X POST "http://localhost:8000/predict" \
     -H "Content-Type: application/json" \
     -d '{"text": "Je n'\''ai pas reçu mon colis"}'
```

**Réponse :**
```json
{
  "input": "Je n'ai pas reçu mon colis",
  "prediction": "livraison"
}
```

## Structure du Projet

```
nlp-support-classifier/
├── app.py                  # Page principale Streamlit (client)
├── train.py                # Script d'entraînement + évaluation (Accuracy, F1)
├── data.py                 # Données d'entraînement labellisées
├── data_store.py           # Persistence des messages (JSON)
├── requirements.txt        # Dépendances Python
├── app/
│   ├── main.py             # API FastAPI
├── core/
│   └── predict.py          # Pipeline de prédiction
├── pages/
│   ├── Employe.py          # Interface employé (Streamlit)
│   └── RH.py               # Boîte de réception RH (Streamlit)
└── model/                  # Dossier du modèle fine-tuné (non versionné)
    ├── config.json
    ├── tokenizer.json
    └── tokenizer_config.json
```

## Métriques d'Évaluation

Le pipeline d'entraînement (`train.py`) calcule à chaque époque :
- **Accuracy** : Taux de prédictions correctes sur le jeu de validation.
- **F1-score (pondéré)** : Mesure équilibrée prenant en compte toutes les catégories.

Le meilleur modèle (selon le F1-score) est automatiquement sauvegardé.
