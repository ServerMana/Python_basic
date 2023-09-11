#A학교에서는 단체 티셔츠를 주문하시 위해 학생별로 원하는 사이즈를 조사했습니다.
#선택할 수 있는 티셔츠 사이즈는 작은 순서대로 "XS","S","M","L","XL","XXL" 총 6종류가 있습니다
#학생별로 원하는 티셔츠 사이즈를 조사한 결과가 들어있는 리스트 shirt_size가 매개변수로 주어질 때, 
#사이즈별로 티셔츠가 몇 벌 씩 필요한지 가장 작은 사이즈부터 순서대로 리스트에 담아 return 하도록 솔류션함수를 완성
#매개변수 설명
# shirt_size의  길이는 1 이상 100 이하입니다
# shirt_size에는 치수를 나타내는 문자열 "XS","S","M","L","XL","XXL"이 들어있습니다
#return값
#티셔츠가 사이즈별로 몇 벌씩 필요한지 가장 작은 사이즈부터 순서대로 리스트에 담아 return해주세요
#return하는 리스트에는
#["XS"개수,"S"개수,"M"개수,"L"개수,"XL"개수,"XXL"개수] 순서대로 들어있으야합니다
#예시 
# |shirt_size                 |return        |
# |___________________________|______________|
# |["XS","S","M","L",XL",XXL"]|[1,2,0,2,1,0] |

from collections import Counter

def count_shirt_sizes(shirt_size):
    # 각 사이즈별 티셔츠 개수를 세기 위해 Counter를 사용
    size_counts = Counter(shirt_size)
    
    # 가능한 모든 사이즈 목록
    sizes = ["XS", "S", "M", "L", "XL", "XXL"]
    
    # 각 사이즈별로 개수를 가져오거나 0으로 초기화
    result = [size_counts[size] for size in sizes]
    
    return result

# 테스트
shirt_size = ["S","XS", "S","L","XL","L"]
result = count_shirt_sizes(shirt_size)
print(result) 
