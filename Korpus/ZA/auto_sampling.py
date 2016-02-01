"""
auto_sampling :

Script for generate Textpair-Annotation.
Only used man-auto textpairs.
Man text ==> good
Auto text ==> bad

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


def auto_sampling(in_file, out_file, korp):
    with open(in_file, "r") as pairl, open(out_file, "w") as out:
        c0 = 0
        c1 = 0
        for i in pairl:
            pattern = re.search("\(Text (\d+) -- Text (\d+)\)", i)
            if pattern:
                if korp[pattern.group(1)] == "man" and korp[pattern.group(2)] == "man":
                    continue
                elif korp[pattern.group(1)] == "auto_gut" and korp[pattern.group(2)] == "auto_gut":
                    continue
                elif korp[pattern.group(1)] == "auto_schlecht" and korp[pattern.group(2)] == "auto_schlecht":
                    continue
                elif korp[pattern.group(1)] == "man" and korp[pattern.group(2)] == "auto_gut":
                    continue
                elif korp[pattern.group(1)] == "auto_gut" and korp[pattern.group(2)] == "man":
                    continue
                elif korp[pattern.group(1)] == "auto_gut" and korp[pattern.group(2)] == "auto_schlecht":
                    continue
                elif korp[pattern.group(1)] == "auto_schlecht" and korp[pattern.group(2)] == "auto_gut":
                    continue
                elif korp[pattern.group(1)] == "man" and korp[pattern.group(2)] == "auto_schlecht":
                    out.write("Text " + pattern.group(1) + ", Text " + pattern.group(2) + "\t\t" + "0" + "\n")
                elif korp[pattern.group(1)] == "auto_schlecht" and korp[pattern.group(2)] == "man":
                    out.write("Text " + pattern.group(1) + ", Text " + pattern.group(2) + "\t\t" + "1" + "\n")

                    # elif korp[pattern.group(1)] == "man":
                    #     out.write("Text " + pattern.group(1)+", Text " + pattern.group(2)+"\t\t" + "1"+"\n")
                    #     c0 +=1
                    #     # print pattern.group(1), korp[pattern.group(1)], pattern.group(2), korp[pattern.group(2)]
                    # elif korp[pattern.group(2)] == "man":
                    #     c1 +=1
                    #     out.write("Text " + pattern.group(1)+", Text " + pattern.group(2)+"\t\t" + "0"+"\n")
                    #     # print pattern.group(1), korp[pattern.group(1)], pattern.group(2), korp[pattern.group(2)]
                    # else:
                    #     pass
                    #     # print pattern.group(1), korp[pattern.group(1)], pattern.group(2), korp[pattern.group(2)]
        pairl.close()
        out.close()
        print "0: ", c0
        print "1: ", c1
        print c0 + c1
        print float(c0) / float(44848)


def auto_filter_anno(in_file, out_file, korp):
    with open(in_file, "r") as pairl, open(out_file, "w") as out:

        for i in pairl:
            pattern = re.search("Text (\d+), Text (\d+)\t\t(\d)", i)
            if pattern:
                # print pattern.group(3)
                if korp[pattern.group(1)] == "man" and korp[pattern.group(2)] == "man":
                    out.write(
                        "Text " + pattern.group(1) + ", Text " + pattern.group(2) + "\t\t" + pattern.group(3) + "\n")
                    # elif korp[pattern.group(1)] == "auto_schlecht" and korp[pattern.group(2)] == "auto_schlecht":
                    #     out.write("Text " + pattern.group(1)+", Text " + pattern.group(2)+"\t\t" + pattern.group(3)+"\n")
                    # elif korp[pattern.group(1)] == "auto_gut" and korp[pattern.group(2)] == "auto_gut":
                    #     continue
                    # if korp[pattern.group(1)] == "man" and korp[pattern.group(2)] == "auto_schlecht":
                    #     out.write("Text " + pattern.group(1)+", Text " + pattern.group(2)+"\t\t" + pattern.group(3)+"\n")
                    # elif korp[pattern.group(1)] == "auto_schlecht" and korp[pattern.group(2)] == "man":
                    #     out.write("Text " + pattern.group(1)+", Text " + pattern.group(2)+"\t\t" + pattern.group(3)+"\n")
                    # elif korp[pattern.group(1)] == "auto_schlecht" and korp[pattern.group(2)] == "auto_gut":
                    #     out.write("Text " + pattern.group(1)+", Text " + pattern.group(2)+"\t\t" + pattern.group(3)+"\n")
                    # elif korp[pattern.group(1)] == "auto_gut" and korp[pattern.group(2)] == "auto_schlecht":
                    #     out.write("Text " + pattern.group(1)+", Text " + pattern.group(2)+"\t\t" + pattern.group(3)+"\n")
                    # elif korp[pattern.group(1)] == "auto_gut" and korp[pattern.group(2)] == "man":
                    #     out.write("Text " + pattern.group(1)+", Text " + pattern.group(2)+"\t\t" + pattern.group(3)+"\n")
                    # elif korp[pattern.group(1)] == "man" and korp[pattern.group(2)] == "auto_gut":
                    #     out.write("Text " + pattern.group(1)+", Text " + pattern.group(2)+"\t\t" + pattern.group(3)+"\n")
                    # else:
                    #     out.write("Text " + pattern.group(1)+", Text " + pattern.group(2)+"\t\t" + pattern.group(3)+"\n")
        pairl.close()
        out.close()


if __name__ == '__main__':
    korp_marked = "/home/jan/Development/Korpus/ZA/Finales_Korpus/Text_Korpus_aktuell_marked.txt"
    overall_pair_list = "/home/jan/Development/Anno/anno_2_0/31082015_Listendatei_aktuell.txt"
    pair_list = "/home/jan/Development/Korpus/ZA/test_sampling_anno.txt"
    anno_file = "/home/jan/Development/Korpus/ZA/Annotation/overall_annotation_100.txt"
    anno_file_ohne_80 = "/home/jan/Development/Korpus/ZA/Annotation/overall_annotation_without_80_20.txt"
    anno_file2 = "/home/jan/Development/Korpus/ZA/Annotation/overall_annotation_80_20pro.txt"
    jan_mel_equal = "/home/jan/Development/Korpus/ZA/Annotation/annotation_regular_equal_Jan_Mel.txt"
    korp = fill_dic(korp_marked)
    auto_sampling(overall_pair_list, "sampling_anno_man3.txt", korp)
    # auto_filter_anno(jan_mel_equal, "filter_anno_JMequal_man_man.txt", korp)


