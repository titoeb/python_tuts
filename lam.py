def fu(a):
    return lambda: print(a)

containter = []
for i in range(10):
    containter.append(fu(i))

for elem in containter:
    elem()

fu(5)()