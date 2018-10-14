while True:
    try:
        n = int(raw_input())
        words = []
        for i in range(n):
            words.append(raw_input().strip())
        for word in sorted(words):
            print word
    except:
        break