"""
- 3. Longest Substring Without Repeating Characters
    문자열에서 중복되는 문자없이 가장 긴 substring을 찾는 문제. (subsequence가 아님.)
    (즉, 연속되어야 한다는 의미)

- solved in 50min? (official: Medium / for me: ★★★★☆)
    Runtime: 52 ms, faster than 92.70% of Python3 online submissions for Longest Substring Without Repeating Characters.
    Memory Usage: 14.8 MB, less than 6.29% of Python3 online submissions for Longest Substring Without Repeating Characters.
    
    1) 중복되는 시점에서 어떻게 인덱스를 이동하냐가 관건이었고, 
    2) 특히, 중복되는 문자가 맨앞, 맨뒤, 중간에 따라서 달라졌음. 

    th) 이런 substring case에 약함. 다른 코드 잘 봐야.

- 배운 것 
    1) sliding window 방법론 
    substring과 같은 케이스 안에서, left, right index를 조정할 변수를 정해두고, 
    iterarive하게 돌면서 인덱스를 조정하는 방법. 

    2) 중복 여부를 set으로 계속 체크하고, set 안에 있으면 중복의 경우니까, 
    어차피 순서대로 와야하니까 중복이 지워질때까지 앞에서부터 차례대로 지우는거야..
    앞에서 부터 지울 때 left window를 +1씩 이동시키고. (놀라운 발상)
    앞에서부터 중복이 있는 부분을 지워 중복이 없게 만들고 새로운 char를 넣어줌. 
    result = max(기존의 max result, r-l+1(지금의 새로운 길이)) 로, max_length를 매번 갱신해주고. 


"""

# 내 풀이 
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s)!=0:
            m_list = []
            m = 0
            n = 0
            length = len(s)
            l = ""
            
            while(n<length):
                if s[n] not in l:
                    l += s[n]
                    m += 1
                    n += 1
                    if n == length:
                        m_list.append(m)
                else:
                    if l.find(s[n])==0: # 겹치는 문자가 첫 번째에 등장할 때
                        l = l[1:]
                        l += s[n]
                    elif l.find(s[n]) == n-1 : # 겹치는 문자가 n-1번째로, 바로 겹쳐 등장할 때
                        l = s[n]
                    else:
                        l = l[l.find(s[n])+1:] # 그 사이에 등장할 때
                        l += s[n]
                    m_list.append(m)
                    m = len(l)
                    n +=1
            return max(m_list)
        else :
            return 0
            
        
        tmp = set(s)
        return len(tmp)
    
    # not subsequence , nut substring 
    # 앞에서부터 substring을 탐색해야함.

    
    # 다른 효율풀이 

    class Solution:
        def lengthOfLongestSubstring(self, s: str) -> int:
            charset = set()
            res, l = 0,0

            for r in range(len(s)):
                while s[r] in charset:
                    charset.remove(s[l]) # substring으로서 연속적이어야 하므로 앞에서부터 지운다.
                    l +=1 
                charset.add(s[r])
                res = max(res, r-l+1)
            return res