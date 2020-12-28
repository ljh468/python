#########################  조코딩 #########################
## 정규표현식
# 정규표현식이란? 복잡한 문자열을 처리할때 사용하는 기법, 모든 언어 공통\

import re
data = """
park 800805-1049118
kim 700905-1059119
"""

pat = re.compile("(\d{6})[-]\d{7}")
print(pat.sub("\g<1>-*******", data))

########################
## 문자클래스 []

## [] 사이의 문자들과 매치
# [abc]
# "a"는 정규식과 일치하는 문자인 "a"가 있으므로 매치
# "before"는 정규식과 일치하는 문자인 "b"가 있으므로 매치
# "dude"는 정규식과 일치하는 문자인 a, b, c 중 어느 하나도 포함하고 있지 않으므로 매치되지않음
# 하이픈을 사용하여 From-To로 표현 가능
# EX) [a-c] = [abc], [0-5] = [012345]

## Dot[.]
# a.b
# 줄바꿈(\n)을 제외한 모든 문자와 매치
# "aab"는 가운데 문자 "a"가 모든 문자를 의미하는 '.'과 일치하므로 정규식과 매치
# "a0b"는 가운데 문자 "0"가 모든 문자를 의미하는 '.'과 일치하므로 정규식과 매치
# "abc"는 "a"문자와 "b"문자 사이에 어떤 문자라도 하나는 있어야 하는 이정규식과 일치하지 않으므로 매치되지 않는다.

## 반복(*)
# ca*t
# "ct"는 "a"가 0번 반복되어 매치
# "cat"는 "a"가 0번 이상 반복되어 매치 (1번 반복)
# "caaat"는 "a"가 0번 이상 반복되어 매치 (3번 반복)

## 반복(+)
# ca+t
# "ct"는 "a"가 0번 반복되어 매치되지 않음
# "cat"는 "a"가 0번 이상 반복되어 매치 (1번 반복)
# "caaat"는 "a"가 0번 이상 반복되어 매치 (3번 반복)

## 반복({m,n}, ?)
# ca{2}t
# "cat"는 "a"가 1번 반복되어 매치되지 않음
# "caat"는 "a"가 2번 반복되어 매치

# ca{2, 5}t
# "a"가 2이상 5이하로 반복되면 매치
# "cat"는 "a"가 1번 반복되어 매치되지 않음
# "caat"는 "a"가 2번 반복되어 매치
# "caaaaat"는 "a"가 5번 반복되어 매치

# ab?c
# 0번 또는 1번 반복되면 매치
# "abc"는 "b"가 1번 사용되어 매치
# "ac"는 "b"가 0번 사용되어 매치

########################
## 정규식을 지원하는 re모듈
import re
p = re.compile('ab*')

########################
## p객체를 이용한 4가지 패턴방식

# match
# 문자가 일치해야만 match객체로 리턴
import re
p = re.compile('[a-z]+')

m = p.match("python")
print(m)
# <_sre.SRE_Match object at 0x01F3F9F8> -> 매치되었음

m = p.match("3 python")
print(m)
# None -> 매치 안됨

########################
# search
# 일치하지않는 문자가 있더라도 일치하는걸 찾아서 match객체로 리턴
import re
p = re.compile('[a-z]+')
m = p.search("python")
print(m)
# <_sre.SRE_Match object at 0x01F3FA68 -> 매치되었음

m = p.search("3 python")
print(m)
# <_sre.SRE_Match object at 0x01F3FA30 -> 매치되었음

########################
# findall
# 일치하는 문자를 찾아서 리스트로 리턴
p = re.compile('[a-z]+')
m = p.findall("life is too short")
print(m)
# <_sre.SRE_Match object at 0x01F3FA30 -> 매치되었음

# finditer
# 일치하는 문자를 Iterator객체로 리턴
m = p.finditer("life is too short")
for r in m:
    print(r)

## match 객체의 메서드 1
# group() - 매치된 문자열을 리턴
# start() - 매치된 문자열의 시작위치를 리턴
# end() -  매치된 문자열의 끝 위치를 리컨
# spen() - 매치된 문자열의 (시작, 끝)에 해당되는 튜플을 리턴한다.
import re
p = re.compile('[a-z]+')
m = p.match('python')
print(m.group())
print(m.start())
print(m.end())
print(m.span())

########################
# 컴파일 옵션, DOTALL, S

# DOTALL, S 옵션
# . 이 줄바꿈도 인식하도록 
import re
p = re.compile('a.b', re.S)
m = p.match('a\nb')
print(m)

# IGNORECASE, I 옵션
# 대소문자를 상관없이 인식하도록
p = re.compile('[a-z]', re.I)
print(p.match('python'))
print(p.match('Python'))
print(p.match('PYTHON'))

# MULTILINE, M 옵션
# ^가 맨처음만이 아닌 각 라인의 맨처음으로 인식하도록
p = re.compile("^python\s\w+", re.M)

data = """python one
life is too short
python two
you need python
python three"""

print(p.findall(data))

# VERBOSE, X
# 길이가 긴 정규표현식으로 나눠서 쓸수있게 만들어줌
charref = re.compile(r'%[#](0[0-7]+|[0-9]+|x[0-9a-fA-F]+);')

charref = re.compile(r"""
&[#]                    # Start of a numeric entity reference
(
    0[0-7]+             # Octal form
    | [0-9]+            # Decimal form
    | x[0-9a-fA-F]+     # Hexadecimal form
)
;                       # Trailing semicolon
""", re.VERBOSE)

# 백슬러시 문제
# \ 사용시 \\두번을 써서 백슬러시를 인식해야함
p = re.compile('\\section')
p = re.compile('\\\\section')
p = re.compile('r\\section') # rowString은 공백아닌걸 표현 가능

########################
## 강력한 정규 표현식

# 메타문자 |
# or을 표현 앞문자 또는 뒤문자와 일치하는 문자 리턴
import re
p = re.compile('Crow|servo')
m = p.match('CrowHello')
print(m)

# 메타문자 ^
# 맨처음에 나오는지 확인
print(re.search('^Life', 'Life is too short'))
print(re.search('^Life', 'My Life'))

# 메타문자 $
# 맨끝에 나오는지 확인
print(re.search('short$', 'Life is too short'))
print(re.search('short$', 'Life is too short, you need python'))

# 메타문자 \b
# 공백을 확인
p = re.compile(r'\bclass\b')
print(p.search('no class at all'))
print(p.search('the declassified algorithm'))
print(p.search('one subclass is'))

########################
# 그루핑 1
# (ABC)+
# 가로를 이용해서 표현식을 묶어주는 역할
p = re.compile('(ABC)+') # ABC가 반복되는것을 찾고 싶을때
m = p.search('ABCABCABC OK?')
print(m)
print(m.group())

# 그루핑 2 
p = re.compile(r"(\w+)\s+\d+[-]\d+[-]\d+")
m = p.search("park 010-1234-1234")
print(m.group(1))

# 그루핑 3
p = re.compile(r'(\b\w+)\s+\1') # \s 같은문자열이 한번더 반복되는것을 찾음
print(p.search('Paris in the the spring').group())

# 그루핑 4
# 그루핑된 문자열에 이름 붙이기 ?P<name>
p = re.compile(r"(?P<name>\w+)\s+((\d+)[-]\d+[-]\d+)")
m = p.search("park 010-1234-1234")
print(m.group("name"))

# 그루핑 5
# 그루핑된 문자열에 이름 붙이기 ?P<name>
p = re.compile(r'(?P<word>\b\w+)\s+(?P=word)') # 같은문자열이 한번더 반복되는것을 찾음
p.search('Paris in the the spring').group()

########################
# 전방탐색: 긍정형 (?=)
p = re.compile(".+:") # 임의의 문자가 반복되다가 :까지의 문자열 매칭
p2 = re.compile(".+(?=:)") # : 바로 전 문자열까지 매칭
m = p.search("http://google.com")
m2 = p2.search("http://google.com")
print(m.group())
print(m2.group())

########################
# 전방탐색: 부정형 (?!)
p = re.compile(".*[.](?!bat$|exe$).*$", re.M) # ?!다음문자가 포함되지않는 문자열 매칭
l = p.findall("""
autoexec.exe
autoexec.bat
autoexec.jpg
""")
print(l)

########################
# 문자열 바꾸기 sub
p = re.compile('(bule|white|red)') # 설정한 문자열을 sub으로 바꿔줄수 있음
print(p.sub('colour', 'blue socks and red shoes'))

########################
# Greedy 와 Non-Greedy
s = '<html><head><title>Title</title>'
print(re.match('<.*>', s).group()) # Greedy
# -> <html><head><title>Title</title> 전체 문장 다 가져옴
print(re.match('<.*?>', s).group()) # Non-Greedy
# -> <html>
# ?를 이용하면 최소한반복을 의미