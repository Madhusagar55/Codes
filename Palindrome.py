s = input("Enter a name:")
           
rev = ""

for ch in s:
    rev = ch + rev
    print(rev)
    
if s == rev:
    print("Palindrome")
else:
    print("Not Palindrome")