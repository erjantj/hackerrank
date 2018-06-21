import sys 

def fib(k, n, memo):
	if n == 0:
		return 1	
	if n == 1:
		return 1	
	mmin = min(k, n)
	f = 0
	if n in memo:
		return memo[n]

	for i in range(1, mmin+1):
		f += fib(mmin, n-i, memo)

	memo[n] = f
	return f

with open('INPUT.TXT') as f:
	content = f.readlines()
	k,n = [int(x) for x in content[0].strip().split()]
	memo = {}
	result = fib(k,n, memo)
	orig_stdout = sys.stdout
	f = open('OUTPUT.TXT', 'w')
	sys.stdout = f
	print(result)
	sys.stdout = orig_stdout
	f.close()