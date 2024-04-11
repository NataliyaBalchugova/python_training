from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys


def generate():
    try:
            opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
    except getopt.GetoptError as err:
            getopt.usage()
            sys.exit(2)

    n = 5
    f = "data/contacts.json"

    for o, a in opts:
        if o == "-n":
            n=int(a)
        elif o == "-f":
            f = a

    file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

    def random_string_contact(prefix, maxlen):
        symbols = string.ascii_letters + string.digits
        return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

    testdata_contact = [Contact(
                                                            firstname=random_string_contact("firstname", 10),
                                                            lastname=random_string_contact("lastname", 20),
                                                            address=random_string_contact("address", 20),
                                                            workphone=random_string_contact("address", 30),
                                                            homephone=random_string_contact("home", 8),
                                                            mobilephone=random_string_contact("mobile", 8),
                                                            secondaryphone=random_string_contact("secondaryphone", 8),
                                                            first_email=random_string_contact("email", 10),
                                                            second_email=random_string_contact("email2", 40),
                                                            third_email=random_string_contact("email3", 40))

        for i in range(n)
                                                        ]


    with open(file, "w") as out:
        jsonpickle.set_encoder_options("json", indent = 2)
        out.write(jsonpickle.encode(testdata_contact))