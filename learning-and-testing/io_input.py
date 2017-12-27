def reverse(text):
	return text[::-1]

def is_palindrome(text):
	return text == reverse(text)

something = input('Enter text: ')	#关于是否是回文的判断
if is_palindrome(something):
	print("Yes, it is a palindrome")
else:
	print('No, it is not a palindrome')