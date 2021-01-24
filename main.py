import database
import matching

def main():
    source_file = "SP1.fastq"
    kmers = {}
    with open(source_file,'r') as f:
        lines = f.readlines()[1::4]
        for line in lines:         
                line = line.strip()
                if(len(line) >= 21):
                    kmers[line] = len(line) - 20 
                else: 
                    kmers[line] = 0

    conn = database.create_connection(r"data.db")

    if conn is not None: 
        database.create_kmer_table(conn)
        for kmer in kmers:
            to_Add = (kmer, kmers[kmer])
            database.create_kmer(conn, to_Add)
        conn.close()
    else: 
        print("Error! cannot create database connection")

    kmer = 'ACGT'
    seq = 'ACACACGT'

    print(matching.sliding_window_match(kmer,seq))
    print(matching.pre_compute_match(kmer,seq))
    

if __name__ == "__main__":
    main()