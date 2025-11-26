protein_dictionary = {
  "AAA": "Asn", "AAC": "Lys", "AAG": "Lys", "AAU": "Asn", "ACA": "Thr", "ACC": "Thr", "ACG": "Thr", "ACU": "Thr",
  "AGA": "Arg", "AGC": "Ser", "AGG": "Arg", "AGU": "Ser", "AUA": "Ile", "AUC": "Ile", "AUG": "Met", "AUU": "Ile",
  "CAA": "Gln", "CAC": "His", "CAG": "Gln", "CAU": "His", "CCA": "Pro", "CCC": "Pro", "CCG": "Pro", "CCU": "Pro",
  "CGA": "Arg", "CGC": "Arg", "CGG": "Arg", "CGU": "Arg",  "CUA": "Leu", "CUC": "Leu", "CUG": "Leu", "CUU": "Leu",
  "GAA": "Glu", "GAC": "Asp", "GAG": "Glu", "GAU": "Asp", "GCA": "Ala", "GCC": "Ala", "GCG": "Ala", "GCU": "Ala",
  "GGA": "Gly", "GGC": "Gly", "GGG": "Gly", "GGU": "Gly", "GUA": "Val", "GUC": "Val", "GUG": "Val", "GUU": "Val",
  "UAA": "Stop", "UAC": "Tyr", "UAG": "Stop", "UAU": "Tyr", "UCA": "Ser", "UCC": "Ser", "UCG": "Ser", "UCU": "Ser",
  "UGA": "Stop", "UGC": "Cys", "UGG": "Trp", "UGU": "Cys", "UUA": "Leu", "UUC": "Phe", "UUG": "Leu", "UUU": "Phe"
}

dna = input("Enter the DNA sequence, spaces don't matter").replace(" ", "").upper()
rna = ""
proteins = []

for i in range(len(dna)):
  if dna[i] == "A": rna += "U"
  if dna[i] == "G": rna += "C"
  if dna[i] == "C": rna += "G"
  if dna[i] == "T": rna += "A"
  if i % 3 == 2 and i + 1 != len(dna): rna += "/"

codons = rna.split("/")

for i in codons:
  if len(i) == 3: proteins.append(protein_dictionary[i])
  else: proteins.append("???")

print(" ".join(codons))
print(", ".join(proteins))
