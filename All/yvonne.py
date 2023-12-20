def stringToBinary( test_str):
    print(str(test_str))

    res=''
    for i in test_str:
        if i==' ': 
            res=res+'000000'
        else:
            res=res+''.join(format(ord(i),'08b'))

    print(str(res))



text=input("Please input any String: ")
stringToBinary(text)

