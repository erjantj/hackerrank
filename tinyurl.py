import hashlib,base64

url = 'https://hipo.kz/post/askhat-murzabaev-soosnovatel-hipo-i-petrel-ai-o-biznese-sporte-kak-obraze-zhizni-i-dostizhenii-tselei/'.encode('utf-8')

m = hashlib.md5(url)
url_hash = m.hexdigest()

print(url_hash)

encoded = base64.b64encode(str.encode(url_hash))

print(encoded)