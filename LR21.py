import random
try:
    with open("numbers.txt", 'w') as file:
        for i in range(20):
            contents = file.write(str("%.2f" %(random.uniform(-3, 3))))
            contents = file.write('\n')
    with open("numbers.txt", 'r') as file:
        contents = file.read()
    print(contents)
    with open("plus.txt", 'w') as file:
        exit
    t1=0
    t2=0
    with open("numbers.txt", 'r') as file:
        for i in file:
            if(float(i) > 0):
                t1= float(i)
                if(t1 > t2):
                    t2=t1
                    with open("plus.txt", 'a') as file:
                        contents = file.write(i)
        if(t1 == 0 or t2 == 0):
            with open("plus.txt", 'w') as file:
                contents = file.write("No + numbers")
        with open("plus.txt", 'r') as file:
            contents = file.read()
        print(contents)	
except:
    print("Error opening file")


