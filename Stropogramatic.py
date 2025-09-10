n=int(input())
def stropo(n):
  m=str(n)
  k=len(m)
  mapp={'0':'0','1':'1','6':'9','9':'6','8':'8'}
  for i in range((k+1)//2):
    left=m[i]
    right=m[k-1-i]
    if left not in mapp or mapp[left]!=right:
      return False
    return True
print(stropo(n))
#time complexity-O(n)
#space complexity-O(1)