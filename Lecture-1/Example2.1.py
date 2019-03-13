import os.path
import sys

def main ():
	keyWords = {"and" : 0, "as" : 0, "assert" : 0, "break" : 0, "class" : 0,
				"continue" : 0, "def" : 0, "del" : 0, "elif" : 0, "else" : 0,
				"expect" : 0, "False" : 0, "finally" : 0, "for" : 0, "from" : 0,
				"global" : 0, "if" : 0, "import" : 0, "in" : 0, "is" : 0, "lambda" : 0,
				"None" : 0, "nonlocal" : 0, "not" : 0, "or" : 0, "pass" : 0, "raise" : 0,
				"return" : 0, "True" : 0, "try" : 0, "while" : 0, "with" : 0, "yield" : 0}
	filename = input("Enter a Python source code filename: ").strip()
	if not os.path.isfile(filename):
		print("File", filename, "does not exist")
		sys.exit()
	
	infile = open(filename, "r")
	
	text = infile.read().split()
	count = 0
	for word in text:
		if word in keyWords:
			keyWords[word] += 1
	for word in keyWords:
		print(word, ":", keyWords[word])
main()