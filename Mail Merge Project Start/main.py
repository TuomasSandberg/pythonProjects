#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
PLACEHOLDER = "[name]"

def mail_merge():
    with open("Input/Names/invited_names.txt","r") as invited_names:
        for names in invited_names:
            with open("Input/Letters/starting_letter.txt", "r") as starting_letter:
                letter = starting_letter.read()
                new_letter = letter.replace(PLACEHOLDER, names.strip())

            with open(f"Output/ReadyToSend/letter_for_{names}.txt", "w") as f:
                f.write(f"{new_letter}")



mail_merge()
    

    