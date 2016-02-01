textid = 0
with open("manu.txt", "r") as input, open("k3_manu.txt", "w") as outfile:
    for i in input:
        outfile.write(str(textid) + "\t" + "\t" + i)
        textid += 1
    outfile.close()
    input.close()
