#if_.py

#비교 연산자
#비교 연산의  결과는 무조건 True 또는 False로 나옴
# ==    : 같으면 True, 다르면 False
# !=    다르면 True, 같으면 False
# <
# >
# <=
# >=

# print(5 != 2)
# print(5 < 2)


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


#조건식 종류

#[가장 일반적인 형식]
# if (조건식) :
#   if의 조건식이 True일 경우 실행할 코드
# elif (조건식) :
#   elif의 조건식이 True일 경우 실행할 코드
#else :
#   위에 모든 조건식이 False일 경우 실행할 코드
#[if만 사용한 경우]
# if (조건식) :
#   if의 조건식이 True일 경우 실행할 코드


#[if랑 elif만 사용한 경우]
# if (조건식) :
#   if의 조건식이 True일 경우 실행할 코드
# elif (조건식)
#   elif의 조건식이 True일 경우 실행할 코드


#[if랑 else만 사용한 경우]
# if (조건식) :
# else :
#   위에 모든 조건식이 False일 경우 실행할 코드


# 위 형식들의 조건식이 있으며
# if는 무조건 1개
# elif는 0개 부터 무한대,
# else는 0개 또는 1개를 사용하여 조건문을 구성할 수 있음
# 조건문은 조건문 안에 중첩해서 사용할 수 있다.


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# score는 숫자로 입력받기
# 100 ~ 90 : A
# 89 ~ 70 : B
# 69 ~ 60 : C
# 59 ~ 0 : D
# 조건식으로 표현해보자.


# score = int(input())        #숫자로 입력받음
# if(100 >= score >= 90):      #조건문이 True여서 실행될 경우 아래의 조건은 더 보지 않고 if 종료, 즉 조건문은 무조건 한개만 동작함
#     print('A')
# elif (89 >= score >= 70):
#     print ('B')
# elif (69 >= score >= 60):
#     print ('C')
# elif (59 >= score >= 0):
#     print('D')


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


print("나이가 12세 이상만 영화 관람이 가능합니다. ")
var1 = input("나이를 입력해주세요.")



# var1 = 2
# var2 = input("Insert anything :")
# print(var2)
# print(type(var2))

# var2 = int(var2)
# print(type(var2))

# sum = var1 + var2
# print(sum)