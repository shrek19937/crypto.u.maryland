ct = "F96DE8C227A259C87EE1DA2AED57C93FE5DA36ED4EC87EF2C63AAE5B9A7EFFD673BE4ACF7BE8923CAB1ECE7AF2DA3DA44FCF7AE29235A24C963FF0DF3CA3599A70E5DA36BF1ECE77F8DC34BE129A6CF4D126BF5B9A7CFEDF3EB850D37CF0C63AA2509A76FF9227A55B9A6FE3D720A850D97AB1DD35ED5FCE6BF0D138A84CC931B1F121B44ECE70F6C032BD56C33FF9D320ED5CDF7AFF9226BE5BDE3FF7DD21ED56CF71F5C036A94D963FF8D473A351CE3FE5DA3CB84DDB71F5C17FED51DC3FE8D732BF4D963FF3C727ED4AC87EF5DB27A451D47EFD9230BF47CA6BFEC12ABE4ADF72E29224A84CDF3FF5D720A459D47AF59232A35A9A7AE7D33FB85FCE7AF5923AA31EDB3FF7D33ABF52C33FF0D673A551D93FFCD33DA35BC831B1F43CBF1EDF67F0DF23A15B963FE5DA36ED68D378F4DC36BF5B9A7AFFD121B44ECE76FEDC73BE5DD27AFCD773BA5FC93FE5DA3CB859D26BB1C63CED5CDF3FE2D730B84CDF3FF7DD21ED5ADF7CF0D636BE1EDB79E5D721ED57CE3FE6D320ED57D469F4DC27A85A963FF3C727ED49DF3FFFDD24ED55D470E69E73AC50DE3FE5DA3ABE1EDF67F4C030A44DDF3FF5D73EA250C96BE3D327A84D963FE5DA32B91ED36BB1D132A31ED87AB1D021A255DF71B1C436BF479A7AF0C13AA14794"
# print len(ct)

freqencytable = {
     97:  8.12, # a
     98:  1.49, # b
     99:  2.71, # c
    100:  4.32, # d
    101: 12.02, # e
    102:  2.30, # f
    103:  2.03, # g
    104:  5.92, # h
    105:  7.31, # i
    106:  0.10, # j
    107:  0.69, # k
    108:  3.98, # l
    109:  2.61, # m
    110:  6.96, # n
    111:  7.68, # o
    112:  1.82, # p
    113:  0.11, # q
    114:  6.02, # r
    115:  6.28, # s
    116:  9.10, # t
    117:  2.88, # u
    118:  1.11, # v
    119:  2.09, # w
    120:  0.17, # x
    121:  2.11, # y
    122:  0.07, # z
}

klen = 7  # calculated previously

# 1. break ct into 7 groups
offset = 6
ct1 = ""
for i in range(offset, len(ct)/2):
    c = (i - offset) % klen
    if (c == 0):
        ct1 = ct1 + ct[2*i]+ct[2*i+1]
#print len(ct1)/2, ct1

# 2. each groups of the ct is to be XOR'd with the same BYTE
# 3. loops (0,255) to see which one is the most like by
pt1 = {}    # pt1 holds a collection of ascii value of plaintext chr(s)
for enckey in range(0,256):   # try ALL 256 possibilities
    valid = True
    for j in range(0, len(ct1)/2):
        cch = int(ct1[2*j]+ct1[2*j+1], 16)
        pt1[j] = (cch ^ enckey)  # ascii value of the chr (an int)
        if (pt1[j] >= 127 or pt1[j] < 32 or (pt1[j] >= 48 and pt1[j] <= 57)):   # none ASCII found
            valid = False
            continue

    if (valid):
        ptfreq = {}
        ptstr = ""
        for key, value in pt1.iteritems():
            ptstr = ptstr + unichr(value)
            # calc. the frequency here
            if (value in ptfreq):   # value is the acsii value of the plaintext chr
                ptfreq[value] = ptfreq[value] + 1
            else:
                ptfreq[value] = 1
        #print hex(enckey), ptfreq
        #print ptstr
    
        # 4. calculate the sum(p[a]*freq[a] + p[b]*freq[b] + .... + p[z]*freq[z])
        ptfreqval = 0.0
        ptfreqrec = {}
        for lowerl in range(97, 123):  # [a-z]
            lowerlfreqInPT = 0.0
            if (lowerl in ptfreq):
                lowerlfreqInPT = ptfreq[lowerl]
            #print lowerl, freqencytable[lowerl], float(lowerlfreqInPT)
            ptfreqval = ptfreqval + (float(lowerlfreqInPT)/len(ptstr)) * freqencytable[lowerl]
        ptfreqrec[ptstr] = ptfreqval
        print ptfreqrec
            
            
    


