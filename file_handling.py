# File Handling and Data Storage


user_input = []
print("Enter strings (Write 'ok' after completing the string):")
while True:
    string = input("Enter a string you want to add: ")
    if string.lower() == 'done':
        break
    user_input.append(string)


with open("data.txt", "w") as file:
    for line in user_input:
        file.write(line +" " )


print("\nContent of data.txt:")
with open("data.txt", "r") as file:
    for line in file:
        print(line.strip())
