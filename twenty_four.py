def list_result(l):
    if len(l) == 1:
        return [l]
    all_result = []
    for index,item in enumerate(l):
        r = list_result(l[0:index] + l[index+1:])
        print (l[0:index] + l[index+1:])
        # map(lambda x : x.append(item),r)
        # all_result.extend(r)
    return all_result

def func(x):
    return x*x

if __name__ == '__main__':
    l=[1,2,3]
    t=[4]
    index=2
    r=l[0:index] + l[index+1:]
    print (r)
    #print (l[0:index] + l[index+1:])
    map(lambda x:x.append(t),l)
    print (l)
    # r=map(func,l)
    # print (l)
    # print (list(r))
    #print (list_result(s))