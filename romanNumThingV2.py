def int_to_roman(input):
    """ Convert an integer to a Roman numeral. """

    if not isinstance(input, type(1)):
        raise TypeError ("expected integer, got %s" % type(input))
    if not 0 < input < 4000:
        raise ValueError ("Argument must be between 1 and 3999")
    ints = (1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1)
    nums = ('M',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I')
    result = []
    for i in range(len(ints)):
        count = int(input / ints[i])
        result.append(nums[i] * count)
        input -= ints[i] * count
    print (''.join(result))

while True:
    number = int(input("please type your number here!\n"))
    int_to_roman(number)

    convert = input("do you want to continue converting\n")
    if convert == "no":
        print ("oh, okay, bye then")
        break
    if convert == "yes":
        print("cool here we go again!")
        continue