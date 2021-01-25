# Coding Assessment for Day Zero Diagnostics

Database creation with fastq file and DNA sequence matching.

## Requirements

Built with Python 3.9 

## Running 

Please run the main.py file to test the code.  
database.py contains the code for file parsing and database creation.  
matching.py contains the code for sequence matching.  

## Testing

Database/table creation was verified by inspecting the data.db contents using CLI and function to read table data.  
Matching functions were tested against each other with given inputs and from the database, making sure that both outputs were correct.  
Pre_computation strings were tested as valid using the same character by character checker that the sliding window approach uses.  
Pre_computation string counts were also verified by running the math on the total number expected.  
Nested loops and operations inside of them were counted naively using a counter to ensure expected runtime was true.  

## Matching Complexity

I've included 2 functions for the matching, one of which sacrifices memory for faster processing.  

We define the size of the kmer as n and the size of the larger sequence as m.  

@pre_computed_match  
We precompute all possible kmers that are off by at most 2 characters.  
The number of kmers that are off by 1 character is n * 3. We see that there are n positions and 3 new options for each one.  
The number of kmers that are off by 2 characters is n choose 2 * 3 * 3. Here we choose 2 positions out of n, and have 3 new options for each position.  
In terms, the number of kmers that are off by 2 characters is (n!)/(2!(n-2)!) * 3 * 3 = (n * (n-1) / 2) * 9.  
We also must add the original kmer for complexity of 1.  
The combined time for precomputation is (n*3) + (n * (n-1) / 2 * 9) + (1) = (3n) + (4.5n^2 - 4.5n) + (1) -> O(n^2)  
Going through all substrings of the sequence is (m-n +1)(1) -> O(m). The cost to check is 1, because we have constant time lookup from our precomputation.  
The overall time complexity is O(m + n^2) -> O(m) if m > n^2 -> O(n^2) if n^2 > m  
The memory complexity is the same as the time complexity for precomputation -> O(n^2)  

@sliding_window_match  
We go through all substrings of the sequence and check each character one by one.  
On average, the complexity to check if a substring is valid is O(n/2) -> O(n).  
Going through all substrings of the sequence is (m-n+1) -> O(m)  
The overall time complexity is O(mn)  
The overall memory complexity is O(1)  

We can possibly improve the performance of the sliding window by using the Robin-Karp Algorithm (rolling hash) but the complexity is the same as the normal sliding window.  

The time complexity of precomputation is better on average. We can see that O(mn) is greater than O(n^2) and O(m).  
The memory complexity is better for the normal solution for most cases except edge cases.   

### Side Notes

database.py contains code that wipes the current table and creates a new one.  

### Assumptions

'A','C','G','T' are the only values in DNA sequences.  
fastq files are always formatted in the same way for this program's purposes.  
Duplicates are not desired during extraction, and not put in table twice.  
