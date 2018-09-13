import pandas as pd
from sklearn.neural_network import MLPClassifier
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn import linear_model as lm
import numpy as np
from titanic.util import encode_label, fill_na


train_df = pd.read_csv('data/train.csv')
test_df = pd.read_csv('data/test.csv')

fill_na(train_df, test_df, 'Fare', train_df["Fare"].median())
fill_na(train_df, test_df, 'Age', train_df["Age"].median())
fill_na(train_df, test_df, 'Embarked', 'S')

encode_label(train_df, test_df, 'Sex', 'SexE')
encode_label(train_df, test_df, 'Embarked', 'EmbarkedE')


feature_classes = ["Pclass", "SibSp", "Parch", "Fare", 'SexE', 'Age', 'EmbarkedE']
train_X = train_df[feature_classes]
train_y = train_df["Survived"]
test_X = test_df[feature_classes]


X_train, X_test, y_train, y_test = train_test_split(train_X, train_y, test_size=0.33, random_state=42)
# clf = MLPClassifier(solver='adam',
#                     alpha=1e-5,
#                     hidden_layer_sizes=(100, 8),
#                     random_state=1,
#                     activation='tanh',
#                     learning_rate='adaptive')
clf = RandomForestClassifier(max_depth= 2, random_state=0)
# clf = lm.LogisticRegression()


clf.fit(X_train, y_train)
val_preds = clf.predict(X_test)

print(accuracy_score(y_test, val_preds))

test_df['Survived'] = clf.predict(test_X)
test_df[['PassengerId', 'Survived']].to_csv('data/result.csv', index=False)


