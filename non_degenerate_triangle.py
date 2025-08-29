import os

# given 3 lines of specific lengths, determine if they can form a non-degenerate triangle


def triangleOrNot(a, b, c):
    result = []
    for x, y, z in zip(a, b, c):
        if (x > 0 and y > 0 and z > 0 and
                x + y > z and x + z > y and y + z > x):
            result.append("Yes")
        else:
            result.append("No")
    return result

if __name__ == "__main__":
    f = open(os.environ['OUTPUT_PATH'], 'w')

    a_cnt = 0
    a_cnt = int(input())
    a_i = 0
    a = []
    while a_i < a_cnt:
        a_item = int(input())
        a.append(a_item)
        a_i += 1


    b_cnt = 0
    b_cnt = int(input())
    b_i = 0
    b = []
    while b_i < b_cnt:
        b_item = int(input())
        b.append(b_item)
        b_i += 1


    c_cnt = 0
    c_cnt = int(input())
    c_i = 0
    c = []
    while c_i < c_cnt:
        c_item = int(input())
        c.append(c_item)
        c_i += 1


    res = triangleOrNot(a, b, c);
    for res_cur in res:
        f.write( str(res_cur) + "\n" )


