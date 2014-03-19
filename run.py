#!/usr/bin/python
import sys
import string
asciionly = lambda str: str.translate(''.join([['.', chr(x)][chr(x) in string.printable[:-5]] for x in range(256)]))
# encrypt a couple messages

key  = "8J1Cxg0GBHbjhQFv7R9OllOK2JPIhzvgX6kvN2UcA"
msg1 = "What would you do if you were not afraid?"
msg2 = "The start is what often stops most people"

guess = "people"

if not len(key) == len(msg1) == len(msg2):
  sys.exit("The key and messages should all be the same length.")

enc1 = bytearray([ord(x) ^ ord(y) for x, y in zip(key, msg1)])
enc2 = bytearray([ord(x) ^ ord(y) for x, y in zip(key, msg2)])

print "As a cryptologist, all you know about the situation is the encrypted form of the messages. You assume they used the same OTP."
print "Msg 1: %s" % asciionly(enc1)
print "Msg 2: %s" % asciionly(enc2)
print
print "You want to guess a value that's in either message. If it is in fact in either, you'll get the plain-text of the string in the _other_ message."
print "Guessing: %s" % guess
# try crib dragging, given enc1 and enc2

msgxor = bytearray([x ^ y for (x, y) in zip(enc1, enc2)])
crib = bytearray(guess)

for i in range(len(msgxor)-len(crib)+1):
  xord = bytearray()
  for j in range(len(crib)):
      xord.append(msgxor[i+j] ^ crib[j])
  
  print asciionly(xord)

print
print "Does any of the above look correct? If so, guess what text might be around it. If that guess is right, you'll get the plain-text in the string you first guessed right (that's now the other message)."
