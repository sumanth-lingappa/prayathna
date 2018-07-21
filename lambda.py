
mx = lambda x,y: x if x>y else y

print mx(8,5)

n = [4,3,2,1]

print reduce(mx, n)
