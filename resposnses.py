def sample_res(txt):
    file = open("all.txt", "r", encoding="utf8")
    x=file.read().split("\n")
    y=""
    for i in  range(len(x)):
        if txt in x[i]:
            y=x[i].replace(",","\n")
            return y

