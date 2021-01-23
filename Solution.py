import sqlite3 

def create_connection(db_file): 
    conn = None
    try: 
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e: 
        print(e)
    finally: 
        return conn



source_file = "SP1.fastq"
k_mers = {}
with open(source_file,'r') as f:
    line_num = -1 # offset by 1 for sequence line
    for line in f:         
        if line_num%4 == 0: 
            line = line.strip()
            if(len(line) >= 21):
                k_mers[line] = len(line) - 20 
            else: 
                k_mers[line] = 0
        line_num += 1

print(len(k_mers))

create_connection(r"data.db")