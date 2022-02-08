def dummyDfs(n):
	def dfs(used, left, n, stack, ans):
		if left < 0:
			return
		if len(stack) == n * 2:
			ans.append("".join(stack))
			return
		for i in range(2 * n):
			if i > 0 and i != n and not (used & (1 << (i - 1))):
				continue
			if not (used & (1 << i)):
				c = "(" if i < n else ")"
				stack.append(c)
				dfs(used | (1 << i), left + 1 if i < n else left - 1, n, stack, ans)
				stack.pop()

	ans = []
	dfs(0, 0, n, [], ans)
	return ans

print(dummyDfs(1))
print(dummyDfs(2))
print(dummyDfs(3))

def simpleDfs(n):
	def dfs(l, r, s, ans):
		# r and l are remaining stack size, opposition to string size
		if r < l:
			return
		if not r and not l:
			ans.append(s)
			return

		if l:
			dfs(l - 1, r, s + "(", ans)
		if r:
			dfs(l, r - 1, s + ")", ans)

	ans = []
	dfs(n, n, "", ans)
	return ans

print(simpleDfs(1))
print(simpleDfs(2))
print(simpleDfs(3))



