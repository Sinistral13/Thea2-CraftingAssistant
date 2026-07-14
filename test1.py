import psycopg2

try:
    conn = psycopg2.connect(
        host="localhost",
        database="thea_mat",
        user="postgres",
        password="J383170#tp99!",
        port=5432
    )
    print("CONNECTED")
    
except Exception as e:
    print(type(e))
    print(repr(e))