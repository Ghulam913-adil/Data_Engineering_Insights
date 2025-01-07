import cx_Oracle

def connect_to_oracle():
    """
    Establish a connection to the Oracle database.
    """
    dsn = cx_Oracle.makedsn("host.docker.internal", 1521, service_name="orclpdb")
    try:
        conn = cx_Oracle.connect(user="hr", password="hr", dsn=dsn)
        print("Connection successful!")
        return conn
    except cx_Oracle.DatabaseError as e:
        print(f"Error connecting to Oracle database: {e}")
        return None
