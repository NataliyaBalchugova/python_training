class Contact:

    def __init__(self, firstname=None, lastname=None, address=None, id=None,
                 homephone=None, mobilephone=None, workphone=None,
                 secondaryphone=None, all_phones_from_home_page=None, all_emails_from_home_page=None,
                 first_email=None, second_email=None, third_email=None):
        self.firstname = firstname
        self.lastname = lastname
        self.address = address
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.secondaryphone = secondaryphone
        self.first_email = first_email
        self.second_email = second_email
        self.third_email = third_email
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page
        self.id = id

    def __repr__(self):
        return "%s:%s:%s:%s:%s:%s" % (self.id, self.firstname, self.lastname, self.address, self.workphone,
                                   self.first_email)
