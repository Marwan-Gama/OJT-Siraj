s='seehemwe'

#q2
print(s[:3])
print(s[3:5])
print(s[-3:-5:-1])
print(s[7:])
print(s[4:7:2])
print(s[-1:-6:-1])
print(s[-2:0:-2])

#q2
def balendrom(s):
    if s[:len(s)+1] == s[-1:0:-1]:
        return True
    else:
        return False

print(balendrom("level"))

