banned_words = {"stupid", "idiot", "abuse", "spam"}
warnings = {}
delivered_messages = []
no_of_messages = int(input("Enter Number of Messages: "))
for i in range(no_of_messages):
    user = input("Enter User Name: ")
    text = input("Enter Message: ")
    message = (user, text)

    user = message[0]
    text = message[1]

    if text == "":
        print("Empty Message.")
        continue

    found = False

    words = text.split()

    for word in words:

        if word.lower() in banned_words:

            found = True
            break

    if found:

        if user in warnings:
            warnings[user] += 1
        else:
            warnings[user] = 1

        print(user, "Warning =", warnings[user])

        if warnings[user] == 3:
            print(user, "has been Banned.")
            break
    else:
        delivered_messages.append(message)
        print("Message Delivered.")