class Solution:
    # @param {string} s
    # @param {string} p
    # @return {boolean}
	def isMatch(self, s, p):
		#print s,p
		if len(p) == 0 or p[0] == '#':
			if len(s) == 0 or s[0] == '#':
				return True
			else:	return False
		if len(s) == 0 or s[0] == '#':
			if p[-1] == '#':	p = p[0:-1]
			if len(p) < 2: return False
			p_len = len(p)
			if p_len % 2 != 0:	return False
			index = 1
			while index < p_len:
				if p[index] != '*':	return False
				index += 2
			return True
		if s[-1] != '#':
			s = s + '#'
			p = p + '#'
		#print s, p
		p_pos = 0
		s_pos = 0
		p_len = len(p)
		s_len = len(s)
		hash = [False for i in xrange(0,128)]
		while p_pos < p_len and s_pos < s_len:
			#Not end and next character is not *
			if p_pos + 1 < p_len and p[p_pos+1] != '*':
				if p[p_pos] == '.':
					p_pos += 1
					s_pos += 1
				else:
					if s[s_pos] == p[p_pos]:
						s_pos += 1
						p_pos += 1
						
					else:
						
						return False
			#end
			elif p_pos == p_len - 1:
				if s[s_pos] == '#':
					return True
				else:
					return False
				#not end and character is *
			else:
				forwordChar = {}
				pos = p_pos
				while pos + 1 < p_len and p[pos+1] == '*':
					if pos+3 < p_len and p[pos] == p[pos+2] and p[pos+3] == '*':
						pass
					elif p[pos] in forwordChar:
						forwordChar[p[pos]].append(pos)
					else:
						forwordChar[p[pos]] = [pos]
					pos += 2
				nextChar = '/'
				lastPos = -1
				if pos < p_len:
					nextChar = p[pos]
					lastPos = pos
					print nextChar
				if '.' in forwordChar:
					if lastPos == -1:	return True
					while s_pos < s_len:
						if nextChar == '.' or s[s_pos] == nextChar:
							if self.isMatch(s[s_pos+1:],p[lastPos+1:]) == True:	return True
						s_pos += 1
					return False
				if s_pos < s_len and s[s_pos] in forwordChar:
					if (s[s_pos] == nextChar or nextChar == '.'):
						if self.isMatch(s[s_pos+1:],p[lastPos+1:]) == True:	return True
					for pos in forwordChar[s[s_pos]]:
						print pos
						if self.isMatch(s[s_pos+1:], p[pos:]) == True:	return True
				if s_pos < s_len and (s[s_pos] == nextChar or nextChar == '.'):
					if self.isMatch(s[s_pos+1:],p[lastPos+1:]) == True:
						return True
				if s_pos < s_len and s[s_pos] == '#':
					return self.isMatch(s[s_pos:], p[p_pos+2:])
				return False
		if s_pos == s_len and p_pos == p_len:	return True
		return False
so = Solution()
#'bbbba', 'b*b*b*b*b*a*a'
#'bbbba', '.*a*b*a'
#'bbbaabbccbcccccccac', 'bba*.*.*c*.*c*b*a'
#'baaaa','ba*'
#'', '.*'
#'aaaaaaaaaaaaab', 'a*a*a*a*a*a*a*a*a*a*c'
#'aab', 'c*a*b'
#'ab', '.*..'
#'aaa', 'a*a'
#"aaba", "ab*a*c*a"
#"", ".*"
if so.isMatch("", ".*"):
	print 'Match'