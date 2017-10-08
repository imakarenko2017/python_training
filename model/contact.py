from sys import maxsize
# class contact

class Contact:
    def __init__(self,firstname=None,middlename=None, lastname=None,nickname=None,title=None,company=None,address=None,homephone=None,cellphone=None,workphone=None,email=None,email2=None,email3=None,homepage=None,birthday=None,birthmonth=None,birthyear=None,anniversary=None,address2=None,homephone2=None,notes=None,id=None):
        self.firstname=firstname
        self.middlename=middlename
        self.lastname=lastname
        self.nickname=nickname
        self.title=title
        self.company=company
        self.address=address
        self.address2=address2
        self.homephone=homephone
        self.homephone2=homephone2
        self.cellphone=cellphone
        self.workphone=workphone
        self.email=email
        self.email2=email2
        self.email3=email3
        self.birthday=birthday
        self.birthmonth=birthmonth
        self.birthyear=birthyear
        self.homepage=homepage
        self.anniversary=anniversary
        self.notes=notes
        self.id=id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and self.lastname==other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

