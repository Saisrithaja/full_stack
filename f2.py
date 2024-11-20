def palindrome(n):
    temp=str(n)
    if temp== temp[::-1]:
        print("palindorome")
    else:
        print("Not a palindrome")

palindrome(45)