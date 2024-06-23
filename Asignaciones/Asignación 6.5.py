text = "X-DSPAM-Confidence:    0.8475"
pos = text.find(":")
#print(pos)
#cincopos = text.find("5", pos)
#print(cincopos)
number = text[pos+1:]
print(float(number))