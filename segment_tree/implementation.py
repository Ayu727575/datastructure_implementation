
class SegmentTree:
    def __init__(self, ar):
        self.arr = ar
        self.tree = [0]*(4*len(self.arr))
        self.build(1,0,len(self.arr)-1)
    
    def build(self,node, start, end):
        if start == end:
            self.tree[node] = self.arr[start]
            return
        mid = (start+end)//2
        left = node*2
        right = node*2+1
        self.build(left,start,mid)
        self.build(right,mid+1,end)
        self.tree[node] = max(self.tree[left],self.tree[right])
    
    def query(self,node,start,end,l,r):
        if l>end or r<start: return float("-inf")
        if start == end:
            return self.tree[node]
        elif start >= l and end <= r:
            return self.tree[node]
        else:
            mid = (start+end)//2
            left = self.query(node*2,start,mid,l,r)
            right = self.query(node*2+1,mid+1,end,l,r)
            return max(left,right)
nums = [8,7,4,2,5,3,1,10]
obj = SegmentTree(nums)
range = list(map(int,input().strip(" ").split()))
print(obj.query(1,0,len(nums)-1,range[0],range[1]))