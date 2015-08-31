class Solution:
    # @param {character[][]} grid
    # @return {integer}
	def numIslands(self, grid):
		if grid == []:	return 0
		colLength = len(grid)
		rowLength = len(grid[0])
		result = 0
		#print colLength, rowLength
		for i, elems in enumerate(grid):
			for j, elem in enumerate(elems):
				if elem == '1':
					stack = [(i,j)]
					while stack != []:
						pos = stack.pop()
						#print grid[pos[0]][pos[1]]
						grid[pos[0]][pos[1]] = '0'
						if pos[0] + 1 < colLength and grid[pos[0]+1][pos[1]] == '1':
							stack.append((pos[0]+1, pos[1]))
						if pos[1] + 1 < rowLength and grid[pos[0]][pos[1]+1] == '1':
							stack.append((pos[0], pos[1]+1))
						if pos[1] - 1 >= 0 and grid[pos[0]][pos[1]-1] == '1':
							stack.append((pos[0], pos[1]-1))
						if pos[0] - 1 >= 0 and grid[pos[0]-1][pos[1]] == '1':
							stack.append((pos[0]-1, pos[1]))
					result += 1
		return result
s = [['1']]
#print s
so = Solution()
print so.numIslands(s)