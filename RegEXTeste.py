import re
newtext = "The match in Germany"
x= re.search("^The.*Germany$", newtext)
if x:
    print("Yes! we have a match")
else:
    print("No match")

newnText ="The rain rain rain in Germany"
c = re.findall("ai", newnText)
print(c)
searching = re.search(r"\bG\w+", newtext)
print(searching)
print(searching.span())
print(searching.group())