Americano_Price=2000
Cafelatte_Price=3000
Capucino_Price=3500

Americano=int(input("아메리카노 판매개수:"))

Cafelatte=int(input("카페라떼 판매개수:"))

Capucino=int(input("카푸치노 판매개수:"))

sale=0

sale+=(Americano*Americano_Price)+(Cafelatte*Cafelatte_Price)+(Capucino*Capucino_Price)
print("총 매출",sale,"원")