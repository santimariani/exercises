count = 0
answer = 0 

while count < 100:
    count = count + 1
    answer = int(count * (count + 1) / 2)
    print(answer)


STOP = 100
triangle_num = 0
counter_row = 0
while counter_row < STOP:
    counter_row = counter_row + 1
    triangle_num = triangle_num + counter_row
    print("Triangle #%d is %d" % (counter_row, triangle_num))