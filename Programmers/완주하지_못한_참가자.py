'''

2회 풀이했음 

1) 요약 
#마라톤 #Hash #Lv1(?)
참가자,완주자 문자열 배열을 입력으로 주면 완주하지 못한 사람의 이름을 반환하는 문제

2) 문제
수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.
마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

제한사항
마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
completion의 길이는 participant의 길이보다 1 작습니다.
참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
참가자 중에는 동명이인이 있을 수 있습니다.

입출력 예
participant	                                    completion	                        return
[leo, kiki, eden]	                            [eden, kiki]	                    leo
[marina, josipa, nikola, vinko, filipa]	        [josipa, filipa, marina, nikola]	vinko
[mislav, stanko, mislav, ana]                   [mislav, stanko, ana] 

출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges
'''

import collections
def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]