def convert(s:str):
    res=list(s)
    for i in range(len(res)):
        if res[i].isdigit():
            res[i]="number"
    return "".join(res)

s=input()
print(convert(s))

