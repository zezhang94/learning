import random
import copy
import itertools
import bisect

# You are given n numbers as well as probabilities p1, p1, ... , pn-1, 
# which sum up to 1. Given a random number generator that produces values in [0, 1) uniformly, 
# how would you generate one of the n numbers according to the specified probabilities?
def random_nonuniform(N, P):
  p, p_sum = random.uniform(0, 1), 0.0
  for i in range(0, len(P) - 1):
    if p >= p_sum and p < (p_sum + P[i]):
      return N[i]
    p_sum += P[i]
  return N[len(N) - 1]

# Elegant solution.
def nonuniform_randon_number_generation(values, probabilities):
  prefix_sum_of_probabilities = list(itertools.accunulate(probabilities))
  interval_idx = bisect.bisect(prefix_sum_of_probabilities, random.random())
  return values[interval_idx]
    
# Given a random number generator that produces values in [0,1] uniformly, 
# how would you generate a value X from T according to a continuous probability distribution, 
# such as the exponential distribution?
# TODO solve it


if __name__ == "__main__":
    N, P = [3, 5, 7, 11], [9 / 18, 6 / 18, 2 / 18, 1 / 18]
    STATICS = {x : 0 for x in N}
    for i in range(1000000):
        STATICS[random_nonuniform(N, copy.copy(P))] += 1
    print(STATICS)