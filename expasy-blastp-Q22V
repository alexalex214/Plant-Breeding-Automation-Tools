#This python scripts is made by me and OpenAI to simplify analysis of DNA sequences.
#It does next things:
#1. Analyse your sequence in Expasy: SIB Swiss Institute of Bioinformatics; 2. blastp each of received amino acid sequences; 3. Use the best alignment to show you amino acid changes in format suitable for SIFT - Predict effects of nonsynonmous / missense variants.
#Hope it helps.

import requests
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML

dna_sequence = (input("Input DNA your sequence: "))

def extract_substitutions(query, subject, match):
    substitutions = []
    query_pos = 1 
    for q_char, s_char, m_char in zip(query, subject, match):
        if q_char == '-' or s_char == '-':
            continue
        
        if q_char != s_char:
            substitutions.append(f"{q_char}{query_pos}{s_char}")

        query_pos += 1

    return substitutions

url = 'https://web.expasy.org/cgi-bin/translate/dna2aa.cgi'
data = {
    'dna_sequence': dna_sequence,
    'output_format': 'fasta'
}

response = requests.post(url, data=data)

print(response.text)

amino_acid_blocks = response.text.split('\n>')[1:]  
amino_acid_sequences = []
for block in amino_acid_blocks:
    lines = block.split('\n')
    header = lines[0]
    sequence = ''.join(line.strip() for line in lines[1:] if line) 
    amino_acid_sequences.append((header, sequence))

if amino_acid_sequences:
    print("**** Amino Acid Sequences in FASTA format ****")
    for header, sequence in amino_acid_sequences:
        print(f">{header}")
        print(sequence)

    for header, amino_acid_sequence in amino_acid_sequences:
        print(f"Processing BLAST for: {header}")
        result_handle = NCBIWWW.qblast("blastp", "nr", amino_acid_sequence)

        blast_records = NCBIXML.parse(result_handle)
        blast_record = next(blast_records)  

        if blast_record.alignments:
            first_alignment = blast_record.alignments[0]
            first_hsp = first_alignment.hsps[0]

            fasta_header = f">{first_alignment.title}"
            fasta_sequence = first_hsp.sbjct

            print("**** Alignment in FASTA format ****")
            print(fasta_header)
            print(fasta_sequence)
            
            print("**** Alignment ****")
            print(f"Sequence: {first_alignment.title}")
            print(f"Length: {first_alignment.length}")
            print(f"E value: {first_hsp.expect}")
            print("Query:")
            print(first_hsp.query)
            print("Match:")
            print(first_hsp.match)
            print("Subject:")
            print(first_hsp.sbjct)
            
            query = first_hsp.query
            match = first_hsp.match
            subject = first_hsp.sbjct

            substitutions = extract_substitutions(query, subject, match)

            print("**** Substitutions ****")
            for sub in substitutions:
                print(sub)
        else:
            print("No alignments found for sequence:", header)
else:
    print("No amino acid changes received.")
