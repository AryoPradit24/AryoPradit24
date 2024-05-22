def find_numbers():
    lcm = 1533
    
    for a in range(2, lcm):
        if lcm % a == 0:
            b = lcm // a
            return a, b
    
    return None

numbers = find_numbers()
if numbers is not None:
    print("Bilangan a:", numbers[0])
    print("Bilangan b:", numbers[1])
else:
    print("Tidak ditemukan bilangan yang memenuhi persyaratan.")
