with open('table_de_multiplication.txt', "a+") as file5:
    for i in range(1,11,1): #strictement inferieur a 11 <=> arrete a 10
        file5.write(f"La table de  multiplication de {i}\n")
        for j in range(1,11,1):
            file5.write(f"{i:02d} x {j:02d} = {i*j}\n")
        file5.write("\n")
