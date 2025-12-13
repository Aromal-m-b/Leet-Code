class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        store = []
        for i,valid in enumerate(isActive):
            if valid:
                if businessLine[i] == 'electronics' or businessLine[i] == 'grocery' or businessLine[i] == 'pharmacy' or businessLine[i] == 'restaurant':
                    bef = code[i].replace("_","und")
                    if len(code[i]) != 0 and bef.isalnum():
                        store.append([businessLine[i],code[i]])      

        store.sort(key = lambda x:(x[0],x[1]))
        return [x[1] for x in store]