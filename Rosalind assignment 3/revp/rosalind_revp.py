#locating restriction sites
'''
1. read the fasta file and turn it into a string 
2. iterate through the string 
3. if the i of the string is the same as the inverse 


'''
file = open('rosalind_revp.txt')
rawdata = {}
names = []
sequences = []
soltuple = []

nuc_dict = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}

for line in file:
    if line.startswith('>'):
        name = line[1:].rstrip('\n')
        rawdata[name] = ''
    else:
        rawdata[name] = rawdata[name] +line.rstrip('\n')

#stores the keys 
for item in rawdata.keys ():
    names.append (item)

#stores the sequences
for key in names:
    sequences = str(rawdata[key])

for index in range(len(sequences)):
    for length in range(4, 13):
        if index + length <= len(sequences):
            sequence = sequences[index:index + length]
            reverse = ''.join([nuc_dict[base] for base in reversed(sequence)])

            if reverse == sequence:
                soltuple.append((index + 1, length))

# Print the result in the format position length
for item in soltuple:
    print(item[0], item[1])
