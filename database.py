import sqlite3 
from sqlite3 import Error 

def create_connection(db_file): 
    conn = None
    try: 
        conn = sqlite3.connect(db_file)
    except Error as e: 
        print(e)
    return conn

def create_kmer_table(conn):
    try: 
        cur = conn.cursor() 
        cur.execute("DROP TABLE IF EXISTS kmer")
        create_table_sql = """ CREATE TABLE IF NOT EXISTS kmer (
                                kmer text, 
                                count integer
                        ); """ 
        cur.execute(create_table_sql)
    except Error as e:
        print(e)

def create_kmer(conn, kmer): 
    try:
        sql = """ INSERT INTO kmer(kmer,count)
                    VALUES(?,?) """
        cur = conn.cursor() 
        cur.execute(sql, kmer)
        conn.commit() 
    except Error as e: 
        print(e)
    return cur.lastrowid

def select_all_seqs(conn):
    cur = conn.cursor()
    rows = [row[0] for row in cur.execute("SELECT kmer FROM kmer")]
    return rows
