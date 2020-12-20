
#2.3.12 大文字と小文字の区別、配置
setup = 'a duck goes into a bar...'
print(setup)

# 両端から.シーケンスを取り除こう
print(setup.strip(.))

# 先頭のタイトルケース（先頭文字だけ大文字）にしよう
# A Duck Goes Into A Bar...
print(setup.capitalize)