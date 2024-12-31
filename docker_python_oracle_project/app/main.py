# Complete Project: Dataset Analysis and Oracle Database Integration
# ---------------------------------------------------------------
# This script orchestrates the process of training a machine learning model,
# generating a classification report, and saving it into an Oracle database.

import cx_Oracle
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import pandas as pd


# Oracle Database Connection and Helper Functions
# ------------------------------------------------
def connect_to_oracle():
    """
    Establish a connection to the Oracle database.
    """
    conn = cx_Oracle.connect(
        user="hr",
        password="hr",
        dsn="localhost:1521/orclpdb"
    )
    return conn

# Model Training and Evaluation
# -----------------------------
def train_model():
    """
    Load dataset, train a machine learning model, and generate a classification report.
    """
    data = load_iris()
    X, y = data.data, data.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    report = classification_report(y_test, y_pred, output_dict=True)
    report_df = pd.DataFrame(report).transpose()

    return report


# Insert Report into Database
# ---------------------------
def insert_report_into_db(report_df):
    """
    Insert the classification report into the Oracle database.
    """
    conn = connect_to_oracle()
    cursor = conn.cursor()

    for index, row in report_df.iterrows():
        if index not in ['accuracy', 'macro avg', 'weighted avg']:
            cursor.execute("""
            INSERT INTO classification_report (model_name, accuracy, precision, recall, f1_score, support)
            VALUES (:model_name, :accuracy, :precision, :recall, :f1_score, :support)
            """, {
                'model_name': 'RandomForest',
                'accuracy': report_df.loc['accuracy', 'f1-score'],
                'precision': row['precision'],
                'recall': row['recall'],
                'f1_score': row['f1-score'],
                'support': row['support']
            })
    conn.commit()
    cursor.close()
    conn.close()


# Main Script
# -----------
if __name__ == "__main__":
    
    print("Training the model and generating the classification report...")
    report_df = train_model()
    
    print("Inserting the classification report into the Oracle database...")
    insert_report_into_db(report_df)
    
    print("Classification report has been successfully saved to the database.")
