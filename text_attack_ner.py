"""
text_attack_ner.py

Performs adversarial attacks on a Named Entity Recognition (NER) model used for real estate document parsing.
"""

import spacy
import random

# Load pre-trained NER model
nlp = spacy.load("en_core_web_sm")

def perturb_text(text):
    """
    Apply simple character-level perturbation to named entities.
    Example: 'Tenant' -> 'Tennant', 'Buyer' -> 'Buy3r'
    """
    replacements = {'a': '@', 'e': '3', 'i': '1', 'o': '0', 'u': 'v'}
    words = text.split()
    perturbed = []

    for word in words:
        if word.istitle():
            perturbed_word = ''.join([replacements.get(c.lower(), c) for c in word])
            perturbed.append(perturbed_word)
        else:
            perturbed.append(word)

    return ' '.join(perturbed)

def attack_document(text):
    """
    Perform an attack by identifying entities and perturbing them.
    """
    doc = nlp(text)
    print("Original Entities:")
    for ent in doc.ents:
        print(f"{ent.text} -> {ent.label_}")

    attacked_text = perturb_text(text)
    attacked_doc = nlp(attacked_text)

    print("\nAttacked Text Entities:")
    for ent in attacked_doc.ents:
        print(f"{ent.text} -> {ent.label_}")

    return attacked_text

# Sample usage
if __name__ == "__main__":
    sample_text = "John Doe is the Buyer and Jane Smith is the Tenant in the lease agreement."
    attacked = attack_document(sample_text)
    print("\nAttacked Text:", attacked)
