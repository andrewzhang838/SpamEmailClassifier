# Spam Email Classifier

This project implements a Spam Email Classifier using Natural Language Processing (NLP) with the Bag of Words model and Binary Search Trees (BSTs). The classifier categorizes emails as either spam or ham (not spam) based on word occurrences.

Binary Search Tree for Word Storage:
Words from spam and ham emails are stored in separate BSTs.
Each word's frequency is tracked, enabling efficient classification.

Natural Language Processing (Bag of Words):
Text preprocessing includes lowercasing and punctuation removal.
Words from emails are tokenized and counted.

Training Phase:
Reads emails and their labels (spam or ham) from a dataset.
Inserts words into the respective spam or ham BST, tracking word frequencies.

Testing Phase:
Processes a new email and calculates a spam score and a ham score.
Compares word occurrences in the spam and ham BSTs to classify the email.
