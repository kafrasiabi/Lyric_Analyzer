import pprint
import operator

class Lyric_Analyzer():
    def __init__(self, song): 
        '''Initilizing Functin'''
        assert type(song) == str
        self.song = song

    def lyric_list(self):
        '''Creates list of lowercase lyrics with no punctuation'''
        lowercase = self.song.lower() 
        no_punctuation = lowercase.translate({ord(c): None for c in '(),!?:;'}) #jesus this took forever to figure out
        lyrics = no_punctuation.split() #makes a list of each word in the song
        return lyrics

    def word_frequency(self): #need to pass the lyric list as a parameter here
        '''Create dict that maps word frequency, sorts in order of high to low'''
        lyrics = self.lyric_list() #call internal function, basically retrieve the fixed lyrics list
        myDict = {} 
        for word in lyrics:
            if word in myDict:
                myDict[word] += 1 
            else:
                myDict[word] = 1
        return sorted(myDict.items(), key = operator.itemgetter(1), reverse = True)

    # def most_common_words(self):
    #     values = freqs.values()
    #     best = max(values)
    #     words = []
    #     for k in freqs:
    #         if freqs[k] == best:
    #             words.append(k)
    #     return (words,best)
    # def words_often(freqs,minTimes):
    #     result = []
    #     done = False
    #     while not done:
    #         temp = most_common_words(freqs)
    #         if temp[1] >= minTimes:
    #             resutl.append(temp)
    #             for w in temp[0]:
    #                 del(freqs[w])
    #         else:
    #             done = True
    #     return result

africa_toto = """
I hear the drums echoing tonight
But she hears only whispers of some quiet conversation
She's coming in, 12:30 flight
The moonlit wings reflect the stars that guide me towards salvation
I stopped an old man along the way
Hoping to find some long forgotten words or ancient melodies
He turned to me as if to say, "Hurry boy, it's waiting there for you"
It's gonna take a lot to take me away from you
There's nothing that a hundred men or more could ever do
I bless the rains down in Africa
Gonna take some time to do the things we never had
The wild dogs cry out in the night
As they grow restless, longing for some solitary company
I know that I must do what's right
As sure as Kilimanjaro rises like Olympus above the Serengeti
I seek to cure what's deep inside, frightened of this thing that I've become
It's gonna take a lot to drag me away from you
There's nothing that a hundred men or more could ever do
I bless the rains down in Africa
Gonna take some time to do the things we never had
Hurry boy, she's waiting there for you
It's gonna take a lot to drag me away from you
There's nothing that a hundred men or more could ever do
I bless the rains down in Africa
I bless the rains down in Africa
(I bless the rain)
I bless the rains down in Africa
(I bless the rain)
I bless the rains down in Africa
I bless the rains down in Africa
(Ah, gonna take the time)
Gonna take some time to do the things we never had
"""
print(Lyric_Analyzer(africa_toto).lyric_list())
pprint.pprint(Lyric_Analyzer(africa_toto).word_frequency())
