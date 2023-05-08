l,m,n=map(int,input().split())
p=(l+m+n)/2
a=(p*(p-l)*(p-m)*(p-n))**0.5
print("%.2f" %a)
