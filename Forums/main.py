from models import Member, Post
import stores


member1 = Member("Ahmad", 23)

member2 = Member("Samer", 29)

m_store = stores.MemberStore()

m_store.add(member1)

m_store.add(member2)

post1 = Post("Post1", "This is the first post")

post2 = Post("Post2", "This is the second post")

post3 = Post("Post3", "This is the third post")

p_store = stores.PostStore()

p_store.add(post1)

p_store.add(post2)

p_store.add(post3)


print("\n***** Forum Summary *****\n")

print("\n***** Members *****\n")

for member in m_store.get_all():

    print(member)

print("\n***** Posts *****\n")

for post in p_store.get_all():

    print(post)
