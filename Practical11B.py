n = int(input("Enter the number of students: "))
for i in range(n):
    name = input("Enter your name: ")
    address = input("Enter your address: ")
    city = input("Enter your city: ")
    pin = int(input("Enter your pincode: "))
    print("Enter 3 subject marks: ")
    m1 = int(input("Enter your m1: "))
    m2 = int(input("Enter your m2: "))
    m3 = int(input("Enter your m3: "))
    average = (m1 + m2 + m3)/3
    print(f'Record of {i+1}\nName: {name}\nAddress: {address}\nCity: {city}\nPin-code:{pin}\nAverage: {average}')