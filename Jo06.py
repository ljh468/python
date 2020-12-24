# 파이썬 프로그램
# 가장먼저 입력과 출력을 생각해라

## 구구단
import os


def GuGu(n):
    result = []
    i = 1
    while i < 10:
        result.append(n*i)
        i = i + 1
    return result


print(GuGu(2))

# 3과 5의 배수 합하기
# 1000미만의 자연수에서 3의 배수와 5의 배수의 총합을 구하라
result = 0
for n in range(1, 1000):
    if n % 3 == 0 or n % 5 == 0:
     result += n
print(result)

# 게시판 페이징하기
# 게시물의 총 건수와 한페이지에 보여줄 게시물 수를 입력으로 주었을때 총 페이지수를 출력


def GetTotalPage(m, n):
    if m % n == 0:
        return m // n
    else:
        return m // n + 1  # 총건수에 한페이지 최대를 나누고 +1


print(GetTotalPage(5, 10))
print(GetTotalPage(30, 10))

# 간단한 메모장 만들기
# 원하는 메모를 파일에 저장하고 추가 및 조회가 가능한 간단한 메모장
# memo.py 파일 참고

# 탭을 4개의 공백으로 바꾸기
# a.txt파일의 탭을 공백으로 바꾸어 b.txt로 저장
# tabto4.py 파일 참고

# 하위 디렉토리 검색하기
# 특정 디렉토리부터 시작해서 그 하위 모든파일중 .py파일만 출력
# dir_search.py 파일 참고
