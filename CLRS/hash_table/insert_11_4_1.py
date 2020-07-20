m = 11

c1 = 1
c2 = 3

def h_(k):
    return k

def h_linear_probing(k, i):
    return (h_(k) + i) % m - 1

def h_quadratic_probing(k, i):
    return (h_(k) + c1 * i + c2 * i * i) % m - 1

def h1(k):
    return k

def h2(k):
    return 1 + k % (m - 1)

def h_double_hashing(k, i):
    return (h1(k) + h2(k) * i) % m - 1

if __name__ == "__main__":
    T = [None] * m
    A = [10, 22, 31, 4, 15, 28, 17, 88, 59]
    count, key = 0, 0
    for a in A:
        for i in range(0, m):
            key = h_double_hashing(a, i)
            if T[key] == None:
                T[key] = a
                break
        print(count, " - ", T)
        count += 1
        