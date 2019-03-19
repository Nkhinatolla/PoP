import collections
c = collections.Counter()
print(c)

words = ['spam', 'egg', 'spam', 'counter', 'counter', 'counter']
for word in words:
	c[word] += 1
print(c)
print(c)
print(c['counter'])

print(c['collections'])

c = collections.Counter(a=4, b=2, c=0, d=-2)
print("-----")
print(collections.Counter(list(c.elements())))
print(collections.Counter([2, 4, 5, 4]))
c.clear()

print(collections.Counter('abracadabra').most_common())

c = collections.Counter(a=3, b=1)

d = collections.Counter(a=1, b=2, c=2)

print(c + d)