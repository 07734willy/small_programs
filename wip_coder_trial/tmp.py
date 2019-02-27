n = int(input())
b = 0
code = []
value = ["a","b","c","d","e","f","A","B","C","D","E","F","1","2","3","4","5","6","7","8","9","0","#"]
condition =[]
for _ in range(n):
    css = input()
    if(css == '{'):
        b = b+1
    elif(css == '}'):
        b = b-1
    if(b == 1):
        hashh = [j for j in range(len(css)) if(css[j]=="#")]
        for i in hashh:
            if(css[i+4].isalnum() == 0):
                code.append(css[i:i+4])
                continue
            try:
                if(css[i+7].isalnum() == 0):
                    code.append(css[i:i+7])
            except:
                continue

for i in range(len(code)):
    for j in code[i]:
        condition.append([j in value])
    if all(condition):
        print(code[i])
    del condition[:]
