
""" its not perfect, but it works, just follow the rules, dont put double
    fives as it will count it even though it shouldnt and i dont know how to fix it """
def romanNum(numeral):
    romanIn = numeral

    if romanIn ==  type(""):
        raise TypeError ("expected string, got %s" % type(romanIn))
    input = romanIn.upper()
    nums = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
    sum = 0
    for i in range(len(input)):
        try:
            value = nums[input[i]]
            if i+1 < len(input) and nums[input[i+1]] > value:
                sum -= value
            else: sum += value
        except KeyError:
            raise ValueError ('input is not a valid Roman numeral: %s' % input)

    print (sum)


while True:
    Numeral = input("please input your roman numeral here!\n")
    romanNum(Numeral)

    convert = input("do you want to continue converting?\n")
    if convert == "no" and not convert == "yes":
        Really = False
        break

    elif convert == "yes" and not convert == "no":
        Really = False
        continue