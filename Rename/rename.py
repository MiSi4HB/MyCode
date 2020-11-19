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
        cName = input("추가할 문자열 : ")
        print("< 변경된 파일명 >")
        for filename in os.listdir(path):
            if filename.startswith("C"):
                ffname = filename.split(".")[0]
                fname = os.path.join(path, filename)
                nname = str(ffname) + str(cName) + '.txt'
                newname = os.path.join(path, nname)
                os.rename(fname, newname)
                print(ffname+cName+'.txt')
    else:
        continue
