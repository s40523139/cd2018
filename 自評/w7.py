with open("w7.txt", "r", encoding="utf-8") as fh :
    #打開存有出席狀況的w7.txt
    lines = fh.readlines()
    raw_date = lines[1:]
    #將資料放入數列
    #print(raw_date)
    #測試檔案開得起來
    k = []
    #讓k為學號字串，但先令k為空的字串
    for i in range(len(raw_date)):
        nb =  raw_date[i].strip()
        #消除跳行符號
        #groups = nb.strip("/t")
        groups = nb.split("\t")
        #上面是這次找到奇怪的地方
        #print(groups)
        #測試，結果為總出席與當日出席對照
        for j in range(len(groups)):
            if groups[j] != "" :
                k.append(groups[j])
                #將w7.txt放入k字串中
absent = [i for i in k if k.count(i) == 1]
#absent = [i for i in k if k.count(i) == 1]
#找出只在k字串中出現一次的字串
print(absent)
#顯示缺席(absent)