from db_connection import connect_to_oracle

def insert_dummy_data():
    """
    Insert dummy data into the Oracle database.
    """
    conn = connect_to_oracle()
    if conn:
        try:
            cursor = conn.cursor()

            # Insert dummy data
            dummy_data = [
                ("John Doe", 30, "johndoe@example.com"),
                ("Jane Smith", 25, "janesmith@example.com"),
                ("Emily Davis", 35, "emilydavis@example.com")
            ]
            cursor.executemany(
                "INSERT INTO DummyData (Name, Age, Email) VALUES (:1, :2, :3)",
                dummy_data
            )
            conn.commit()
            print("Dummy data inserted successfully!")
        except cx_Oracle.DatabaseError as e:
            print(f"Error inserting data: {e}")
        finally:
            conn.close()

if __name__ == "__main__":
    insert_dummy_data()
