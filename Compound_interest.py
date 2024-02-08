p,r,t = map(int,input().split())
c = (1 + (r/100))**t;
cp = c*p;
print("%.2f" %cp)