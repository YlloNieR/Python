import mmap

word = b"ABC"

with open('hello.txt', 'rb', 0) as file, \
     mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ) as s:
    if s.find(word) != -1:
        print('true')
        print(s.find(word))
        print(s.read_byte())
        print(s.read())
        print(s.readline())
        print("seek ... ",s.seek(0))
        print(s.flush())
        print(s.rfind(word))
        print(s.tell())
        print(s.size())


