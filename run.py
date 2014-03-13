#!/usr/bin/python
# encrypt a couple messages

key  = 'sillysecret'
msg1 = 'Hello world'
msg2 = 'the program'
enc1 = bytearray([ord(x) ^ ord(y) for x, y in zip(key, msg1)])
enc2 = bytearray([ord(x) ^ ord(y) for x, y in zip(key, msg2)])

# try crib dragging, given enc1 and enc2

msgxor = bytearray([x ^ y for (x, y) in zip(enc1, enc2)])
crib = bytearray('guess me!')

for i in range(len(msgxor)):
  xord = bytearray()
  for j in range(len(crib)):
    if i+j < len(msgxor):
      xord.append(msgxor[i+j] ^ crib[j])
    else:
      break
  
  print str(xord)
