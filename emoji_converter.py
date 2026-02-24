#accept user input 
message = input("Enter a message: ")
word = message.split(" ")
#Define the emoji dictionary
emoji_dict = {
    ":)": "😊",
    ":(": "😢",
    ":D": "😄",
    ":P": "😛",
    ":O": "😲"
}

#Convert the message to emojis
for w in word:
    if w in emoji_dict:
        print(emoji_dict[w], end = " ")
    else:
        print(w, end = " ")