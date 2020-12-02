'''
#마라톤 #Hash #Lv1(?)
참가자,완주자 문자열 배열을 입력으로 주면 완주하지 못한 사람의 이름을 반환하는 문제
'''

import collections
def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]