

n=int(input())
s=input()

s1=s[:len(s)-n]
s2=s[len(s)-n:]
print(s2+s1)
