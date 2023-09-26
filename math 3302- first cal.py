from scipy.stats import poisson

mu = 20

# Part (a)
prob_a = 1 - poisson.cdf(20, mu)

# Part (b)
prob_b = poisson.cdf(19, mu) - poisson.cdf(10, mu)

# Part (c)
prob_c = poisson.cdf(28, mu) - poisson.cdf(11, mu)

print(f"Part (a): P(X > 20) = {prob_a}")
print(f"Part (b): P(10 < X < 20) = {prob_b}")
print(f"Part (c): P(12 ≤ X ≤ 28) = {prob_c}")
