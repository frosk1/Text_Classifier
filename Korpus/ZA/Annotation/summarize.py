"""
Summarize modul

terminal output for detailed information of korpus.
"""
import collections
import re

__author__ = 'jan'


def fill_dic(korp_file):
    dicto = {}
    with open(korp_file, "r") as korp:
        for i in korp:
            pattern = re.search("(\d+)\t(\w+).*", i)
            if pattern:
                dicto[pattern.group(1)] = pattern.group(2)
        korp.close()
    return dicto


def count(file, korp):
    count = []
    with open(file, "r") as anno:
        for i in anno:
            pattern = re.search("Text (\d+), Text (\d+)\t\t(\d)", i)
            # print i
            if pattern:
                if pattern.group(3) == "0":
                    count.append(korp[pattern.group(1)])
                else:
                    count.append(korp[pattern.group(2)])
        anno.close()
    return collections.Counter(count)


def printer(counter_dic):
    counter_dic["Anno_Pairs"] = 0
    for i in counter_dic.keys():
        counter_dic["Anno_Pairs"] += counter_dic[i]
    counter_dic["auto_gesamt"] = counter_dic["auto_gut"] + counter_dic["auto_schlecht"]
    print "Overall_Anno_Pair: ", counter_dic["Anno_Pairs"]
    for i in counter_dic.keys():
        if i == "Anno_Pairs":
            continue
        else:
            print i, ": ", counter_dic[i], ";", round(float(counter_dic[i]) / (float(counter_dic["Anno_Pairs"]) / 100),
                                                      2), "%"


if __name__ == '__main__':
    # Korpus :
    # ZA "/home/jan/Development/Korpus/ZA/Finales_Korpus/Text_Korpus_aktuell_marked.txt"

    # Annotation :
    # overall_annotation_20.txt
    # overall_annotation_80.txt
    # overall_annotation_100.txt

    korp = fill_dic("/home/jan/Development/Korpus/ZA/Finales_Korpus/Text_Korpus_aktuell_marked.txt")
    # count_dic = count("overall_annotation_80.txt", korp)
    # printer(count_dic)

    l = []
    with open("overall_annotation_80.txt", "r") as anno:
        for i in anno:
            pattern = re.search("Text (\d+), Text (\d+)\t\t(\d)", i)
            # print i
            if pattern:
                l.append(korp[pattern.group(1)])
                l.append(korp[pattern.group(2)])
        anno.close()
    printer(collections.Counter(l))
