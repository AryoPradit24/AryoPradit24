a = 0
for i in range(10**9, 10**10):
    if i % 2 == 0 and i % 3 == 0 and i % 5 == 0  and i % 7 == 0 and i % 11 == 0 :
        a = i
        break

print(a)
