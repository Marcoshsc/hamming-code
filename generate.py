import util

def generate(number: str):

    util.validate(number)

    numberList = []
    placeHolders = []
    index = 1
    for n in number:
        nInt = int(n)
        while( util.isPowerOfTwo(index) ):
            placeHolders.append(index)
            numberList.append(-1)
            index += 1
        numberList.append(nInt)
        index += 1

    combinations = []
    greaterPower = placeHolders[len(placeHolders) - 1]
    for c, n in enumerate(numberList):
        i = c + 1
        if util.isPowerOfTwo(i):
            continue
        combination = []
        k = 1
        while(k <= greaterPower):
            if(k & i == k):
                combination.append(k)
            k *= 2
        combinations.append({
            'index': i,
            'combination': combination
        })

    for n in placeHolders:
        i = n - 1
        appear = []
        for c in combinations:
            if n in c['combination']:
                appear.append(c['index'] - 1)
        value = numberList[appear[0]] ^ numberList[appear[1]]
        for k in range(2, len(appear)):
            value = value ^ numberList[appear[k]]
        
        numberList[i] = value

    return ''.join([str(n) for n in numberList])  