def runge_rule(sum, sum2, eps, k):
    return abs((sum - sum2) - (sum2 - sum) / (pow(2, k) - 1)) <= eps
