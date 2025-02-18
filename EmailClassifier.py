#pip install scikit-learn pandas nltk
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

# Sample email dataset
data = {
    "text": [
        "Win a free iPhone now!",
        "Your invoice for last month is attached.",
        "Claim your lottery prize today.",
        "Meeting at 3 PM with the team.",
        "Discount on all products for today only!",
        "Project deadline extended, check email.",
    ],
    "label": [1, 0, 1, 0, 1, 0]  # 1 = Spam, 0 = Important
}

df = pd.DataFrame(data)

# Text preprocessing
vectorizer = TfidfVectorizer(stop_words=stopwords.words("english"))
X = vectorizer.fit_transform(df["text"])
y = df["label"]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train model
model = MultinomialNB()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

# Test on new email
new_email = ["Congratulations! You won a free vacation."]
new_vector = vectorizer.transform(new_email)
print("Prediction:", "Spam" if model.predict(new_vector)[0] == 1 else "Important")
