class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for s in tokens:
            try:
                num = int(s)
                stack.append(num)
            except ValueError:
                if s == "+":
                    stack[-2] = stack[-2] + stack[-1]
                    stack.pop()
                elif s == "-":
                    stack[-2] = stack[-2] - stack[-1]
                    stack.pop()
                elif s == "*":
                    stack[-2] = stack[-2] * stack[-1]
                    stack.pop()
                elif s == "/":
                    if stack[-2] * stack[-1] < 0 and stack[-1] * (stack[-2] / stack[-1]) != stack[-2]:
                        stack[-2] = stack[-2] / stack[-1] + 1
                        stack.pop()
                        continue
                    stack[-2] = stack[-2] / stack[-1]
                    stack.pop()
                #print stack[-1]
        return stack[0]
so = Solution()
print so.evalRPN(["-78","-33","196","+","-19","-","115","+","-","-99","/","-18","8","*","-86","-","-","16","/","26","-14","-","-","47","-","101","-","163","*","143","-","0","-","171","+","120","*","-60","+","156","/","173","/","-24","11","+","21","/","*","44","*","180","70","-40","-","*","86","132","-84","+","*","-","38","/","/","21","28","/","+","83","/","-31","156","-","+","28","/","95","-","120","+","8","*","90","-","-94","*","-73","/","-62","/","93","*","196","-","-59","+","187","-","143","/","-79","-89","+","-"])