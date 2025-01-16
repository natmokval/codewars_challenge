# https://www.codewars.com/kata/52f677797c461daaf7000740/python
# Smallest possible sum

def solution(lst):
    ln = len(lst)
    while len(lst)  > 1:
        lst = func(lst)
    return lst[0] * ln

def func(lst):
    tmp = list(set(lst))
    tmp.sort()
    return [tmp[0] if tmp[i]%tmp[0] == 0 else tmp[i]%tmp[0] for i in range(len(tmp))]
