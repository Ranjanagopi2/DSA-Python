def selectionsort(arr,n):
  for i in range(n):
    minimum=i
    for j in range(i+1,n):
      if arr[j]<arr[minimum]:
        minimum=j 
    arr[i],arr[minimum]=arr[minimum],arr[i]
  return arr 
arr=list(map(int,input().split()))
n=len(arr)
selectionsort(arr,n)
print(*arr)