#!/bin/python3

import sys

def count(c,t,pices, p, memo):

with open('input.txt') as f:
	content = f.readlines()
	n = int(content[0].strip())
	pices = [1,3,5]

	i = 1
	for k in range(n):
		t = int(content[i].strip())
		i+=1
		c = [int(x) for x in content[i].strip().split()]
		i+=1
		memo = [0]*t
		count(c,t-1 ,pices, 0, memo)
		print(memo)