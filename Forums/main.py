from models import Member, Post


member1 = Member("Ahmad", 23)

member2 = Member("Samer", 29)

members = [member1, member2]

post1 = Post("Post1", "This is the first post")

post2 = Post("Post2", "This is the second post")

post3 = Post("Post3", "This is the third post")

posts = [post1, post2, post3]

print("\n***** Forum Summary *****\n")

print("\n***** Members *****\n")

for member in members:

    print(f"Name: {member.name}  || Age: { member.age }")

print("\n***** Posts *****\n")

for post in posts:

    print(f"Title: {post.title}")

    print(post.txt)

    print()
