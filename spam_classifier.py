import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline
import pickle


data = pd.read_csv('dataset/email_spam.csv')


X = data['text']
y = data['spam']


model = Pipeline([
    ('vectorizer', TfidfVectorizer(stop_words='english', lowercase=True, ngram_range=(1, 2))),
    ('classifier', LinearSVC(class_weight='balanced', max_iter=10000))
])

print("Training started...")
model.fit(X, y)
print("Model trained successfully!")

with open('saved_model/spam_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model saved at saved_model/spam_model.pkl")
