'''
You are given a chunk of text.
Gather all capital letters in one word
in the order that they appear in the text. 
'''

def find_message(text):
    """Find a secret message"""
    message = []
    for i in text:
        if i.isupper():
            message.append(i)
    return ''.join(message)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert find_message("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO", "hello"
    assert find_message("hello world!") == "", "Nothing"
    assert find_message("HELLO WORLD!!!") == "HELLOWORLD", "Capitals"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
