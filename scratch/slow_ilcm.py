# from problem #5

def slow_ilcm(li):
    vectors = dict([ (x,x) for x in li ])
    while any([ x != vectors.values()[0] for x in vectors.values()]):
        cur_min = min(vectors.items(), key = itemgetter(1))
        vectors[cur_min[0]] += cur_min[0]
    
    return vectors.values()[0]

# used to slightly speed up slow way 
def simplify(iterable):
    li = list(iterable)
    ret = list(iterable)
    for x in li:
        for y in li:
            if y <= x:
                continue
            if y % x == 0:
                ret.remove(x)
                break
    return ret
