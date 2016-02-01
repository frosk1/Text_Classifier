__author__ = 'jan'
listek1 = []
listek2 = []
count = 0
with open("Text_Korpus_aktuell.txt", "r") as input:
    for i in input:
        listek1.append(i.split("\t\t")[0])
        count += 1
    for i in range(len(listek1)):
        # print i , listek1[i]
        if i != int(listek1[i]):
            print "yes"
            print "das ist i", i, "das ist liste i", listek1[i]
