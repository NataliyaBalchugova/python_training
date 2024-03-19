class Contact:

    def __init__(self, firstname=None, lastname=None, address=None, id=None, homephone=None,
                                                mobilephone=None, workphone=None,
                 secondaryphone=None, all_phones_from_home_page=None):
        self.firstname = firstname
        self.lastname = lastname
        self.address = address
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.secondaryphone = secondaryphone
        self.all_phones_from_home_page = all_phones_from_home_page
        self.id = id
