'''
이 문제는 기존의 Best Time to Buy and Sell Stock과 비슷하지만, 여러번 거래를 할 수 있다는 점이 다르다.
여기에서 제일 어려운 포인트는 과연 어떻게 해야 가장 maximum한 수익을 낼 수 있는가 이다.
[7,1,5,3,6,4] 여기에선 2 day에 사서 3 day에 팔고, 다시 4 day에 사서 5 day에 파는 방법으로 최대 수익을 냈고,
[1,2,3,4,5] 여기에선 1 day에 사서 2, 3, 4에 팔 수 있었지만, 5 day에 팔아서 최대 수익을 냈다.
for 하나로 이게 가능할까? 모든 경우의 수를 계산하지 않고 한번의 for문으로 이게 되는거라면,,

인간이라면 어떻게 구할까?
먼저 [7,1,5,3,6,4] 전체를 본다.
그리고 기존의 방법 6-1=5과 (5-1)+(6-3)=7를 계산해서 어떤 게 더 큰지 계산을 하면서 알 수 밖에 없다.
굳이 그럼 for을 여러번 돌아야할까?
for문 하나에서 구하는 방법도 있긴하다.
먼저 기존의 방법으로 최대의 수익을 내는 방법을 구한다.
아니 이게 가능해? 모든 경우의 수를 구하는 게 제일 편해보이는데?
이게 medium인가...? 내 머리로는 도저히 방법이 떠오르지 않는다.
한가지 방법이 떠올랐는데, buy 하고 sell 할때, 그 다음 요소가 더 크면 안 팔고, 더 크면 판다.
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        min_price_2 = prices[0]
        total_sell = 0
        sell = 0
        max_price = 0

        for i in range(0, (len(prices)-1)):
            # buy 타이밍
            print(f"i: {i}")
            if prices[i] <= min_price:
                min_price = prices[i]
                print(f"min_price: {min_price}")
                
            if prices[i+1] < prices[i]:
                sell = prices[i] - min_price
                total_sell += sell
                min_price = prices[i+1]
                print(f"prices[{i+1}] < prices[{i}]: {prices[i+1]} < {prices[i]}")
                print(f"changed min_price: {min_price}")
                print(f"total_sell: {total_sell}")

            elif prices[i+1] > prices[i]:
                sell = prices[i+1] - min_price
                total_sell += sell
                min_price = prices[i+1]
                print(f"prices[{i+1}] > prices[{i}]: {prices[i+1]} > {prices[i]}")
                print(f"changed min_price: {min_price}")
                print(f"total_sell: {total_sell}")
            
        for j in prices:
            if j < min_price_2:
                min_price_2 = j
            if max_price < j - min_price_2:
                max_price = j - min_price_2
            
        
        if total_sell > max_price:
            return total_sell
        else:
            return max_price
            