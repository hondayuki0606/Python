
#2.3.11 多彩な文字列操作
poem = '''All that coth flow er cannot liwuid name
Or else would fire and water be tha same;
Fire that propetry can never get.
Then 'tis not cold that doth the fire put out
But 'tis the wet that makes it die, no doubt, '''
print(poem)

print(' 手始めに最初の13文字（オフセット）を取り出そう')
print(poem[:13])

print(' この詩には何文字含まれているかを取り出そう')
print(len(poem))

print('先頭はAllになっているだろうか')
print(poem.startswith('All'))

print('末尾はmakes it die, no doubt, になっているだろうか')
print(poem.endswith('makes it die, no doubt, '))

print('詩の中でtheという単語は最初に現れる箇所のオフセットを調べてみよう')
word = 'the'
print(poem.find('the'))

print('そして、最後のtheのオフセットもわかる')
print(poem.rfind('the'))

print('theという文字は何回現れているんだろう')
print(poem.count('the'))

print('この詩に含まれる文字はすべて英字か数字になっているか')
print(poem.isalnum)
