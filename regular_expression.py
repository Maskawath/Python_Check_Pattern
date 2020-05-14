import re

pattern = re.compile(r"\d\d\d.\d\d\d.\d\d\d\d")

try:
	with open ("data.txt" , "r", encoding="utf-8") as f:
		contents = f.read()
		matches= pattern.finditer(contents)
		for match in matches:
			print(match)
except IOError:
    print ("Could not read file:", f)