while True:
    try:
        N,m = map(int,raw_input().split())
        goods = []
        for i in range(m):
            goods.append(map(int,raw_input().split()))

        for i in range(0,m):
            for j in range(1,N+1):
                if goods[i][0] <= j:
                    a[i+1][j] = max(a[i][j],a[i][j-goods[i][0]]+goods[i][0]*goods[i][1])
    except:
        break