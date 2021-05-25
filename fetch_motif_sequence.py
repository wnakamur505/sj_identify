import sys
import pysam

reference = sys.argv[1]

fasta_tb = pysam.FastaFile(reference)

#with open("428_100test.bed","r") as f:
#with open("input_file","r") as f:
with open("c9.bed","r") as f:

    for line in f:
        
        f = line.rstrip('\n').split('\t')

        motif_seq = fasta_tb.fetch (f[0], int(f[1])-1, int(f[2])) #個数があっているから多分これは良い。
        
        MOTIF_SEQ = motif_seq.upper()
        
        #print( MOTIF_SEQ + '\t' + f[5])
        
        print( MOTIF_SEQ + '\t' + f[0] + '\t' + f[1] + '\t' + f[2] + '\t' + f[3] + '\t' + f[4] + '\t' + f[5] + '\t' + f[6] + '\t' + f[7] + '\t' + f[8] + '\t' + f[9] + '\t' + f[10] + '\t' + f[11] +'\t' + f[12] + '\t' + f[13] + '\t' + f[14] +'\t' + f[15] + '\t' + f[16] +'\t' +  f[17] + '\t' + f[18] + '\t' + f[19] + '\t' + f[20] + '\t' + f[21] + '\t' + f[22] + '\t' + f[23] + '\t' + f[24] + '\t' + f[25] + '\t' + f[26])
        
        #python3 fetch_motif_sequence.py > fetch_motif_sequence.txt