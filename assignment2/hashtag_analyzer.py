post_list = []

hashtag_count = {}

user_set = set()
while True:
    user = input("Enter User Name: ").lower()
    hashtag = input("Enter Hashtag: ").lower()
    if hashtag == "banned":
        print("Banned Hashtag Found")
        break
    if hashtag == "":
        print("Empty Hashtag")
        continue
    post = (user, hashtag)
    post_list.append(post)
    user_set.add(user)
    if hashtag not in hashtag_count:
        hashtag_count[hashtag] = 1
    else:

        hashtag_count[hashtag] += 1
print("\nPosts")
for post in post_list:
    print(post)

print("hashtag Counts")
for tag, count in hashtag_count.items():
    if count >= 5:
        status = "Trending"
    elif count >= 3:
        status = "Rising"

    else:
        status = "Flat"
    print(tag, ":", count, "-", status)
print("Unique Users:", len(user_set))
top_hashtag = ""
highest = 0
for tag, count in hashtag_count.items():

    if count > highest:
        highest = count
        top_hashtag = tag

print("Top Hashtag:", top_hashtag)