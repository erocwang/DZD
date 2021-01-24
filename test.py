# normal scan = (m-n) * n -> (m) * n
# precompute = (n choose 2 * 3 + 1) + (n * 3 + 1) + (m-n) = (n * n-1 / 2) + (n * 3 + 1) + (m - n) 
# -> (n^2) + (n) + (m)
# -> n^2 or m depending on which is larger, more memory however 
import time 
import sqlite3

bases = ['A','C','G','T']

def pre_compute_match(kseq, seq) -> set: 
    res = set()
    if(len(kseq) > len(seq)): 
        return res 
    global bases 
    pre_computed = set() 
    # for i in range(len(kseq)):
    #     temp = list(kseq)
    #     for j in range(4):
    #         temp[i] = bases[j]
    #         pre_computed.add("".join(temp)) # add one char diffs
    #         # if not matches(kseq,"".join(temp)): print("WRONG")
    for i in range(len(kseq)):
        temp = list(kseq)
        for j in range(4): 
            temp[i] = bases[j]
            for k in range(i+1,len(kseq)):
                temp_copy = temp[:] 
                for l in range(4): 
                    temp_copy[k] = bases[l]
                    pre_computed.add("".join(temp_copy)) # add two char diffs 
            temp[i] = kseq[i]

    for i in range(len(seq)-len(kseq)+1):
        seq_substr = seq[i:i+len(kseq)]
        if seq_substr in pre_computed:
            res.add(seq_substr)
    return res
    

def sliding_window_match(kseq, seq) -> set: 
    res = set()
    if(len(kseq) > len(seq)): 
        return matches
    for i in range(len(seq)-len(kseq)+1):
        seq_substr = seq[i:i+len(kseq)]
        if matches(kseq,seq_substr):
            res.add(seq_substr)
    return res


def matches(a , b) -> bool: 
    count = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            count += 1
        if count > 2:
            return False
    return True

def create_connection(db_file): 
    conn = None
    try: 
        conn = sqlite3.connect(db_file)
        # conn = sqlite3.connect(':memory:')
        print(sqlite3.version)
    except Error as e: 
        print(e)
    return conn

def select_all_seqs(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()

    rows = [row[0] for row in cur.execute("SELECT kmer FROM kmer")]

    return rows


kseq = 'ACGT' 
# seq = 'ACACACGT'

conn = create_connection(r"data.db")
rows = select_all_seqs(conn)

curtime = time.process_time()
for seq in rows: 
    pre_compute_match(kseq,seq)
print("Time for precompute: " + str((time.process_time_ns()-curtime)))

curtime = time.process_time()
for seq in rows: 
    sliding_window_match(kseq,seq)
print("Time for sliding window: " + str((time.process_time_ns()-curtime)))
