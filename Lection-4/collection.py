import collections
c = collections.Counter()
for word in ['spam', 'egg', 'spam', 'counter', 'counter', 'counter']:
	c[word] += 1

print(c)

print(c['counter'])

print(c['collections'])

c = collections.Counter(a=4, b=2, c=0, d=-2)

print(list(c.elements()))

c.clear()

print(collections.Counter('abracadabra').most_common(3))

c = collections.Counter(a=3, b=1)

d = collections.Counter(a=1, b=2, c=2)

print(c + d)