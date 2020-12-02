'''
#베스트앨범 # Hash #Lv3
베스트 앨범 : 장르별로 가장 많이 재생된 곡들을 상위 두곡씩 뽑아 베스트앨범 구성 
'''

def Q4_solution(genres, plays):
    answer = []
    d = {e:[] for e in set(genres)}
    print('d : ', d)
    for e in zip(genres, plays, range(len(plays))):
        print('e : ', e)
        d[e[0]].append([e[1] , e[2]])  # e[0]->genres 이고, 이미 아까 리스트로 만들어 두었으니 append가 되는구나
    print('after d : ', d) 
    # {'pop': [[600, 1], [2500, 4]], 'classic': [[500, 0], [150, 2], [800, 3]]}
    # 딕셔너리 형태로 각 고유번호와 재생 횟수를 넣었음
    # genreSort = sorted(list(d.keys()), key= lambda x: sum( map(lambda y: y[0],d[x])), reverse = True)
    genreSort =sorted(list(d.keys()), key= lambda x: sum([t[0] for t in d[x]]), reverse = True) 
    # t[0] 600, 2500 같은 재생 횟수 # map(function , list) -> 리스트에 있는 값들을 하나씩 꺼내서 함수를 적용 # d[x] 여기서 x는 각 dict의 key
    # 오름차순이기 때문에 reverse=True로 해서 내림차순으로. 
    # genre sort :  ['pop', 'classic']
    for g in genreSort:
        temp = [e[1] for e in sorted(d[g],key= lambda x: (x[0], -x[1]), reverse = True)] # 해당 장르의 리스트 내에서 정령 안에서 e[1]을 꺼내는 것 
        # 600 -1
        # 2500 -4
        print('temp : ',temp)
        answer += temp[:min(len(temp),2)]
    return answer

# 번외
# reduce # 리스트의 값들을 누적적으로 실행 
from functools import reduce 
reduce(lambda x, y: x + y, [0, 1, 2, 3, 4])
>>> 10

# filter # 리스트에서 참인 값들을 반환
>>> list(filter(lambda x: x < 5, range(10))) # 파이썬 2 및 파이썬 3
>>> [0, 1, 2, 3, 4]
# 참의 값만 통과시켜 내줌