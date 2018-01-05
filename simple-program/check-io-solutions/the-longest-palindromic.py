def longest_palindromic(text):
    for i in range(len(text), 0, -1):
        print('Checking len = {}'.format(i))
        for k in range(0, len(text) - i + 1):
            print('...',text[k:k+i],'...',text[k:k+i][::-1])
            if text[k:k+i] == text[k:k+i][::-1]:
                print('... and Done.')
                return text[k:k+i]
    print('failed')
    return text[0]

longest_palindromic("artrartrt")
'''
if __name__ == '__main__':
    assert longest_palindromic("artrartrt") == "rtrartr", "The Longest"
    assert longest_palindromic("abacada") == "aba", "The First"
    assert longest_palindromic("aaaa") == "aaaa", "The A"
    '''
