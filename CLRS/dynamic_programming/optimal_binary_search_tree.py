def optimal_BST(P, Q):
    n = len(P)
    """
    Args:
        P: probabilities of key
        Q: probabilities of dummy keys  
    """
    E = [[float('inf') for j in range(n + 2)] for i in range(n + 2)] # expected serch costs
    W = [[float('inf') for j in range(n + 2)] for i in range(n + 2)] # probabilities' sum
    R = [[0 for j in range(n)] for i in range(n)] # root list
    for step in range(-1, n - 1):
        for i in range(1, n + 1):
            j = i + step
            if i > n or j >= n:
                break
            if j == i - 1:
                E[i][j] = Q[j]
                W[i][j] = Q[j]
            else:
                W[i][j] = W[i][j - 1] + P[j] + Q[j]
                E[i][j] = float('inf')
                for r in range(i, j + 1):
                    e = E[i][r - 1] + E[r + 1][j] + W[i][j]
                    if e < E[i][j]:
                        E[i][j] = e
                        R[i][j] = r
    return (E, W, R)

def construct_optimal_BST(R, i, j, last_root):

    parent = "k" + str(last_root)
    
    if i > j and i >= len(R):
        print("d" + str(j) + " is the right child of " + parent)
        return

    r = R[i][j]
    child = "k" + str(r) if i <= j else "d" + str(j)
        
    if last_root == 0:
        print("k" + str(r) + " is root")
    elif j < last_root:
        print(child + " is the left child of " + parent)
    else:
        print(child + " is the right child of " + parent)

    if i > j:
        return

    construct_optimal_BST(R, i, r - 1, r)
    construct_optimal_BST(R, r + 1, j, r)
    

if __name__ == "__main__":
    # example
    #P = [0, 0.15, 0.10, 0.05, 0.10, 0.20]
    #Q = [0.05, 0.10, 0.05, 0.05, 0.05, 0.10]
    # 15.5-2
    P = [0, 0.04, 0.06, 0.08, 0.02, 0.10, 0.12, 0.14]
    Q = [0.06, 0.06, 0.06, 0.06, 0.05, 0.05, 0.05, 0.05]

    tup = optimal_BST(P, Q)
    
    E, W, R = tup[0], tup[1], tup[2]
    print("-------- E --------")
    for i in range(len(E)):
        print(E[i])
    print("-------- W --------")
    for i in range(len(W)):
        print(W[i])
    print("-------- R --------")
    for i in range(len(R)):
        print(R[i])
    print("-------------------")

    construct_optimal_BST(R, 1, len(P) - 1, 0)

    '''
    R[1, 5] = 2 root
    -R[1, 1] = 1 left
    --R[1, 0] left
    --R[2, 1] right
    -R[3, 5] = 5 right
    --R[3, 4] = 4 left
    ---R[3, 3] = 3 left
    ----R[3, 2] left
    ----R[4, 3] right
    ---R[5, 4] right
    --R[6, 5] right
    '''
                


    