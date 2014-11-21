import sys

s1 = "Crsr utu, t  i  ctstyedu,taf,rnpeen taycre,i thsheeeatn,endees,ibe ."
s2 = "ra aadee ohsccipet.o e n  n  aatm eee   .x geie t  cf v  o x t tene"
s3 = "yptcnycsatieoanr a ghnfditdybdlosddvdfam atenomt sfatwebnwtedrt   a"
s4 = "phhtd h mhncmt eocCra orfhseui s e a adaFmhncnehteodeanuo,hreahcbvs"
s5 = "tyei onfoegumitsfkrasure o,attcywsalii nopeer  oocrersttw icmtaarei"
s6 = "o  csfionrsruohe eyp s dnu r irseinunrhnrl ryswu u s  e  asioetnorl"
s7 = "gipet qrg ,ennenarphbehsosostoytrgda loe eVepcagbrd iidwkn sns  kyy"

plaintext = [s1, s2, s3, s4, s5, s6, s7]

# Cryptography is the ps the practice
for i in range(0, 68):
    for line in range(0,7):
        if (i == 67 and line > 0):
            break;
        #print line, plaintext[line], len(plaintext[line])
        sys.stdout.write(plaintext[line][i])
    
