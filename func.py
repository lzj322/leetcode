
def power(x,n=2):
	return x*x
def person(name, age, **kw):
	print 'name:',name,'age:', age, 'other:', kw
def func(a, b, c=0, *args, **kw):
	print 'a=', a, 'b=', b, 'c=', c, 'args=',args, 'kw=',kw

# print power(5)
# person('Michael',30)
# person('Bob',35, city = 'Beijing')
# func(1,2)
# func(1,2,c=3)
# func(1,2,3,'a','b')
# func(1,2,3,'a','b',x=99)
L= ['Michael','Sarah','Tracy','Bob','Jack']
print L[:3]
for i,word in enumerate(L):
	print i,word
pp=[x*x for x in range(1,11)]
print pp

d={'x':'A','y':'B','z':'C'}
for k,v in d.iteritems():
	print k,'=',v
[s.lower() for s in L]

#generator
g=(x*x for x in range(10))
for n in g:
	print n