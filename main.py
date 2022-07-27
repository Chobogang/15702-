n, m = map(int,input().split())
score =list(map(int,input().split()))
max = 0
greaterId = 0

for i in range(m) :
    id = input().split()
    count = 0 
    for k in range(1, 5) :
        if id[k] == 'O' :
            count += score[k-1]
    if count >= max :
        if int(id[0]) <= greaterId :
            greaterId = int(id[0])
            max = count
        else : 
            greaterId = int(id[0])
            max = count
            
print(greaterId, max)
            
    