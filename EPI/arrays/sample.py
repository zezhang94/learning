import random
import copy
import itertools

# Implement an algorithm that takes as input an array of distinct elements and a size, 
# and returns a subset of the given size of the array elements.
# All subsets should be equally likely. 
def sample_offline(A, n):
  if n >= len(A):
    return A
  k = len(A) - n
  for i in range(k):
    A.remove(A[random.randint(0, len(A) - 1)])
  return A
# Return the result in input array itself.
def sample_offline_local(A, n):
  if n >= len(A):
    return
  for i in range(n):
    r = random.randint(i, len(A) - 1)
    A[r], A[i] = A[i], A[r]

# Design a program that takes as input a size k, and reads packets, 
# continuously maintaining a uniform random subset of size k of the read packets.
# Copy answer )-:
def sample_online(it, k):
  results = list(itertools.islice(it, k))
  num_seen_so_far = k
  for x in it:
    num_seen_so_far += 1
    r = random.randrange(num_seen_so_far)
    if r < k:
      results[r] = x
  return results


if __name__ == "__main__":
    A = [x for x in range(10)]
    random.shuffle(A)
    STATICS = {x : 0 for x in range(10)}
    for i in range(1000000):
        B = sample_offline(copy.copy(A), 1)
        STATICS[B[0]] += 1
    print(STATICS)
