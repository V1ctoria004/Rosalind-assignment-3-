'''
def calculate_failure_array(s):
    n = len(s)
    failure_array = [0] * n

    j = 0
    for k in range(2, n + 1):
        while j > 0 and s[j] != s[k - 1]:
            j = failure_array[j - 1]
        if s[j] == s[k - 1]:
            j += 1
        failure_array[k - 1] = j

    return failure_array

def fasta_to_string (filename):
    file = open(filename)
    rawdata = {}
    names = []
    sequences = []
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
    return str(sequences[0])

def main():
    # Sample Dataset
    dna_string = fasta_to_string ('rosalind_kmp.txt')

    # Calculate the failure array
    result = calculate_failure_array(dna_string)

    # Print the result
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()

-----------------

def calculate_failure_array(s):
    n = len(s)
    failure_array = [0] * n

    j = 0
    for k in range(2, n + 1):
        while j > 0 and s[j] != s[k - 1]:
            j = failure_array[j - 1]
        if s[j] == s[k - 1]:
            j += 1
        failure_array[k - 1] = j

    return failure_array

def fasta_to_string(filename):
    file = open(filename)
    rawdata = {}
    names = []
    sequences = []
    for line in file:
        if line.startswith('>'):
            name = line[1:].rstrip('\n')
            rawdata[name] = ''
        else:
            rawdata[name] += line.rstrip('\n')

    # stores the keys
    for item in rawdata.keys():
        names.append(item)

    # stores the sequences
    for key in names:
        sequences.append(str(rawdata[key]))

    return str(sequences[0])

def main():
    # Sample Dataset
    dna_string = fasta_to_string('rosalind_kmp.txt')

    # Calculate the failure array
    result = calculate_failure_array(dna_string)

    # Print the result
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()
'''

def calculate_failure_array(s):
    n = len(s)
    failure_array = [0] * n

    j = 0
    for k in range(2, n + 1):
        while j > 0 and s[j] != s[k - 1]:
            j = failure_array[j - 1]
        if s[j] == s[k - 1]:
            j += 1
        failure_array[k - 1] = j

    return failure_array

def fasta_to_string(filename):
    file = open(filename)
    rawdata = {}
    names = []
    sequences = []
    for line in file:
        if line.startswith('>'):
            name = line[1:].rstrip('\n')
            rawdata[name] = ''
        else:
            rawdata[name] += line.rstrip('\n')

    # stores the keys
    for item in rawdata.keys():
        names.append(item)

    # stores the sequences
    for key in names:
        sequences.append(str(rawdata[key]))

    return str(sequences[0])

def main():
    # Sample Dataset
    dna_string = fasta_to_string('rosalind_kmp.txt')

    # Calculate the failure array
    result = calculate_failure_array(dna_string)

    # Write the result to a file
    with open('kmp_result.txt', 'w') as output_file:
        output_file.write(" ".join(map(str, result)))

if __name__ == "__main__":
    main()
