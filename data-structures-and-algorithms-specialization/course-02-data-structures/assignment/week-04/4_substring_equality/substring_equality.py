# python3

import sys

class Solver:
	def __init__(self, s):
		self.s = s
		self.m1 = (10 ** 9) + 7
		self.m2 = (10 ** 9) + 9
		self._multiplier = 263

		self.h1 = self.hashfunc(self.m1)
		self.h2 = self.hashfunc(self.m2)

	def hashfunc(self, m):
		hashes = [0] * (len(self.s) + 1)
		for i in range(1, len(self.s) + 1):
			hashes[i] = (hashes[i-1] * self._multiplier + ord(self.s[i-1])) % m
		return hashes

	def ask(self, a, b, l):
		pow1 = pow(self._multiplier, l, self.m1)
		ha = (self.h1[a+l] - (pow1 * self.h1[a]) + self.m1) % self.m1
		hb = (self.h1[b+l] - (pow1 * self.h1[b]) + self.m1) % self.m1
		if ha != hb:
			return False

		pow2 = pow(self._multiplier, l, self.m2)
		ha = (self.h2[a+l] - (pow2 * self.h2[a]) + self.m2) % self.m2
		hb = (self.h2[b+l] - (pow2 * self.h2[b]) + self.m2) % self.m2
		if ha != hb:
			return False
		
		return True

s = sys.stdin.readline()
q = int(sys.stdin.readline())
solver = Solver(s)
for i in range(q):
	a, b, l = map(int, sys.stdin.readline().split())
	print("Yes" if solver.ask(a, b, l) else "No")
