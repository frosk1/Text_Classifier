from random import *

korpus1 = "korpus_zalando_auto_gut_auto_schlecht.txt"
korpus2 = "korpus_zalando_manu_gut_uniq_2.txt"
listek1 = []
listek2 = []
listeneu = []
k1dic = {}
k2dic = {}
c = 0


def umwandeln_dic(input):
    dicci = {}
    for x in input:
        dicci[x.split("\t\t")[0]] = x.split("\t\t")[1]
    return dicci


with open(korpus1, "r") as input1, open(korpus2, "r") as input2:
    k1dic = umwandeln_dic(input1)
    k2dic = umwandeln_dic(input2)
    while len(listek1) <= 345 or len(listek2) <= 129:
        x = randint(0, 345)
        y = randint(0, 129)
        if x not in listek1:
            # outfile.write("\n")
            # outfile.write(str(c)+"\t\t"+k1dic[str(x)])
            listeneu.append(k1dic[str(x)])
            listek1.append(x)

        if y not in listek2:
            # outfile.write("\n")
            # outfile.write(str(c)+"\t\t"+k2dic[str(y)])
            listeneu.append(k2dic[str(y)])
            listek2.append(y)


            # input1.close()
            # input2.close()

# print "listeneu"+str(len(listeneu))

with open("korpus_zalando_Auto_Manu_uniq_2_final.txt", "w") as outfile:
    for i in range(len(listeneu)):
        if "\n" not in listeneu[i]:
            outfile.write(str(i) + "\t" + "\t" + listeneu[i] + "\n")
        outfile.write(str(i) + "\t" + "\t" + listeneu[i])
