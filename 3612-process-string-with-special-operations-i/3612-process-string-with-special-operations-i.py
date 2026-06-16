class Solution:
    def processStr(self, s: str) -> str:
        res = []
        for c in s:
            if ord(c) > 96 and ord(c)<123:
                res.append(c)
            elif c == '*':
                if res:
                    res.pop()
            elif c == '#':
                res.extend(res)
            elif c == '%':
                res = res[::-1]
        return ''.join(res)