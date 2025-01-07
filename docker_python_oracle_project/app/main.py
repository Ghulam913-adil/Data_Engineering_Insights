import oracledb
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import pandas as pd

# Oracle Database Connection and Helper Functions
# ------------------------------------------------

def connect_to_oracle():
    """
    Establish a connection to the Oracle database using Thin mode.
    """
    oracledb.init_oracle_client(lib_dir=None)  # Disable the need for the client libraries
    conn = oracledb.connect(
        user="hr",
        password="hr",
        dsn="localhost:1521/orclpdb",
        mode=oracledb.DEFAULT_AUTH
    )
    return conn

# # Model Training and Evaluation
# # -----------------------------
# def train_model():
#     """
#     Load dataset, train a machine learning model, and generate a classification report.
#     """
#     data = load_iris()
#     X, y = data.data, data.target
#     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

#     model = RandomForestClassifier(random_state=42)
#     model.fit(X_train, y_train)
#     y_pred = model.predict(X_test)

#     report = classification_report(y_test, y_pred, output_dict=True)
#     report_df = pd.DataFrame(report).transpose()

#     return report_df


# # Insert Report into Database
# # ---------------------------
# def insert_report_into_db(report_df):
#     """
#     Insert the classification report into the Oracle database.
#     """
#     conn = connect_to_oracle()
#     cursor = conn.cursor()

#     for index, row in report_df.iterrows():
#         if index not in ['accuracy', 'macro avg', 'weighted avg']:
#             cursor.execute("""
#             INSERT INTO classification_report (model_name, precision, recall, f1_score, support)
#             VALUES (:model_name, :precision, :recall, :f1_score, :support)
#             """, {
#                 'model_name': 'RandomForest',
#                 'precision': row['precision'],
#                 'recall': row['recall'],
#                 'f1_score': row['f1-score'],
#                 'support': row['support']
#             })
#     conn.commit()
#     cursor.close()
#     conn.close()

# # Main Script
# # -----------
# if __name__ == "__main__":

#     print("Training the model and generating the classification report...")
#     report_df = train_model()

#     print("Inserting the classification report into the Oracle database...")
#     insert_report_into_db(report_df)

#     print("Classification report has been successfully saved to the database.")
