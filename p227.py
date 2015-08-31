class Solution:
    # @param {string} s
    # @return {integer}
	def calculate(self, s):
		in_priority = {'+': 0, '-': 0, '*': 1, '/': 1}
		index = 0
		length = len(s)
		nums = []
		nums.append(1)
		op = []
		op.append('*')
		while index < length:
			num = 0
			while index < length and s[index] == ' ':	index += 1
			while index < length and s[index] >= '0' and s[index] <= '9':
				num = num * 10 + int(s[index])
				index += 1
			#print num
			while index < length and s[index] not in in_priority:
				index += 1
			if index == length:
				nums.append(num)
				break
			#print s[index]
			if in_priority[op[-1]] >= in_priority[s[index]]:
				#print " "
				#print nums[-1],num
				if op[-1] == '+' or op[-1] == '-':
					op.append(s[index])
					nums.append(num)
				elif op[-1] == '*':
					nums[-1] = nums[-1] * num
					op[-1] = s[index]
				elif op[-1] == '/':
					if num != 0:
						nums[-1] = nums[-1] / num
					op[-1] = s[index]
				else:
					print 'Error' + op[-1]
				
			else:
				op.append(s[index])
				nums.append(num)
			#print nums[-1]
			index += 1
		if op[-1] == '*':
			nums[-2] = nums[-2] * nums[-1]
			nums.pop()
			op.pop()
		elif op[-1] == '/':
			if nums[-1] != 0:
				nums[-2] = nums[-2] / nums[-1]
			nums.pop()
			op.pop()
		#print nums[0]
		for i in xrange(0, len(op)):
			#print nums[i+1]
			if op[i] == '+':
				nums[0] = nums[0] + nums[i+1]
			elif op[i] == '-':
				nums[0] = nums[0] - nums[i+1]
			else:
				print 'Error in op stack'
		#if len(nums) != 1:	print 'Error'
		return nums[0]
s = "282-1*2*13-30-2*2*2/2-95/5*2+55+804+3024"
so = Solution()
print so.calculate(s)