import sys
infodict={}
students = open(sys.argv[1],"r").readlines()
name = sys.argv[2].split(",")
for i in students:
    i =i.split(":")
    infodict[i[0]] = i[1]
for i in name:
    try:
        print("Name: {}, University: {}".format(i,infodict[i]), end="")
    except:
        print("No record of '{}' was found".format(i))
