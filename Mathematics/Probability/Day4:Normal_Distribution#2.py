import math

def normal_cdf(x, mu, sigma):
    """Cumulative distribution function for N(mu, sigma^2)."""
    return 0.5 * (1 + math.erf((x - mu) / (sigma * math.sqrt(2))))

# Given parameters
mu = 20.0
sigma = 2.0

# 1) P(X < 19.5)
p1 = normal_cdf(19.5, mu, sigma)

# 2) P(20 < X < 22) = P(X < 22) - P(X < 20)
p2 = normal_cdf(22.0, mu, sigma) - normal_cdf(20.0, mu, sigma)

# Print with 3 decimal places
print(f"{p1:.3f}")
print(f"{p2:.3f}")
