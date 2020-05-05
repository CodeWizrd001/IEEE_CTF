flag = "ieee_nitc{SH4RKb0Y_4nd_laVA61rL}"
block_size = 3
flagChunks = []

flagChunk = ""
for i in range(len(flag)) :
    flagChunk += flag[i]
    if i%block_size == block_size-1 :
        flagChunks.append(flagChunk)
        flagChunk = ""

flagChunks.append(flagChunk)

print(flagChunks,len(flagChunks))