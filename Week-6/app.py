def xbonacci(sig,n):
  result = []
  result += sig
  x = len(sig)

  if x > n:
    return sig[-n:]


  for i in range (x,n):
    next_item = sum(result[-x:])
    result.append(next_item)

  return result

#test
print(xbonacci([1,1],10))
print(xbonacci([1,1,1],8))
print(xbonacci([1,1,1,1],10))
print(xbonacci([0,0,0,0,1],10))
