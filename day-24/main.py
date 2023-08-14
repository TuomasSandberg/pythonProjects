with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

with open("new_file.txt", mode="w") as file: #mode changes the read to write in this example "w" writes and "a" appends
    file.write("\nlisää tekstiä tänne")

