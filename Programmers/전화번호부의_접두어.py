'''
#전화번호 목록 #Hash #Lv2 
전화번호 목록 : 전화번호들이 담긴 배열이 주어지면 배열 내의 특정 번호가 또 다른 번호의 접두어로 겹치는지를 체크하는 문제
'''

def solution(phonebook):
    phonebook = sorted(phonebook)
    for p1, p2 in zip(phonebook, phonebook[1:]):
        if p2.startswith(p1): 
            return False 
return True