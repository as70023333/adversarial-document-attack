# Adversarial Document Attack

**Adversarial attacks on NLP models used in real estate document processing.**  
This project simulates how lease or title agreements can be subtly manipulated to bypass Named Entity Recognition (NER) models. It includes:

- Character-level perturbation (e.g. “Tenant” → “Tennant”)
- PDF injection strategies (planned)
- Detection before and after attack
- Evaluation using spaCy NER

Built to explore security risks in PropTech and inspire defense mechanisms.
## Features
- Uses spaCy NER model
- Character-level perturbation to fool entity recognition
- Displays before/after entity detection


## Run
```bash
python text_attack_ner.py
```

## Requirements
- spacy
- en_core_web_sm
