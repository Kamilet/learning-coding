# wrong.. $5.34 → $5.34 .. dont really understand
def checkio(text):
    text = text.split(' ')
    _text = []
    for items in text:
      if items[0] == '$':
        _temp = []
        _maxp = 0
        for i in range(len(items)-1):
          if items[i] == '.' or items[i] == ',':
            _maxp = i
            _temp.append(items[i])
        if (len(_temp) > 1 and _temp[0][0] == ',') or (len(_temp) == 1 and _temp[0][0] == '.' and len(_temp[0])-i == 3):
          print('ppp')
          _text.append(items)
        else:
          _temp = []
          for i in range(len(items)-1):
            if items[i] == '.':
              _temp.append(',')
            elif items[i] == ',':
              _temp.append('.')
            else:
              _temp.append(items[i])
          _temp.append(items[-1])
          _text.append(''.join(_temp))
      else:
        _text.append(items)
    print(' '.join(_text))
    return ' '.join(_text)

if __name__ == '__main__':    

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("$1.234.567,89") == "$1,234,567.89" , "1st Example"
    assert checkio("$0,89") == "$0.89" , "2nd Example"
    assert checkio("Euro Style = $12.345,67, US Style = $12,345.67") == \
                   "Euro Style = $12,345.67, US Style = $12,345.67" , "European and US"
    assert checkio("Us Style = $12,345.67, Euro Style = $12.345,67") == \
                   "Us Style = $12,345.67, Euro Style = $12,345.67" , "US and European"
    assert checkio("$1.234, $5.678 and $9") == \
                   "$1,234, $5,678 and $9", "Dollars without cents"
    assert checkio("$5.34") == '$5.34'

'''wrong
def checkio(text):
    _flag = False
    _flag_2 = False
    _text = []
    for _p in range(len(text)-1):
      if text[_p] == '$': _flag = True
      elif text[_p] == ' ' or text[_p+1] == ' ' : _flag = False
      if _flag:
        if text[_p] == '.':
          _text.append(',')
          _flag_2 = True
        elif text[_p] == ',':
          if _flag_2:
            _text.append('.')
          else:
            _text.append(text[_p])
            _flag = False
            _flag_2 = False
        else: _text.append(text[_p])
      else: _text.append(text[_p])
    _text.append(text[-1])
    print(''.join(_text))
    return ''.join(_text)
'''
