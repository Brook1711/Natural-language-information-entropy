from math import log2
p_list = [
    9.0/35, 
    12.0/35,
    14.0/35
]
H_0 = 0
for p in p_list:
    H_0 += -p*log2(p)
print("H=   "+str(H_0))