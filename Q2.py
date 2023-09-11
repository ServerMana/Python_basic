#print("이 프로그램은 두 정수의 합을 구하는 프로그램 입니다")
#a=int(input("첫번째 값을 입력하세요"))
#b=int(input("두번째 값을 입력하세요"))
#sum=a+b
#print("두 정수의 합은",sum,"입니다")


#print("이 프로그램은 이름 입력시 상호작용하는 프로그램입니다")

#이름=input("이름을 입력하시오\n")
#print(이름,"씨 안녕하세요?")
#print("파이썬에 오신걸 환영합니다")

print("거스름돈을 계산해주는 프로그램")

product_price = int(input("상품 가격을 입력하세요: "))

payment = int(input("지불한 돈의 액수를 입력하세요: "))
change = payment - product_price
print("거스름돈은", change, "원입니다.")
change_500=change//500
change_100=(change-change_500*500)//100
print("500원 개수:",change_500,"100원 개수:",change_100)



#p=int(input("분자 값을 입력하세요"))
#q=int(input("분모 값을 입력하세요"))
#print("나눗셈의 몫은",p//q)
#print("나눗셈의 나머지",p%q)
