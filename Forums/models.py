class Member:
    ''' Descripes a Forum's member '''

    def __init__(self, name, age):
        ''' Initialize new Member '''

        self.name = name

        self.age = age


class Post:
    ''' Descripes a Forum's post '''

    def __init__(self, title, bodytxt=""):
        ''' Initialize new Post '''
        
        self.title = title

        self.txt = bodytxt



