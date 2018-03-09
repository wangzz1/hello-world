def fibonacci(n):
    term = [0,1]
    i = 2
    while i <= n:
        term.append(term[i-2]+term[i-1])
    return term[n]

fibonacci(3)
