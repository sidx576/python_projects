# def partition(arr,start,end):
#     # mid=start+(end-start)//2
#     pivot=arr[start]
  
#     i=start+1
#     j=end

#     while i<=j:

#         while i<=j and arr[i]<=pivot:
#             i+=1

#         while i<=j and arr[j]>=pivot:
#             j-=1
        
        

#         # else swap
#         if i<=j:
#             arr[i], arr[j]=arr[j], arr[i]
          

#         # else:
#         #     break
#         # print(pivotInd)
#     arr[start],arr[j]=arr[j],arr[start]
#     return j


def partit(arr,start,end):
    pivot=arr[start]
    low=start+1
    high=end
    # m=start+(end-start)//2
    

    while low<=high:

        # also a reason why if already sorted it will not swap
        while low<=high and arr[low]<=pivot:
            low+=1

        while low<=high and arr[high]>=pivot:
            high-=1

        if(low<=high):
            arr[low],arr[high]=arr[high],arr[low]
            

    arr[start],arr[high]=arr[high],arr[start]
    return high




def quick_sort(arr,start,end):
    # start = 0
    # end=len(arr)-1

    #Base case
    if start>=end:
        return 
    
    #Partition
    p=partit(arr,start,end)

    # print(p)
    # left sorting
    quick_sort(arr,start,p-1)
    # right sorting
    quick_sort(arr,p+1,end)
    
    return arr


arr=[5,4,3,2,1,6,9,8,5,4,-2,-4,-6,-8,-3]
quick_sort(arr,0,len(arr)-1)
