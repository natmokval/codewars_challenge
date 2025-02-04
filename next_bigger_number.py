# https://www.codewars.com/kata/55983863da40caa2c900004e/python
# Next bigger number with the same digits

def next_bigger(n):
    arr = [str(n)[i] for i in range(len(str(n)))]
    for i in range(len(arr)-1, 0, -1):
        tail = arr[i:]
        if arr[i] > arr[i-1]:
            tail.sort()
            for n, j in enumerate(tail):
                if j > arr[i-1]:
                    arr[i-1], tail[n] = tail[n], arr[i-1]
                    tail.sort()
                    return int("".join(arr[:i] + tail))
    return -1
