a=input("")
a=a.lower()
b=""
tool_b=len(b)
tool_a=len(a)
i=tool_a-1
while i>=0 :
    b=b[:tool_b]+a[i]
    i=i-1
    tool_b=len(b)
if a==b:
    print("palindrome")
else:
    print("not palindrome")



