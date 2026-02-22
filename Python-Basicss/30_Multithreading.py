import time
import threading  

def cal_square(numbers):
    print("Calculate Square Numbers:")
    for n in numbers:
        time.sleep(0.2)
        print("square: ", n*n)

def cal_cube(numbers):
    print("Calculate Cube Numbers:")
    for n in numbers:
        time.sleep(0.2)
        print("cube: ", n*n*n)

numbers = [2, 4, 8, 10]
t = time.time()

t1 = threading.Thread(target= cal_square, args= (numbers,))
t2 = threading.Thread(target= cal_cube, args= (numbers,))

t1.start()
t2.start()

t1.join()
t2.join()

print("done in ", time.time()-t)
print("Now all done.")
