#Program to find out the enter character is vowel or consonant

l = input("Input a letter of the alphabet: ")

if l in ('a', 'e', 'i', 'o', 'u' and 'A', 'E', 'I', 'O', 'U' ):
	print("%s is a vowel." % l)
#elif l == 'y':
	#print("Sometimes letter y stand for vowel, sometimes stand for consonant.")
else:
	print("%s is a consonant." % l)
