def next_greater_element_idx(arr, n):
    stk = []
    res = [-1]*n
    i = n-1
    while i>=0:
        while stk and arr[stk[-1]]<arr[i]:
            stk.pop(-1)
        if len(stk) == 0:
            res[i] = -1
        else:
            res[i] = stk[-1]
        stk.append(i)
        i-=1
    return res
def next_greater_element(arr, n):
    stk = []
    res = [-1]*n
    i = n-1
    while i>=0:
        while stk and stk[-1]<arr[i]:
            stk.pop(-1)
        if len(stk) == 0:
            res[i] = -1
        else:
            res[i] = stk[-1]
        stk.append(arr[i])
        i-=1
    return res
def display(arr, n):
    for i in range(n):
        print(arr[i],end=" ")
    print()
arr = [3,1,4,5,6]
n = len(arr)
res_arr = next_greater_element(arr, n)
display(res_arr, n)
res_arr = next_greater_element_idx(arr, n)
display(res_arr, n)