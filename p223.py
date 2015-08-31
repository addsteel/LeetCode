class Solution:
    # @param {integer} A
    # @param {integer} B
    # @param {integer} C
    # @param {integer} D
    # @param {integer} E
    # @param {integer} F
    # @param {integer} G
    # @param {integer} H
    # @return {integer}
	def computeArea(self, A, B, C, D, E, F, G, H):
		#If there exists overlap
		if (E <= C and E >= A ) or (G <= C and G >= A ) or (E <= A and G >= A ) or (E <= C and G >= C ):
			if (H >= B and H <= D) or (F >= B and F <= D) or (H >= B and F <= B) or (H >= D and F <= D):
				vertical = [B,D,F,H]
				horizontal = [A,C,E,G]
				vertical = sorted(vertical)
				horizontal = sorted(horizontal)
				print vertical
				print horizontal
				return (D-B) * (C-A) + (H-F) * (G-E) - (vertical[2] - vertical[1]) * (horizontal[2] - horizontal[1])
		#If not
		return (D-B) * (C-A) + (H-F) * (G-E)
A = -2
B = -2
C = 2
D = 2
E = -1
F = -1
G = 1
H = 1
A = -5
B = -2
C = 5
D = 1
E = -3
F = -3
G = 3
H = 3
so = Solution()
print so.computeArea(A, B, C, D, E, F, G, H)