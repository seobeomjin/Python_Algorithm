'''
1) 요약
#전화번호 목록 #Hash #Lv2 
전화번호 목록 : 전화번호들이 담긴 배열이 주어지면 배열 내의 특정 번호가 또 다른 번호의 접두어로 겹치는지를 체크하는 문제

2) 문제
구조대 : 119
박준영 : 97 674 223
지영석 : 11 9552 4421
전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때, 
어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return 하도록 solution 함수를 작성해주세요.

제한 사항
phone_book의 길이는 1 이상 1,000,000 이하입니다.
각 전화번호의 길이는 1 이상 20 이하입니다.
입출력 예제
phone_book	return
[119, 97674223, 1195524421]    false
[123,456,789]   true
[12,123,1235,567,88]    false

# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges
'''

def solution(phonebook):
    phonebook = sorted(phonebook)
    for p1, p2 in zip(phonebook, phonebook[1:]):
        if p2.startswith(p1): 
            return False 
    return True

# 채점 결과
# 정확성: 84.6
# 효율성: 15.4
# 합계: 100.0 / 100.0

