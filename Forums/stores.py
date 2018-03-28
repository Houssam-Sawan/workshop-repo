class MemberStore:
    ''' Store for members '''

    members = []


    def get_all(self):
        ''' Get a list of all members '''

        return self.members


    def add(self, member):
        ''' Append new member '''
        
        return self.members.append(member)


class PostStore:
    ''' Store for posts '''


    posts = []


    def get_all(self):
        ''' Get a list of all posts '''

        return self.posts


    def add(self, post):
        ''' Add new post '''

        return self.posts.append(post)
