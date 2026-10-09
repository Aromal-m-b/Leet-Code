class Solution:
    def minInsertions(self, s: str) -> int:
        count = 0
        insertions = 0

        for c in s:
            if c == '(':
                count += 2

                if count % 2 != 0:
                    insertions += 1
                    count -= 1
            else:
                count -= 1

                if count < 0:
                    insertions += 1
                    count = 1

        return insertions + count