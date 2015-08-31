from collections import deque
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """
        if not node:
            return None
        newSet = {}
        queue = deque([node])
        while queue:
            cur = queue.popleft()
            if cur.label not in newSet:
                newNode = UndirectedGraphNode(cur.label)
                newSet[cur.label] = newNode
            else:
                newNode = newSet[cur.label]
            for neighbor in cur.neighbors:
                if neighbor.label not in newSet:
                    queue.append(neighbor)
                    tmp = UndirectedGraphNode(neighbor.label)
                    newSet[tmp.table] = tmp
                    newNode.neighbors.append(tmp)
                else:
                    newNode.neighbors.append(newSet[neighbor.label])
        return newSet[node.label]
u1 = UndirectedGraphNode(1)
u2 = UndirectedGraphNode(2)
u3 = UndirectedGraphNode(3)
so = Solution()
print so.cloneGraph(u1).label

class Solution(object)
    def cloneGraph(self, node):
        if not node:
            return None
        dic, queue = dict(), collections.deque([node])
        while queue:
            curr = queue.popleft()
            if curr.label not in dic:
                newNode = UndirectedGraphNode(curr.label)
                dic[curr.label] = newNode
            else:
                newNode = dic[curr.label]
            for neighbor in curr.neighbors:
                if neighbor.label not in dic:
                    queue.append(neighbor)
                    tmp = UndirectedGraphNode(neighbor.label)
                    dic[tmp.label] = tmp
                    newNode.neighbors.append(tmp)
                else:
                    newNode.neighbors.append(dic[neighbor.label])
        return dic[node.label]