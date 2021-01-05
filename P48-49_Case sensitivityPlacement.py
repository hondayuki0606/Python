
#2.3.12 大文字と小文字の区別、配置
setup = 'a duck goes into a bar...'
print(setup)

# 両端から.シーケンスを取り除こう
print(setup.strip('.'))

# 先頭のタイトルケース（先頭文字だけ大文字）にしよう
# A duck goes into a bar...
print(setup.capitalize())

# すべての単語をタイトルケースにするにはこうする。
# A Duck Goes Into A Bar...
print(setup.title())

# すべての文字を大文字にすることもできる。
# A DUCK GOES INTO A BAR...
print(setup.upper())

# 逆にすべての文字を変換するにはこうする。
# a docu goes into a bar...
print(setup.lower())

# 大文字小文字を逆にすることもできる。
# A DOCU GOES INTO A BAR...
print(setup.swapcase())

# 次に文字列のレイアウトを操作する関数を使ってみよう。これらの関数は、指定した
# スペース（ここでは30）のなかで文字列をド尿に配置するかを決める。
# 30文字分のスペースの中央に文字列を配置するには、次のようにする。
print(setup.center(30))

# こうすると左端に配置される。
print(setup.ljust(30))

# 右端にそろえることもできる。
print(setup.rjust(30))