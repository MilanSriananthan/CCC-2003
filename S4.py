cases = int(input())
result = []
def split(word, point):

    for i in range(len(word)-point + 1):
        result.append(word[i:i+point])
    return -1


for i in range(cases):
    result = []
    task = input()
    for x in range(1, len(task) + 1 ):
        split(task, x)
#        print(result)
    result = set(result)
    result = list(result)
    print(len(result) + 1) 