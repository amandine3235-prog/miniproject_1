# 386페이지 - 1번
a="a:b:c:d"
b=a.split(":")
print(b) # ['a', 'b', 'c', 'd']
c="#".join(b)
print(c) # a#b#c#d

# 386페이지 - 2번
a={'A':90, 'B':80}
b=a.get('C',70) 
#딕셔너리 안에 Key가 없을 경우, 미리 정해 둔 디폴트 값을 대신 가져오게 하고 싶을 때는
#get(x, '디폴트값')을 사용하면 된다
print(b) # 70

# 386페이지 - 3번
a=[1,2,3]
a=a+[4,5]
print(a) #[1, 2, 3, 4, 5]

b=[1,2,3]
b.extend([4,5])
print(b) #[1, 2, 3, 4, 5]

#답 : +를 사용하여 리스트를 더하면 리스트 a의 값이 변하는 것이 아니라 두 리스트가 더해진 새로운 리스트를 반환한다. 
# extend를 사용한 경우에는 원래의 리스트에 추가를 하는 개념이라 새로운 리스트가 반환되지 않는다.

# 387페이지 - 4번
A=[20,55,67,82,45,33,90,87,100,25]
sum=0
for i in A:
    if i>50:
        sum=sum+i
print(sum) #481

# 387페이지 - 5번
# 입력을 정수 n으로 받았을 때 n항 이하까지의 피보나치 수열을 출력하는 함수를 작성하시오.



# 388페이지 - 6번
# 사용자에게 입력받은 숫자의 총합을 구하는 프로그램 작성(숫자는 ','로 구분하여 입력한다)
# 65,45,2,3,45,8
# sum1=input("숫자를 입력하시오 : ")
# n=sum1.split(',')
# result=0
# for i in n:
#     result+=int(i)
# print(result) #168 

# 388페이지 - 7번
# 사용자에게 2~9의 숫자 중 하나를 입력받아 해당 숫자의 구구단을 한줄로 출력하는 프로그램 작성
# gugudan=input("구구단을 출력할 숫자를 입력하세요(2~9) : ")

# for i in range(1,10):
#     print(i*int(gugudan),end=" ")
# 구구단을 출력할 숫자를 입력하세요(2~9) : 2
# 2 4 6 8 10 12 14 16 18 

# 388페이지 - 8번
# 파일 역순으로 바꾸어 저장
# f=open('abc.txt','r')
# read=f.readlines()
# f.close()

# read.reverse()
# f=open('abc.txt','w')
# for i in read:
#     i=i.strip()
#     f.write(i)
#     f.write('\n')
# f.close()

# 389페이지 - 9번
# sample.txt의 숫자값을 모두 읽어 총합과 평균값을 구한 후 평균값을 result.txt에 쓰는 프로그램을 작성하시오
f=open("sample.txt")
lines=f.readlines()
f.close()

total=0
for line in lines:
    score=int(line)
    total+=score
avg=total/len(lines)

f=open("result.txt","w")
f.write(str(avg))
f.close()

# 389페이지 - 10번
class Calculator:
    def __init__(self, numbers):
        self.numbers = numbers

    def sum(self):
        total = 0
        for num in self.numbers:
            total += num 
        return total

    def avg(self):      
        total=self.sum()
        return total/len(self.numbers)

cal1=Calculator([1,2,3,4,5])
print(cal1.sum()) #합계 #15
print(cal1.avg()) #평균 #3.0

cal2=Calculator([6,7,8,9,10])
print(cal2.sum()) #합계 #40
print(cal2.avg()) #평균 #8.0

# 390페이지 - 11번
# 1번 : import mymod
# 2번 : from mymod import 모듈함수명
# 3번 : from mymod import *



# 390페이지 - 12번





# 391페이지 - 13번




# 391페이지 - 14번




# 391페이지 - 15번




