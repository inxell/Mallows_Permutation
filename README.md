# Mallows_Permutation
Simulating the Mallows Permutation when parameter `q` is close to `1` and `n >> 1/(1-q)`.
# Mallows Processes
Given a parameter `0 < q < 1`, the Mallows Processes `X_t` is defined as follows,
+ When `t = 1`, `X_1 = [1]`.
+ At each time `t > 1`, we sample an index from `{0, 1,..., t-1}` such that the probability of `i` being chosen is proportional to `q^i`. We obtain `X_t` by inserting `t` into `X_{t-1}` at index `i`.

It can be verified that at each time `t`, `X_t` thus defined is Mallows distributed with parameter `1/q`.
# When `n >> 1/(1-q)`
In this case, when `t` is large, the propability distribution of `i` is concentrated in the front part of `{0, 1,..., t-1}`. In order to capture those outliers when `i` is large, we need to simulate the choice of `i` more accurately. Here, instead of using just one uniform random variable to determine the value of `i` at each time `t`, we use multiple i.i.d. uniform random variables to determine the value of `i` in each step. We exploit the shift-invariance property of the distribution of `i`. Specifically, at time `t`, given `m` \in `{0, 1,..., t-1}`, conditioned on `i >= m`, the probability of `i - m = k` is proportional to `q^k`.

