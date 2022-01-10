class SetList:
    """
    Class is used to generate setlists
    """

    def __init__(self, title):
        """
        initialize the class

        Parameters
        ----------
        self.title : str
            set list title
        self.song_list : list
            the list of songs needing int he setlist
        """
        
        self.title = title
        self.set_list = []

    
    def add_songs(self, **kw):
        """
        add songs to setlist

        Parameters
        ----------
        takes number of kwargs:
        set_order : int
            song in the set order
        song_title : str
            Song Name
        song_artist : str
            Song writer
        song_url : str 
            optional for adding url for playback
        song_bpm : float 
            optional
        """

        self.set_order = kw.get('set_order', 0)
        self.song_title = kw.get('song_title')
        self.song_artist = kw.get('song_artist')
        self.song_url = kw.get('song_url', 'no link provided')
        self.song_bpm = kw.get('song_bpm', -1)
        

        # append song to song_list
        self.set_list.append([self.set_order, self.song_title, self.song_artist, self.song_url, self.song_bpm])

