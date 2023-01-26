import codecademylib3_seaborn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load the passenger data
passengers = pd.read_csv("passengers.csv")

# Update sex column to numerical
passengers["Sex"] = passengers["Sex"].map({'male':0, 'female':1})

# Fill the nan values in the age column
passengers["Age"].fillna(inplace=True, value=passengers["Age"].mean())

# Create a first class column
passengers["FirstClass"] = passengers["Pclass"].apply(lambda p: 1 if p == 1 else 0)

# Create a second class column
passengers["SecondClass"] = passengers["Pclass"].apply(lambda p:1 if p == 2 else 0)

# Select the desired features
features = passengers[["Sex", "Age", "FirstClass", "SecondClass"]]
survival = passengers[["Survived"]]

# Perform train, test, split
train_features, test_features, train_labels, test_labels = train_test_split(features, survival, train_size=0.8)

# Scale the feature data so it has mean = 0 and standard deviation = 1
scaler = StandardScaler()
train_features = scaler.fit_transform(train_features)
test_features = scaler.transform(test_features)

# Create and train the model
cc_lr = LogisticRegression()
cc_lr.fit(train_features, train_labels)

# Score the model on the train data
print(cc_lr.score(train_features, train_labels))

# Score the model on the test data
print(cc_lr.score(test_features, test_labels))

# Analyze the coefficients
print(cc_lr.coef_)

# Sample passenger features
Jack = np.array([0.0,20.0,0.0,0.0])
Rose = np.array([1.0,17.0,1.0,0.0])
You = np.array([1.0,22.0,0.0,1.0])

# Combine passenger arrays
sample_passengers = np.array([Jack, Rose, You])

# Scale the sample passenger features
sample_passengers = scaler.transform(sample_passengers)
print(sample_passengers)

# Make survival predictions!
print(cc_lr.predict(sample_passengers))
print(cc_lr.predict_proba(sample_passengers))
