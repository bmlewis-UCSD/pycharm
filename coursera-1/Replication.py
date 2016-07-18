def ApproximatePatternCount(Pattern, Text, d):
    count = 0 # initialize count variable
    for i in range(len(Text) - len(Pattern) + 1):
        aprox = HammingDistance(Text[i:i + len(Pattern)],Pattern)
        if aprox <= d:
           count = count + 1
    return count


def ApproximatePatternMatching(Pattern, Text, d):
    positions = [] # initializing list of positions
    for i in range(len(Text) - len(Pattern) + 1):
        aprox = HammingDistance(Text[i:i + len(Pattern)],Pattern)
        if aprox <= d:
            positions.append(i)
    return positions



def PatternMatching(Text, Pattern):
    positions = []
    for i in range(len(Text) - len(Pattern) + 1):
        if Text[i:i + len(Pattern)] == Pattern:
            positions.append(i)
    return positions
###
def PatternCount(Pattern, Text):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count
###
#p = "TGACCCGTTATGCTCGAGTTCGGTCAGAGCGTCATTGCGAGTAGTCGTTTGCTTTCTCAAACTCC"
#q = "GAGCGATTAAGCGTGACAGCCCCAGGGAACCCACAAAACGTGATCGCAGTCCATCCGATCATACA"
def HammingDistance(p, q):
    HD = 0
    for i in range(0, len(p)):
         if p[i] != q[i]:
            HD = HD + 1
    return HD
#print HammingDistance(p, q)

 ###
##inefficient version
def SymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2]
    for i in range(n):
        array[i] = PatternCount(ExtendedGenome[i:i+(n//2)],symbol)
    return array
### fatser version
def FasterSymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2]
    array[0] = PatternCount(symbol, Genome[0:n//2])
    for i in range(1, n):
        array[i] = array[i-1]
        if ExtendedGenome[i-1] == symbol:
            array[i] = array[i]-1
        if ExtendedGenome[i+(n//2)-1] == symbol:
            array[i] = array[i]+1
    return array
###skew array
#Genome = "GATACACTTCCCGAGTAGGTACTG"
def Skew(Genome):
    skew = {} #initializing the dictionary
    n = len(Genome)
    skew[0] = 0
    for i in range(1,n+1):
        skew[i] = skew[i-1]
        if Genome[i-1] == "G":
            skew[i] = skew[i-1]+1
        if Genome[i - 1] == "C":
            skew[i] = skew[i - 1] - 1
    return skew
###
def MinimumSkew(Genome):
    positions = [] # output variable
    d = Skew(Genome)
    m = min((d.values()))
    positions = [k for k in d if d[k] == m]
    return positions
#print(MinimumSkew(Genome))
#print(Skew(Genome))
###
def ReverseComplement(text):
    revComp = ""
    for i in range(len(text)):
        revComp += complement(text[len(text)-i-1])
    return revComp
####
def complement(nucleotide):
    nucleotide = nucleotide.lower()
    bp = "" # output variable
    if nucleotide == "a":
        bp = "t"
    elif nucleotide == "t":
        bp = "a"
    elif nucleotide == "c":
        bp = "g"
    elif nucleotide == "g":
        bp = "c"
    return bp
####


        #text = raw_input("enter text: ")
#print ReverseComplement(text)