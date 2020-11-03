stack = []
book = dict() #딕셔너리 추가
for i in range(int(input())): #몇개 팔았는지
    name = input() #책 제목 받기
    if name not in book.keys(): #만약 딕셔너리에 책 제목이 없다면
        book[name] = 1 #수량을 1로 설정
    else:
        book[name] += 1 #수량을 1개 추가

best = max(book.values()) #가장 많은 수량을 best로 저장

for name, value in book.items():
    if best == value:
        stack.append(name)

stack.sort()
print(stack[0])