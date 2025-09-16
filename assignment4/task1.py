try:
   
    with open("sample.txt", "r") as file:
       
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("Error: The File 'sample.txt' does not exist.")
except Exception as e:
    print("An unexpected error occurred:", e)
