while True:
    try:
        num = int(raw_input())
        i = 2
        while num!=1:
            if num%i == 0:
                print i,
                num = num/i
            else:
                i += 1
        print ''
    except:
        break