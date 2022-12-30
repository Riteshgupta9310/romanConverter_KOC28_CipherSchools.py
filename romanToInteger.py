#convert given Roman to Integer
#largest to smallest: add them up
#smallest to largest: subtract smaller 

def roman_number(roman):
    if roman=='I':
        return 1
    if roman=='V':
        return 5
    if roman=='X':
        return 10
    if roman=='L':
        return 50
    if roman=='C':
        return 100
    if roman=='D':
        return 500
    if roman=='M':
        return 1000
    return -1

def roman_integer(str):
    res=0
    i=0

    while(i<len(str)):
        n1=roman_number(str[i])
        
        if (i+1<len(str)):
            n2=roman_number(str[i+1])

            #comparing both roman values n1 and n2:
            if n1>=n2:
                res=res+n1
                i=i+1
            else:
                res=res+n2-n1
                i=i+2
        else:
            res=res+n1
            i=i+1
    return res




roman=str(input("Enter a roman number: "))
print("The required integer is:",roman_integer(roman))