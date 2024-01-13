from math import sqrt
maxx = 9
block_size = 3
arr = [0]*maxx
block = [float("inf")]*block_size
blk_ind = 0
def update(ind, val):
    if val<=block[ind//block_size]:
        block[ind//block_size] = val
        arr[ind] = val
        print(arr)
    else:
        arr[ind] = val
        start_ind = ind-(ind%block_size)
        end_ind = start_ind + block_size
        min_val = float("inf")
        while start_ind<=end_ind:
            min_val = min(min_val, arr[start_ind])
            start_ind += 1
        block[ind//block_size] = min_val
        print(arr)
def query(l,r):
    res = float("inf")
    while l<r and l%block_size != 0 and l!=0:
        res = min(res, arr[l])
        l+=1
    while l+block_size-1 <= r:
        res = min(res, block[l//block_size])
        l += block_size
    while l<=r:
        res = min(res, arr[l])
        l+=1
    return res
def preprocess(input, n):
    blk_ind = -1
    global block_size 
    block_size = int(sqrt(n))
    for i in range(n):
        arr[i] = input[i]
        if i%block_size == 0:
            blk_ind += 1
        block[blk_ind] = min(input[i], block[blk_ind])
    
            
            
input = [7, 2, 3, 0, 5, 10, 3, 12, 18]
n = len(input)
preprocess(input, n)
print(block)
print("query(1,6)->",query(1,6))
print("query(3,7)->",query(3,7))
print("query(4,8)->",query(4,8))
update(3,5)
print("query(3,7)->",query(3,7))
