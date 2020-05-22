import random
import copy

# Write a program that takes as input a positive integer n and a size k <= n, 
# and returns a size-k subset of [0, 1, 2, ... , n - 1]. The subset should be represented as an array. 
# All subsets should be equally likely and, in addition, 
# all permutations of elements of the array should be equally likely. 
# You may assume you have a function which takes as input a nonnegative integer t and 
# returns an integer in the set [0, 1, ... , t - 1] with uniform probability.
def random_sub_set(S, k):
  H = {}
  for i in range(k):
    r = random.randint(i, len(S) - 1)
    i_value, r_value = H.get(r, r), H.get(i, i)
    H[i] = i_value
    H[r] = r_value
  return [H[i] for i in range(k)]

def random_subset_answer(n, k) :
    changed_elements = {}
    for i in range(k) :
        # Generate a random index between j and n - 7, inclusive.
        rand_idx = random.randrange(i, n)
        rand_idx_mapped = changed_elements.get(rand_idx, rand_idx)
        i_mapped = changed_elements.get(i, i)
        changed_elements[rand_idx] = i_mapped
        changed_elements[i] = rand_idx_mapped
    return [changed_elements[i] for i in range(k)]

if __name__ == "__main__":
    A = [x for x in range(10)]
    random.shuffle(A)
    STATICS = {x : 0 for x in range(10)}
    for i in range(1000000):
        B = random_sub_set(copy.copy(A), 1)
        STATICS[B[0]] += 1
    print(STATICS)
    A = {0, 1, 2}
    STATICS = {1 : 0, 2 : 0, 3 : 0}
    for i in range(150000):
        B = random_sub_set(A, 2)
        STATICS[(B[0] + B[1])] += 1
    print(STATICS)