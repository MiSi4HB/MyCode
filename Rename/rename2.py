import os
i = "start"
path = '/Users/minseo/work/HelloWatch/py/raw/rename/'
print("ls - 파일확인 / rn - 파일명변경 / exit - 종료")
while (i != "exit"):
    i = input(path + " >> ")
    if i == "exit":
        exit
    elif i == "ls":
        print("< 파일명 >")
        for filename in os.listdir(path):
            print(filename)
    elif i=="rn":
        dName = input("변경할 부분 : ")
        cName = input("추가할 문자 : ")
        print("< 변경된 파일명 >")
        for filename in os.listdir(path):
                ffname = filename.split(dName)[0]
                sname = filename.split(dName)[1]
                fname = os.path.join(path, filename)
                nname = str(ffname) + str(cName) + str(sname)
                newname = os.path.join(path, nname)
                os.rename(fname, newname)
                print(nname)
    else:
        continue
