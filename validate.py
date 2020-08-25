import util

def validate(number: str):

    util.validate(number)

    intList = [int(c) for c in number]

    powers = []
    k = 1
    while(k < len(intList)):
        powers.append(k)
        k *= 2
    
    combinations = []
    for c, n in enumerate(intList):
        i = c + 1
        if util.isPowerOfTwo(i):
            continue
        combination = []
        for w in powers:
            if(w & i == w):
                combination.append(w)
        combinations.append({
            'index': i,
            'combination': combination
        })
    
    sums = [intList[p - 1] for p in powers]

    for ce, n in enumerate(powers):
        for c in combinations:
            if n in c['combination']:
                sums[ce] += intList[c['index'] - 1]
    
    sums = [0 if s % 2 == 0 else 1 for s in sums]

    totalSum = 0
    for s in sums:
        totalSum += s
    
    if(totalSum == 0):
        print('Correct sequence!')
        print('No error was encountered.')
        return
    
    position = 0
    i = 0
    for c in range(len(sums) - 1, -1, -1):
        n = sums[i]
        position += n**c
        i += 1

    position -= 1
    intList[position] = 0 if intList[position] == 1 else 1
    print('Corrupted sequence.')
    print(f'Invalid bit encountered at index {position}.')
    print(f'Right sequence would be {"".join([str(n) for n in intList])}')