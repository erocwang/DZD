import sqlite3 

def create_connection(db_file): 
    conn = None
    try: 
        conn = sqlite3.connect(db_file)
        # conn = sqlite3.connect(':memory:')
        print(sqlite3.version)
    except Error as e: 
        print(e)
    return conn

def create_table(conn, create_table_sql):
    try: 
        cur = conn.cursor() 
        cur.execute(create_table_sql)
    except Error as e:
        print(e)

def create_kmer(conn, kmer): 
    sql = """ INSERT INTO kmer(kmer,count)
              VALUES(?,?) """
    cur = conn.cursor() 
    cur.execute(sql, kmer)
    conn.commit() 
    return cur.lastrowid



source_file = "SP1.fastq"
kmers = {}
with open(source_file,'r') as f:
    line_num = -1 # offset by 1 for sequence line
    for line in f:         
        if line_num%4 == 0: 
            line = line.strip()
            if(len(line) >= 21):
                kmers[line] = len(line) - 20 
            else: 
                kmers[line] = 0
        line_num += 1

print(len(kmers))

conn = create_connection(r"data.db")

sql_create_kmer_table = """ CREATE TABLE IF NOT EXISTS kmer (
                                kmer text, 
                                count integer
                        ); """ 

if conn is not None: 
    create_table(conn, sql_create_kmer_table)
    for kmer in kmers:
        to_Add = (kmer, kmers[kmer])
        #create_kmer(conn, to_Add)
    conn.close()
else: 
    print("Error! cannot create database connection")