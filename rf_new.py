import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib

# Step 1: Load the dataset
dataset = pd.read_csv("synthesized_heart_rates.csv")

# Step 2: Preprocess the data (if needed)
# For simplicity, assuming there are no missing values and all features are numerical.

# Step 3: Split the dataset into features (X) and labels (y)
X = dataset[['MEAN_RR', 'MEDIAN_RR', 'SDRR', 'pNN25', 'pNN50', 'HR']]
y = dataset['condition']

# Step 4: Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.17, random_state=42)

# Step 5: Choose a classification model and train it
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Step 6: Evaluate the model
y_pred = clf.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))
joblib.dump(clf, 'random_forest_model.pkl')

# Step 7: Tune hyperparameters (optional)

# Step 8: Make predictions (if needed)
