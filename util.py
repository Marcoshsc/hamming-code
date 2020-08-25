def validate(number: str):
    if(len(number) == 0):
        raise Exception('Empty number')
    for c in number:
        try:
            cNumber = int(c)
        except:
            raise Exception('Invalid number')

def isPowerOfTwo(number: int):
    return number != 0 and (number & (number - 1)) == 0