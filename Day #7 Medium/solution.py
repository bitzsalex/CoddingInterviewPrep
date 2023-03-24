# given encoded messages
a = '111'
b = '11101'
c = '123'
d = '18910'

def decoder(message: str):
    length = len(message)
    if message and (message[0] == '0' or message[0] not in "123456789"):
        return 0
    
    if length <= 1:
        return 1
    
    # doing the double split first
    char_code = int(message[:2], 10)
    if char_code > 0 and char_code < 27:
        return decoder(message[1:]) + decoder(message[2:])
            
    return decoder(message[1:])
    

print(decoder(a))
print(decoder(b))
print(decoder(c))
print(decoder(d))

# reference: https://javascript.plainenglish.io/facebook-coding-interview-questions-9e40bdbbec35