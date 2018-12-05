def primes_file(upto_n, filename):
    primes = [2]
    outputfile = open(filename, "wt")

    for num in range(primes[-1] + 1, upto_n + 1, 1):
        p = True
        for div in primes:
            if num % div == 0:
                p = False
                break
            if div > num**0.5:
                break
        if p:
            primes.append(num)

    print(len(primes))
    outputfile.write(str(primes))
    outputfile.close()

primes_file(1000000, "primos_1000000.txt")

# def primes_file(upto_n, filename):
#     primes = [2]
#     outputfile = open(filename, "wt")
#     lines = 0
#     msg = ""
#
#     for num in range(primes[-1], upto_n + 1):
#         p = True
#         for div in primes:
#             if num % div == 0:
#                 p = False
#                 msg = " divisible by " + str(div)
#                 break
#         if p:
#             primes.append(num)
#             msg = " is prime"
#
#         outputfile.write(str(num) + msg + "\n")
#
#     outputfile.write(str(primes))
#     outputfile.close()
#
# primes_file(1000, "primos_1000.txt")
