    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer = ''
        min_len = min(len(word) for word in strs)

        for pos in range(min_len):
            current = strs[0][pos]

            for i in range(1, len(strs)):
                if strs[i][pos] != current:
                    return answer
            
            answer += current
        
        return answer
