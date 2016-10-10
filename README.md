# Mallows_Permutation
Simulating the Mallows Permutation when parameter `q` is close to `1` and `n >> 1/(1-q)`.
# Mallows Processes
Given a parameter `q > 0`, the Mallows Processes `X_t` is defined as follows,
+ When `t=1`, `X_1 = [1]`.
+ At each time `t > 1`, we sample an index from `{0, 1,..., t-1}` such that the probability of `i` being chosen is proportional to `q^i`. We obtain `X_t` by inserting `t` into `X_{t-1}` at index `i`.
It can be verified that at each time `t`, `X_t` thus defined is Mallows distributed with parameter `1/q`.

