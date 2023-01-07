import time as t

start = t.time()

for i in range(10):
    print(i)
    t.sleep(1) # kasih delay

end = t.time()
print(f"Runtime : {end-start}")