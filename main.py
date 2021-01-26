import database
import matching

def main():
    kmers = database.read_fastq("SP1.fastq")

    conn = database.create_connection(r"data.db")

    if conn is not None: 
        database.create_kmer_table(conn)
        for kmer in kmers:
            new_entry = (kmer, kmers[kmer])
            database.create_kmer(conn, new_entry)
        conn.close()
    else: 
        print("Error! Cannot create database connection")

    kmer = 'ACGT'
    seq = 'ACACACGT'

    print(matching.sliding_window_match(kmer,seq))
    print(matching.pre_compute_match(kmer,seq))
    

if __name__ == "__main__":
    main()