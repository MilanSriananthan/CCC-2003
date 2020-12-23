cases = int(input())
def vowel(letter):
    if letter == "a" or letter == "A" or letter == "E" or letter == "e" or letter == "i" or letter == 'I' or letter == "O" or letter == "o" or letter == "U" or letter == "u":
        return True
    return False

def sylable(seq):
    result = seq
    for i in range(len(seq)):
#        print(seq[-i-1])
        if vowel(seq[-i-1]) == True:
            result = seq[-i-1:]
            break
#    print(result)
    return result


def rhyme(seq1, seq2, seq3, seq4):
    if seq1 == seq2 and seq2 == seq3 and seq3 == seq4:
        return "perfect"
    elif seq1 == seq2 and seq3 == seq4:
        return "even"
    elif seq1 == seq3 and seq2 == seq4:
        return "cross"
    elif seq1 == seq4 and seq2 == seq3:
        return "shell"
    return "free"

for i in range(cases):
    line1 = input()
    line2 = input()
    line3 = input()
    line4 = input()
    line1 = line1.split(" ")
    line2 = line2.split(" ")
    line3 = line3.split(" ")
    line4 = line4.split(" ")
    last1 = line1[-1]
    last2 = line2[-1]
    last3 = line3[-1]
    last4 = line4[-1]
    last1 = sylable(last1).lower()
    last2 = sylable(last2).lower()
    last3 = sylable(last3).lower()
    last4 = sylable(last4).lower()
#    print(last4)
#    print(last1)
#    print(last2)
    print(rhyme(last1, last2, last3, last4))