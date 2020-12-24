import sys

src = sys.argv[1]
dst = sys.argv[2]

# 파일읽기
f = open(src)
tab_content = f.read()
f.close()

# 탭을 공백으로 replace
space_content = tab_content.replace("\t", " "*4)
print(space_content)

# 파일로 저장
f = open(dst, 'w')
f.write(space_content)
f.close()

# py tabto4.py a.txt b.txt