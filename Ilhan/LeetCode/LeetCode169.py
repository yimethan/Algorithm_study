'''
이 문제는 가장 저렴할 때 사고, 가장 비쌀 때 파는 단순한 문제처럼 보인다.
배열에는 가격이 들어가 있다.
어떻게 제일 쌀 때 사고, 제일 비쌀 때 팔 수가 있을까?
우리가 눈으로 봤을 때는 너무 직관적으로 알 수가 있다.
배열에서 가장 작은 값을 찾는 건 1가지 경우를 제외하곤 필요하다.
그 다음 가장 큰 요소를 찾아야 하는데, 문제는 가장 작은 요소보다 뒤에 있는 가장 큰 요소를 찾아야한다.
그렇다면, 먼저 가장 작은 요소를 찾고, 그 요소 이후에 가장 큰 요소를 찾는 방식으로 풀면 어떨까?
++ 이렇게 풀면 가장 마지막에 최소값이 있을 때 에러가 발생한다.
그렇다고 최소 값이 가장 마지막에 있을 때 그걸 제외하고 다시 구하는 방법은 너무 비효율적이다.
결국 이 문제는 차가 제일 클 때를 찾는거다. 최소 최대를 찾는게 아니다.
그럼 버블 방식으로 풀어야 하나..?
이건 말이 안되는 방법이고,
앞과 뒤에서 동시에 접근이 가능한 큐인 덱을 사용하면 어떨까?
그러니까, 먼저 딕셔너리나 튜플을 사용해서 각 인덱스의 넘버를 요소와 함께 명시해준다.
그리고 오름차순 정렬을 수행하고,
가장 작은 수가 맨 뒤 요소라면 delete하고, 아니라면 buy,
그리고 제일 뒤로 가서, 제일 큰 수가 맨 앞 요소라면 delete하고, 아니라면 sell
해서 제일 높은 차익을 내면 된다.
이 방법은 너무 과하게 복잡한 풀이라고 생각된다.
훨씬 간단한 방법이 있을 거 같은데,,
그냥 for 문 두개 사용하면 제일 쉽게 풀일 문제 같은데,,, 이렇게 해볼까?
'''
'''
실패한 알고리즘 1
        minimum = prices[0]
        index = 0
        min_index = 0
        for i in prices:
            if minimum > i:
                minimum = i
                min_index = index
            index += 1
        
        print("minimum: ", minimum, " min_index: ", min_index)

        maximum = prices[min_index]
        for i in prices[min_index:]:
            if maximum < i:
                maximum = i
        
        print("maximum: ", maximum)

        return (maximum - minimum)
'''
'''
실패한 알고리즘 2
from collections import deque

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        sorted_prices = sorted(prices, reverse = True)
        if prices == sorted_prices:
            return 0
        
        tupled_prices = tuple((value, index) for value, index in enumerate(prices))
        print(tupled_prices)

        sorted_tupled_prices = sorted(tupled_prices, key=lambda x: x[1])
        print(sorted_tupled_prices)

        deque_prices = deque(sorted_tupled_prices)

        for i in range(len(deque_prices)):
            if deque_prices[0][0] == 0:
                deque_prices.popleft()
            
            if deque_prices[-1][0] == (len(deque_prices) - 1):
                deque_prices.pop()
'''

'''
실패한 알고리즘 3, 메모리 초과
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        calculated_list = []
        for i in range(len(prices)):
            for j in range(i, len(prices)):
                print(f"prices[{i}] - prices[{j}]: ", prices[i] - prices[j])
                calculated_list.append(prices[i] - prices[j])
        
        return -(min(calculated_list))
'''

'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = prices[0]
        for i in range(len(prices)):
            for j in range(i, len(prices)):
                if prices[i] - prices[j] < minimum:
                    minimum = prices[i] - prices[j]
                
        
        return -minimum
'''
'''
아 너무 모르겠어서 결국 힌트 요청, 내 인생..

Time Limit Exceeded가 발생해서 GPT에게 힌트를 요청했음

힌트:
최솟값(min_price)을 계속 업데이트하면서 단일 루프로 해결 가능

매 순간 **최저 가격(min_price)**을 업데이트하면서, 현재 가격과의 차이를 계산하여 최대 이익을 갱신하는 방식으로 해결 가능
이렇게 하면 O(N) (단일 루프)으로 문제 해결 가능
한 번만 순회(O(N))하도록 알고리즘을 변경하는 것이 핵심

for 루프를 하나만 사용하고, 지나온 값 중 가장 작은 min_price를 유지하면서 max_profit을 갱신하면 됨
이렇게 하면 한 번만 리스트를 순회하며 값을 찾을 수 있음
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = prices[0]
        max_price = 0
        for i in prices:
            if minimum > i:
                minimum = i
            if max_price < i - minimum:
                max_price = i - minimum
        return max_price