class MemberStore:
    ''' Store for members '''

    members = []

    last_id = 1


    def get_all(self):
        ''' Get a list of all members '''

        return MemberStore.members


    def add(self, member):
        ''' Append new member '''
        
        member.id = MemberStore.last_id

        MemberStore.last_id += 1

        return MemberStore.members.append(member)


    def entity_exists(self, member):
        ''' check if member exists or not '''

        return member in MemberStore.members


    def get_by_id(self, id):
        ''' return a member by their id '''

        for memb in MemberStore.members:

            if memb.id == id :

                return memb

        return None


    def delete(self, id):
        ''' Delete a member by their id '''

        memb = MemberStore.get_by_id(self, id)

        try:

            MemberStore.members.remove(memb)

        except ValueError:

            print(ValueError("Member was not found"))

        



class PostStore:
    ''' Store for posts '''


    posts = []

    last_id = 1


    def get_all(self):
        ''' Get a list of all posts '''

        return PostStore.posts


    def add(self, post):
        ''' Add new post '''

        post.id = PostStore.last_id

        PostStore.last_id += 1

        return PostStore.posts.append(post)
        

    def entity_exists(self, post):
        ''' check if post exists or not '''

        return post in PostStore.posts


    def get_by_id(self, id):
        ''' return a post by their id '''

        for post in PostStore.posts:

            if post.id == id :

                return post

        return None


    def delete(self, id):
        ''' Delete a post by their id '''

        post = PostStore.get_by_id(self, id)

        try:

            PostStore.posts.remove(post)

        except ValueError:

            print(ValueError("Post was not found"))
        


    