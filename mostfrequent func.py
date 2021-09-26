s='mississippi'

def most_frequent(s):
    d= dict()
    for key in s:
        if key not in d:
            d[key] = 1
        else:
            d[key] += 1

    sort_d = sorted(d.items(), key=lambda x:x[1], reverse=True)

    for i in sort_d:
            print(i[0],'=',i[1])
print(most_frequent(s))
