"""
Summarize modul

terminal output for detailed information of korpus.
"""
import re

# Author Jan Wessling


def fill_dic(korp_file):
    dicto = {}
    with open(korp_file, "r") as korp:
        for i in korp:
            pattern = re.search("(\d+)\t(\w+).*", i)
            if pattern:
                dicto[pattern.group(1)] = pattern.group(2)
        korp.close()
    return dicto


def detect(count_dic, number, korpus):
    if korpus[number] == "auto_gut":
        count_dic["auto_gut"] += 1
    elif korpus[number] == "auto_schlecht":
        count_dic["auto_schlecht"] += 1
    elif korpus[number] == "man":
        count_dic["man"] += 1


def count(file, korp):
    count = {"auto_gut": 0, "auto_schlecht": 0, "man": 0}
    with open(file, "r") as anno:
        for i in anno:
            pattern = re.search("Text (\d+), Text (\d+)\t\t(\d)", i)
            # print i
            if pattern:
                if pattern.group(3) == "0":
                    # print pattern.group(1)
                    detect(count, pattern.group(1), korp)
                else:
                    # print pattern.group(2)
                    detect(count, pattern.group(2), korp)
        anno.close()
    return count


def printer(count_dic):
    count_dic["auto_gesamt"] = count_dic["auto_gut"] + count_dic["auto_schlecht"]
    for i in count_dic.keys():
        print i, ": ", count_dic[i]


if __name__ == '__main__':
    # Fball /home/jan/Development/Korpus/Fball/Finales_Korpus/Fussball_korpus_marked.txt
    # noch annotationsdatei eingeben count_dic = count("annotationsdatei ", korp)
    korp = fill_dic("/home/jan/Development/Korpus/Fball/Finales_Korpus/Fussball_korpus_marked.txt")
    count_dic = count(" ", korp)
    printer(count_dic)
