objects = [1,2,3,1,2,3,1]

strok = list(map(str, objects))

print(*strok, id(strok), id(objects))


