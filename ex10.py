message = "Hello my little friends!"
offset = 37
encoded_message = ""
ord_a = ord('a')
ord_A = ord('A')
for ch in message:
    if str.isalpha(ch):
        if str.istitle(ch):
            pos = ord(ch) - ord_A
            pos = (pos + offset) % 26
            encoded_message += chr(pos + ord_A)
        else:
            pos = ord(ch) - ord_a
            pos = (pos + offset) % 26
            encoded_message += chr(pos + ord_a)
    else:
        encoded_message += ch

print(encoded_message)

for i in range(90, 98):
    print(chr(i))