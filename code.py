import string
import pandas as pd
from collections import Counter

class BSTNode:
    def __init__(self, word, count=1):
        self.word = word
        self.count = count
        self.left = None
        self.right = None

    def insert(self, word):
        if word == self.word:
            self.count += 1
        elif word < self.word:
            if self.left is None:
                self.left = BSTNode(word)
            else:
                self.left.insert(word)
        else:
            if self.right is None:
                self.right = BSTNode(word)
            else:
                self.right.insert(word)

    def search(self, word):
        if word == self.word:
            return self.count
        elif word < self.word and self.left is not None:
            return self.left.search(word)
        elif word > self.word and self.right is not None:
            return self.right.search(word)
        return 0

class SpamClassifier:
    def __init__(self):
        self.spam_tree = None
        self.ham_tree = None
        self.spam_count = 0
        self.ham_count = 0

    def preprocess(self, text):
        text = text.lower().translate(str.maketrans('', '', string.punctuation))
        words = text.split()
        return words

    def train(self, emails, labels):
        for email, label in zip(emails, labels):
            words = self.preprocess(email)
            if label == 'spam':
                self.spam_count += 1
                for word in words:
                    if self.spam_tree is None:
                        self.spam_tree = BSTNode(word)
                    else:
                        self.spam_tree.insert(word)
            else:
                self.ham_count += 1
                for word in words:
                    if self.ham_tree is None:
                        self.ham_tree = BSTNode(word)
                    else:
                        self.ham_tree.insert(word)

    def predict(self, email):
        words = self.preprocess(email)
        spam_score = 0
        ham_score = 0
        
        for word in words:
            if self.spam_tree:
                spam_score += self.spam_tree.search(word)
            if self.ham_tree:
                ham_score += self.ham_tree.search(word)

        if spam_score > ham_score:
            return 'spam'
        else:
            return 'ham'

# Load dataset
def load_data(file_path):
    df = pd.read_csv(file_path)
    emails = df['text'].tolist()
    labels = df['label'].tolist()
    return emails, labels

# Example usage
file_path = 'spam_dataset.csv'
emails, labels = load_data(file_path)

classifier = SpamClassifier()
classifier.train(emails, labels)

# Test prediction
test_email = "Get your free prize today by clicking this link!"
print(f'Test Email: {test_email}\nPrediction: {classifier.predict(test_email)}')
