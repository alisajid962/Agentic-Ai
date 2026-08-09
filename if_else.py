while True:
        user1= input("Enter the input: ").lower()
        user2 = input("Ënter the input2: ").lower()
        if(user1=="paper" and user2=="rock"):
            print("User1 won ")
            break
        elif (user1=="rock" and user2=="paper"):
            print("user2 won")
            break
        elif(user1=="sciccor" and user2=="sciccor"):
            print("draw")
            continue
        elif(user1=="rock" and user2=="rock"):
            print("draw")
            continue
        elif user1=="paper" and user2=="paper":
            print("draw")
            continue
        elif(user2=="sciccor" and user1 =="paper" ):
            print("user2 won")
            break
        elif(user2=="sciccor" and user1=="rock"):
            print("user1 won")
            break
        else:
            print("invalid input")
            continue