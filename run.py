#!/usr/bin/python
import sys

# encrypt a couple messages

key  = 'sillysecret'
msg1 = 'Hello world'
msg2 = 'the program'
guess = 'the'

if not len(key) == len(msg1) == len(msg2):
  sys.exit("The key and messages should all be the same length.")

enc1 = bytearray([ord(x) ^ ord(y) for x, y in zip(key, msg1)])
enc2 = bytearray([ord(x) ^ ord(y) for x, y in zip(key, msg2)])

print "As a cryptologist, all you know about the situation is the encrypted form of the messages (and that they were encrypted with the same OTP)"
print "Msg 1: %s" % enc1
print "Msg 2: %s" % enc2
print
print "You want to guess a value that's in either message. If it is in fact in either, you'll get the plain-text of the string in the _other_ message."
print "Guessing: %s" % guess
# try crib dragging, given enc1 and enc2

msgxor = bytearray([x ^ y for (x, y) in zip(enc1, enc2)])
crib = bytearray(guess)

for i in range(len(msgxor)):
  xord = bytearray()
  for j in range(len(crib)):
    if i+j < len(msgxor):
      xord.append(msgxor[i+j] ^ crib[j])
    else:
      break
  
  print str(xord)

print
print "Does any of the above look correct? If so, guess what text might be around it. If that guess is right, you'll get the plain-text of the string you first guessed right in (that's now the other message)."
