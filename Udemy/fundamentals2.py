#multiplication, division, an exponent, addition, and subtraction that is equal to 100.25
print(0.25 + (25/5) + (5**3) - 30)
print(2/3)
print(3 + 1.5 + 4)
s = 'hello'
print(s[1])
print(s.index('e'))
print(s[::-1])

print([0]*3)
l = [1,2,[3,4,'hello']]
l[2][2]="goodbye"
print(l)
l = [5,3,4,6,1]
l.sort()
print(l)

d = {'simple_key':'hello'}
print(d['simple_key'])
d = {'k1':{'k2':'hello'}}
print(d['k1']['k2'])
d = {'k1':[{'nest_key':['this is deep',['hello']]} ] }
print(d['k1'][0]['nest_key'][1][0])
d = {'k1':[1,2, {'k2':['this is tricky',{'tough':[1,2,['hello']] } ] } ] }
print(d['k1'][2]['k2'][1]['tough'][2][0])