# encoding=utf-8
import io

f = io.open('abc.txt', 'wt', encoding='utf-8')
f.write(u'Imagin non-English language here like this: 卧槽')
f.close()

text = io.open('abc.txt', encoding='utf-8').read()
print(text)