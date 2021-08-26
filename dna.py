"""
This project involves some DNA analysis for a fictional crime investigation.

Case Information:
Three suspects were apprehended by authorites. One of which is believed to be an international spy.
The only evidence is some surveillance video and a small DNA sample retrieved from a computer keyboard.
Each suspect has submitted a DNA sample.
Use the DNA sample retrieved from crime scene and the three DNA samples from the suspects
to determine the spy everyone is looking for.
"""

sample = ['GTA','GGG','CAC']

# create a method that will read a suspect's DNA sample and add the file's content to an empty string
def read_dna(dna_file):
  dna_data = ""
  with open(dna_file, "r") as f:
    for line in f:
      dna_data += line
  return dna_data

# create a method that will iterate through a string, slice it into smaller strings that are three letters long, and add them to a list
def dna_codons(dna):
  codons = []
  for i in range(0, len(dna), 3):
    if (i + 3) < len(dna):
      # i starts at 0. We add dna[0:3], which adds only the first three characters of a string
      codons.append(dna[i:i + 3])
  return codons

# create a method that will iterate through a suspect’s codon list to see how many of her codons match the sample codons
def match_dna(dna):
  matches = 0
  # iterate through the codons in the suspect DNA's list to see if the codon also exists in the sample
  for codon in dna:
    # there is a single match if a codon in the DNA matches a codon in the sample
    if codon in sample:
      matches += 1
  return matches

# create a method to determine if a suspect offers enough to continue investigation
def is_criminal(dna_sample):
  # create a string to hold DNA samples
  dna_data = read_dna(dna_sample)
  # create a codon list from the chopped string 
  codons = dna_codons(dna_data)
  # match the sample with the DNA
  num_matches = match_dna(codons)
  # see if the number of matches is significant
  if num_matches >= 3:
    print("Number of codon matches: %s. DNA profile matches. Continue investigation." % num_matches)
  else:
    print("Number of codon matches: %s. DNA profile matches. Suspect cleared." % num_matches)
      
      
# call is_criminal() on the .txt files to find out who the spy is
# uncomment code below
#is_criminal('suspect1.txt')
#is_criminal('suspect2.txt')
#is_criminal('suspect3.txt')
