array=[5,1,5,2,3,8]
data=2
def lsearch(arr,data):
    for i in range(len(arr)):
        if data==arr[i]:
            return i
    return -1
print(lsearch(array,data))

def bsearch(arr,element):
    l=0
    r=len(arr)-1
    index=-1
    while l<=r and index == -1:
        m= (l+r)//2
        if arr[m]==element:
            index=m

        else:
            if element<arr[m]:
                r=m-1
            else:
                l=m+1
        return index
def sorting(arr):
    for i in range(1,len(arr)):
        elem=arr[i]
        k=i-1
        while k>=0 and elem<arr[k]:
            arr[k+1]=arr[k]
            k-=1
        arr[k]+=1