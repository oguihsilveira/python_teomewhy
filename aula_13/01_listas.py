""" x = []
for i in range(1, 101):
    x.append(i)

print(x) """

##############################################

""" y = [i for i in range(1, 101)]
print(y) """

##############################################

""" def par(w):
    return w % 2 == 0

s = [par(i) for i in range(1,101)]
print(s) """

##############################################

def par(w):
    return w % 2 == 0

w = [i for i in range(1, 101) if par(i)]
