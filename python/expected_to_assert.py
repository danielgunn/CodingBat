# This tool converts the expected/run table that Codingbat.com
# gives you once youve solved a problem, into a series of
# assert statements in python

f = open("expected_input_warmup2.dat","r")
for line in f:
    print("assert",line.split("\t")[0].replace("→","=="))
f.close()