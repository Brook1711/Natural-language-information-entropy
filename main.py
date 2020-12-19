import math

en_list = [
    0.1859,
    0.0642,
    0.0127,
    0.0218,
    0.0317,
    0.1031,
    0.0208,
    0.0152,
    0.0467,
    0.0575,
    0.0008,
    0.0049,
    0.0321,
    0.0198,
    0.0574,
    0.0632,
    0.0152,
    0.0008,
    0.0484,
    0.0514,
    0.0796,
    0.0228,
    0.0083,
    0.0175,
    0.0014,
    0.0164,
    0.0005
]
en_entropy = 0
for p_i in en_list:
    en_entropy += -p_i * math.log2(p_i)

en_H_0 = math.log2(26+1)

en_eta = en_entropy / en_H_0
print("en_eta:      "+str(en_eta))
print("1-en_eta:    "+str(1-en_eta))

cn_list = []
cn_list += 140 * [0.5/140]
cn_list += 485 * [0.35/485]
cn_list += 1775 * [0.147/1775]
cn_list += 7600 * [0.003/7600]

cn_entropy = 0
for p_i in cn_list:
    cn_entropy += -p_i * math.log2(p_i)
cn_H_0 = math.log2(140 + 485 + 1775 + 7600)

cn_eta = cn_entropy / cn_H_0
cn_eta = cn_entropy / cn_H_0
print("cn_eta:      "+str(cn_eta))
print("1-cn_eta:    "+str(1-cn_eta))
