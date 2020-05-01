def retFlagChunks() :
	x = 'ieee_nitc{vishnu_UltG4M3r__pirate__Ph4t3_HuR4K3n_J0nQu1L_Azr13L_DR4G0n_Xx--xX}'
	flagChunks = []
	temp = ""
	for i in range(len(x)) :
		temp += x[i]
		if i%6 == 5 :
			flagChunks.append(temp)
			temp = ""
	return flagChunks

g = retFlagChunks()
for i in g :
    print(i)