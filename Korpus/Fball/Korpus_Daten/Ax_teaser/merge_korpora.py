from random import *
import re

korpus1 = "Ax_teaser_korpus_marked.txt"
korpus2 = "K_teaser_korpus_marked_angepasst.txt"
listek1 = []
listek2 = []
listeneu = []
# k1dic = {}
# k2dic = {}
c = 0


def umwandeln_dic(input):
    dicci = {}

    for i in input:
        pattern = re.search("(\d+)\t(\w+.*)", i)
        if pattern:
            dicci[pattern.group(1)] = pattern.group(2)

    # for x in input:
    #     dicci[x.split("\t\t")[0]] = x.split("\t\t")[1]
    # print dicci.keys()
    return dicci


with open(korpus1, "r") as input1, open(korpus2, "r") as input2:
    k1dic = umwandeln_dic(input1)
    k2dic = umwandeln_dic(input2)
    while len(listek1) <= 305 or len(listek2) <= 130:
        x = randint(0, 305)
        y = randint(0, 130)
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

    input1.close()
    input2.close()

# print "listeneu"+str(len(listeneu))

with open("Fussball_korpus_marked.txt.txt", "w") as outfile:
    for i in range(len(listeneu)):
        if "\n" not in listeneu[i]:
            outfile.write(str(i) + "\t" + "\t" + listeneu[i] + "\n")
            # outfile.write(str(i)+"\t"+"\t"+listeneu[i])
    outfile.close()
