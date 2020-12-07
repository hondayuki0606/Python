# join関数はsplit関数の逆の関数でリストを任意の文字列で結合する。
# string.join(list)という形式でまずは挟む文字列を指定してから、結合する文字列のリストを指定する
crypto_list = ['Yeti','Bigfoot','Loch Nes Monster']
crypto_str = ', '.join(crypto_list)
print('Found and signing book deals:', crypto_str)