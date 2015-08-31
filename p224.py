class Solution:
    # @param {string} s
    # @return {integer}
	def calculate(self, s):
		op = []
		nums = []
		index = 0
		length = len(s)
		#Out stack priorities
		out_priority = {'(':1, '+':0, '-':0, ')':2}
		#In stack priorities
		in_priority = {'(':2, '+':1, '-':1, ')':0}
		while index < length:
			while index < length and s[index] == ' ':
				index += 1
			num = 0
			sign = False
			while index < length and s[index] >= '0' and s[index] <= '9':
				num = num * 10 + int(s[index])
				index += 1
				sign = True
			if sign == True:
				nums.append(num)
			while index < length and s[index] == ' ':
				index += 1
			if index == length:
				break;
			#First In, second Out
			if op != [] and in_priority[s[index]] > in_priority[op[-1]]:
				op.append(s[index])
			elif op != []:
				while op != [] and out_priority[op[-1]] <= out_priority[s[index]]:
					if op[-1] == '+':
						nums[-2] = nums[-2] + nums[-1]
						nums.pop()
						op.pop()
					elif op[-1] == '-':
						nums[-2] = nums[-2] - nums[-1]
						nums.pop()
						op.pop()
					elif op[-1] == '(':
						op.pop()
						break
				if s[index] != ')':
					op.append(s[index])
			else:
				op.append(s[index])
			index += 1
		if op != []:
			if op[0] == '+':
				return nums[0] + nums[1]
			elif op[0] == '-':
				return nums[0] - nums[1]
		return nums[0]
s = "1+(1+1+1+(2+3-(4+5+5+6)+3+5+4))"
#s = "1 + (2 - 3)"
#s = "2147483647"
#s = "1+1+1+1"
so = Solution()
print so.calculate(s)