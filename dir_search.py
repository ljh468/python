import os

def search(dirname):
    try:
        filenames = os.listdir(dirname)
        for filename in filenames:
            full_filename = os.path.join(dirname, filename)

            # 만약 full_filename이 폴더라면 한번더 search함수 실행(재귀함수개념)
            if os.path.isdir(full_filename):
                search(full_filename)
            else:
                # 튜플형태로 경로, 확장자가 출력됨
                # 확장자만 찾기위해 [-1] 인덱스를 줌
                ext = os.path.splitext(full_filename)[-1]

                if ext == ".py":
                    print(full_filename)
    # 권한오류 예외처리
    except PermissionError:
        pass

search("C:/")