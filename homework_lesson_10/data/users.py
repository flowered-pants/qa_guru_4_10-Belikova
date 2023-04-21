import dataclasses


@dataclasses.dataclass
class Students:
    first_name = str
    last_name = str
    email = str
    gender = str
    number = str
    birthday = str
    subject = str
    hobbies = str
    picture = str
    address = str
    state_and_city = str

    def __init__(self, first_name, last_name, email, gender, number, birthday, subject, hobbies, picture,
                 address, state_and_city):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.gender = gender
        self.number = number
        self.birthday = birthday
        self.subject = subject
        self.hobbies = hobbies
        self.picture = picture
        self.address = address
        self.state_and_city = state_and_city
