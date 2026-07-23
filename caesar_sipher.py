def caeser(msg,shift):
    result=""
    for i in msg:
        if i.isalpha():
            if i.isupper():
             position=ord(i)-ord('A')
             n=(position+shift)%26
             new_letter= chr(n+ord('A'))
            elif i.islower():
             position=ord(i)-ord('a')
             n=(position+shift)%26
             new_letter= chr(n+ord('a'))
            result+=new_letter
        else:
            result+=i
    print(result)
message=input("enter a message:")
shifting_value=int(input("enter the value of shifts you want:"))
caeser(msg=message,shift=shifting_value)