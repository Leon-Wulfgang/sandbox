def fibonacci(n, mem=dict()):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        if n in mem:
            return mem[n]
        else:
            n_result = fibonacci(n-1, mem) + fibonacci(n-2, mem)
            mem[n] = n_result
            return n_result


#n = int(input())
n = 39
print(fibonacci(n))
