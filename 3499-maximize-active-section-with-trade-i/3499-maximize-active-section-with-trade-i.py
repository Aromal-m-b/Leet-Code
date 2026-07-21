class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        if "1" not in s:
            return 0
        ones = s.count("1")
        zero_blocks = []
        count = 0
        flag = 0
        for i in s:
            if i == '0':
                count += 1
                flag = 1
            else:
                if flag:
                    zero_blocks.append(count)
                    count = 0
                    flag = 0
        if count > 0:
            zero_blocks.append(count)
        if len(zero_blocks) > 1:
            print(zero_blocks)
            left = zero_blocks[0]
            max_act = 0
            for i in range(1, len(zero_blocks)):
                right = zero_blocks[i]
                max_act = max(max_act, left + right)
                left = right
            return ones + max_act
        else:
            print(zero_blocks)
            return ones
