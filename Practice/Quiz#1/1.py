text = input().split()
vowels = ['a', 'o', 'e', 'i', 'u', 'y']

def change(s):
	if s[0] in vowels:
		return (s + 'yay')
	else:
		for i in range(len(s)):
			if s[i] in vowels:
				return (s[i:] + s[:i] + 'ay')

for word in text:
	print(change(word))