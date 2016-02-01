"""
Comparison modul

Looking for the same annotation data.
"""
import re

file1 = "/home/jan/Development/Korpus/Fball/Annotation/03122015_Annotation_f_Jan_60_65.txt"
file2 = "/home/jan/Development/Korpus/Fball/Annotation/04122015_Annotation_f_Mel_60_65.txt"

file3 = "out.txt"
list1 = []
list2 = []
list3 = []


def evengleich(file1, file2, file3):
    with open(file1, "r") as in1, open(file2, "r") as in2, open(file3, "w") as out:
        for i in in1:
            list1.append(i)
        for x in in2:
            list2.append(x)
        in1.close()
        in2.close()
        out.close()
    for i in list1:
        pattern1 = re.match("Text (\d+), Text (\d+)\t\t(\d)", i)
        if pattern1:
            for x in list2:
                pattern = re.match("Text (\d+), Text (\d+)\t\t(\d)", x)
                if pattern:
                    if pattern1.group(1) == pattern.group(1) and pattern1.group(2) == pattern.group(
                            2) and pattern1.group(3) == pattern.group(3):
                        print i


if __name__ == "__main__":
    file1 = "/home/jan/Development/Korpus/Fball/Annotation/03122015_Annotation_f_Jan_144_149.txt"
    file2 = "/home/jan/Development/Korpus/Fball/Annotation/04122015_Annotation_f_Mel_144_149.txt"

    file3 = "out.txt"
    list1 = []
    list2 = []
    list3 = []

    evengleich(file1, file2, file3)
