def retFlagChunks() :
	x = 'ieee_nitc{Z3u5_UltG4M3r__pirate__Ph4t3_HuR4K3n_J0nQu1L_Azr13L_DR4G0n_Xxxx-----xxxX}'
	x = 'Z3u5_UltG4M3r__pirate__Ph4t3_HuR4K3n_J0nQu1L_Azr13L_DR4G0n_Xxxx-----xxxX'
	print(len(x))
	flagChunks = []
	temp = ""
	for i in range(len(x)) :
		temp += x[i]
		if i%8 == 7 :
			flagChunks.append(temp)
			temp = ""
	return flagChunks

g = retFlagChunks()
print(g,len(g))
h = [
'ieee_n', 
'itc{Z3', 
'u5_Ult', 
'G4M3r_', 
'_pirat', 
'e__Ph4', 
't3_HuR', 
'4K3n_J', 
'0nQu1L', 
'_Azr13', 
'L_DR4G', 
'0n_Xxx',
'--xxX}']
for i in g :
    print(i,i in h)