"""
Identify modul

Looking for text patterns
"""

# Author Jan Wessling


class Dicto(object):
    def __init__(self, name, filename):
        self.name = name
        self.filename = filename
        self.dict = self.fill_dict()

    def fill_dict(self):
        # print file
        dic = {}
        with open(self.filename, "r") as inputs:
            for i in inputs:
                # print i
                tmp = i.split("\t\t")
                dic[tmp[0]] = (tmp[1], set())
        inputs.close()
        return dic


def compare(korp_dic, dicto):
    auto = dicto.dict
    korp = korp_dic.dict
    c = 0
    for i in korp.keys():
        for x in auto.keys():

            if korp[i][0] == auto[x][0]:
                # print korp[i][0]
                # print auto[x][0]
                korp[i][1].add(dicto.name)
                c += 1
    return c


if __name__ == '__main__':
    korpus = Dicto("korpus", "Fussball_korpus.txt")
    auto_gut = Dicto("auto_gut", "Ax_teaser_gut.txt")
    # auto_schlecht = Dicto("auto_schlecht","korpus_ZA_auto_schlecht.txt")
    auto_schlecht_halbiert = Dicto("auto_schlecht", "Ax_teaser_schlecht.txt")
    # man_gut = Dicto("man","korpus_ZA_manu_fuer_gut.txt")
    # man_schlecht = Dicto("man","korpus_ZA_manu_fuer_schlecht.txt")
    man = Dicto("man", "K_teaser_korpus_angepasst.txt")

    print "auto:"
    print compare(korpus, auto_gut)
    print compare(korpus, auto_schlecht_halbiert)

    print "manu:"
    # print compare(korpus, man_gut)
    # print compare(korpus, man_schlecht)
    print compare(korpus, man)

    print "###################################"
    # korpus.dict["270"][1].add("auto_gut")
    # korpus.dict["109"][1].add("man")
    # korpus.dict["334"][1].add("auto_gut")
    # korpus.dict["131"][1].add("auto_gut")
    # korpus.dict["374"][1].add("auto_gut")
    korpus.dict["120"][1].add("man")

    man = 0
    auto = 0
    for i in korpus.dict.keys():
        # print i, korpus.dict[i][1]
        if "auto_gut" in korpus.dict[i][1] or "auto_schlecht" in korpus.dict[i][1]:
            auto += 1
        elif "man" in korpus.dict[i][1]:
            man += 1
        else:
            print i, korpus.dict[i][1]
            print korpus.dict[i][0]

    print "man :", man
    print "auto: ", auto
    print "overall :", man + auto
    # print korpus.dict["121"]


    with open("Fussball_korpus_marked.txt", "w") as output:
        # print korpus.dict.keys()
        for i in range(len(korpus.dict.keys())):
            output.write(str(i) + "\t" + list(korpus.dict[str(i)][1])[0] + "\t" + korpus.dict[str(i)][0])
        output.close()
