import sys

option = sys.argv[1]

if option == '-a':
    memo = sys.argv[2]
    f = open('memo.txt', 'a')
    f.write(memo)
    f.write('\n')
    f.close()
# py memo.py -a "Life is too short"

elif option == '-v':
    f = open('memo.txt')
    memo = f.read()
    f.close()
    print(memo)
# py memo.py -v