class Solution:
    # @param {integer[]} nums1
    # @param {integer[]} nums2
    # @return {float}
	def findMedianSortedArrays(self, nums1, nums2):
		def getMedian(nums):
			l = len(nums)
			if l % 2 == 1:
				return nums[l/2]/1.0
			else:
				return (nums[l/2] + nums[l/2 - 1] ) / 2.0
		#saveNum = -1
		if len(nums2) < len(nums1):
			nums = nums2
			nums2 = nums1
			nums1 = nums
		if len(nums1) == 0: 
			if len(nums2) > 0:	return getMedian(nums2)
			else:	return ()
		k = (len(nums1) + len(nums2))/2
		left1 = 0
		right1 = len(nums1)
		left2 = 0
		right2 = len(nums2)
		target = 0
		#find the k-th number in sorted arrays
		while(1):
			if right1 - left1 <= 1 or right2 - left2 <= 1: break;
			mid = (left1+right1)/2
			l = left2
			r = right2
			while(l<r):
				if nums2[(l+r)/2] > nums1[mid]:
					l = (l+r)/2+1
				elif nums2[(l+r)/2] < nums1[mid]:
					r = (l+r)/2-1
				else:
					l=(l+r)/2
					r=l
					break;
			if r < right2 and r >= left2:
				#here are r-left2 + mid+1-left1 before nums1[k]
				if r-left2 + mid+1-left1 == k - 1:
					target = 1
					left1 = mid
					right1 = mid
					left2 = -1
					right2 = -1
					break;
				elif r-left2 + mid-left1 > k-1:
					right1 = mid
					right2 = r
				else:
					left1 = mid+1
					left2 = r+1
					k = k - (r-left2 + mid-left1 + 1)
			else:
				if r >= right2:
					right1 = mid;
				else:
					left1 = mid+1
					k = k - mid - 1
		print left1
		print left2
		return -1
#nums1 = (3,)
#nums2 = ()
nums1 = (3,4)
nums2 = (1,2,4,5,6)
#nums1 = (3,4,4,5,6,7,8)
#nums2 = (1,2,3,4,5,6,7)
#nums1 = (3,5)
#nums2 = (3,4)
#nums2 = (1,2,6)
#nums1 = (3,4,5)
#nums1 = (1,2)
#nums2 = (3,4,5,6,7)
so = Solution()
print so.findMedianSortedArrays(nums1, nums2)