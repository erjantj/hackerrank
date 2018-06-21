s = 'xacxzaa'
b = 'fxaazxacaaxzoecazxaxaz'

len_s = len(s)
len_b = len(b)

freqs_a = {}
prems = 0

for i in s:
	if i not in freqs_a:
		freqs_a[i] = 0
	freqs_a[i] = freqs_a[i] + 1

for i in range(0,(len_b-len_s)+1):
	token = b[i:(i+len_s)]

	freqs_token = {}

	for i in token: 
		if i not in freqs_token:
			freqs_token[i] = 0
		freqs_token[i] = freqs_token[i] + 1

	match = True

	for k,i in freqs_a.items():
		if k not in freqs_token:
			match = False
		elif freqs_token[k] != i:
			match = False

	if match:
		print(token)
		prems = prems+1

print(prems)