# code for connection, database/table/entry creation, and fetching 
import sqlite3 
from sqlite3 import Error 

# returns a map of kmers to their 21-mer counts
def read_fastq(source_file): 
    kmers = {}
    with open(source_file,'r') as f:
        lines = f.readlines()[1::4]
        for line in lines:         
                line = line.strip()
                count = 0
                for i in range(21,len(line)+1):
                    if line[i-21:i] in kmers: 
                        kmers[line[i-21:i]] += 1
                    else:
                        kmers[line[i-21:i]] = 1
    return kmers

# returns a connection to the specified database if valid
def create_connection(db_file): 
    conn = None
    try: 
        conn = sqlite3.connect(db_file)
    except Error as e: 
        print(e)
    return conn

# creates a kmer table with given connection path
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

# inserts a new entry into the kmer table if valid 
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

# returns all kmers in the kmer table from specified connection
def select_all_seqs(conn):
    cur = conn.cursor()
    rows = [row[0] for row in cur.execute("SELECT kmer FROM kmer")]
    return rows
