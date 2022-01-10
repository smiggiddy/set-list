class Users:
    """
    For adding the user accounts for setlists
    """

    def __init__(self, setlist):

        self.id = ...
        self.first_name = ...
        self.last_name = ...
        self.password = ...
        self.setlist = setlist

        self.band_members = []

    def add_members(self, name, description, contact):
        """ 
        Method for adding setlist viewers
        """

        self.name = name
        self.description = description
        self.contact = contact 

        self.band_members.append([self.name, self.description, self.contact])