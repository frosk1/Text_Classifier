import re

__author__ = 'jan'
# with open("Ax_fball_teaser.csv","r") as input, open("Ax_teaser_korpus_marked.txt", "w") as output:
#     c = 0
#     d = 0
#     for i in input.readlines():
#         if "##SCHLECHT##" in i:
#             d += 1
#             output.write(str(c)+"\t"+"auto_schlecht"+"\t" + i)
#         else:
#             output.write(str(c)+"\t"+"auto_gut"+"\t" + i)
#         c += 1
#     print "d", d
#     input.close()
#     output.close()

# with open("K_teaser_korpus.txt","r") as input, open("K_teaser_korpus_marked.txt","w") as output:
#     for i in input:
#         s = i.split("\t\t")
#         output.write(s[0]+"\t"+"man"+"\t"+s[1])
#     input.close()
#     output.close()

with open("K_teaser_korpus_marked.txt", "r") as input:
    for i in input:
        pattern = re.search("(\d+)\t(\w+.*)", i)
        if pattern:
            print pattern.group(2)
            # print re.split("\t",i)
