from random import randint


n = randint(1, 300)

ran_arr = [randint(1, 10**9) for _ in range(n)]

id = randint(10**9, 10**10)

# write to file
with open(f"input_{id}.txt", "w") as f:
    f.write(f"{n}\n")
    f.write(" ".join(map(str, ran_arr)))
    f.close()



