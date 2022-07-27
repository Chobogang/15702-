# 문제 수 n, 학생 수 m
n, m = map(int, input().split())
score = list(map(int, input().split()))
max = 0
greaterId = 100001

for i in range(m):
    id = input().split()
    count = 0
    for k in range(1, n + 1):
        if id[k] == 'O':
            count += score[k - 1]
    if count > max:
        greaterId = int(id[0])
        max = count
    elif count == max:
        count = max
        greaterId = min(int(id[0]), greaterId)
    else:
        continue

print(greaterId, max)
