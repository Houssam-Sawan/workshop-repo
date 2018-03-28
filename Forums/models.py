class Member:
    ''' Descripes a Forum's member '''

    def __init__(self, name, age):
        ''' Initialize new Member '''

        self.name = name

        self.age = age

        self.id = 0


    def __str__(self):
        ''' Return class info as printable string'''

        return f"ID: {self.id} || Name: {self.name} || Age: { self.age }"


class Post:
    ''' Descripes a Forum's post '''

    def __init__(self, title, bodytxt=""):
        ''' Initialize new Post '''
        
        self.title = title

        self.txt = bodytxt

        self.id = 0


    def __str__(self):
        ''' Return class info as printable string'''
        
        return f"ID: {self.id} || Title: {self.title}\n{ self.txt }\n"



