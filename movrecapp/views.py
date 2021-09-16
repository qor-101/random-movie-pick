from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from imdb import IMDb
import random
# Create your views here.

def index(request):
    
    return render(request,"onlypage.html")


def getmov(request):
    
    ml=['Avatar', "Pirates of the Caribbean: At World's End", 'Spectre', 'The Dark Knight Rises', 'John Carter', 'Spider-Man 3', 'Tangled', 'Avengers: Age of Ultron', 'Harry Potter and the Half-Blood Prince', 'Batman v Superman: Dawn of Justice', 'Superman Returns', 'Quantum of Solace', "Pirates of the Caribbean: Dead Man's Chest", 'The Lone Ranger', 'Man of Steel', 'The Chronicles of Narnia: Prince Caspian', 'The Avengers', 'Pirates of the Caribbean: On Stranger Tides', 'Men in Black 3', 'The Hobbit: The Battle of the Five Armies', 'The Amazing Spider-Man', 'Robin Hood', 'The Hobbit: The Desolation of Smaug', 'The Golden Compass', 'King Kong', 'Titanic', 'Captain America: Civil War', 'Battleship', 'Jurassic World', 'Skyfall', "the preacher's wife", 'the christmas chronicles', "national lampoon's christmas vacation", 'home alone', 'love actually', 'krampus', 'a very harold & kumar christmas', 'the night before', 'scrooged', 'the best man holiday', 'black christmas', 'frosty the snowman', 'the ref', "mickey's christmas carol", 'the muppet christmas carol', 'the santa clause', 'merry christmas', 'happy christmas', 'white christmas', 'bad santa', 'batman returns', 'lethal weapon', 'the man who invented christmas', "the bishop's wife", 'gremlins', 'elf', 'christmas in connecticut', 'a christmas carol', 'a christmas tale', 'kiss kiss, bang bang', 'Good Boys', 'Stuber', 'Shazam', 'When we first met', 'Blockers', 'Game Night', 'Jumanji: Welcome to the jungle', 'Thor: Ragnarok', 'The Other Woman', 'How To Be A Latin Lover', 'A Very Harold & Kumar 3D Christmas', 'Going In Style', 'Chips', 'The Dictator', 'War Dogs', 'Step Brothers', 'Central Intelligence', 'Ted', 'Kenau', 'The Hangover', 'The Brothers Grimsby', 'Bad teacher', 'My big fat greek wedding 2', 'Superbad', 'The night before', 'Bridemaids', "Daddy's home", 'Project X', 'The Intern', 'Crazy, stupid love', 'ginger snaps', "jacob's ladder", 'in the mouth of madness', 'cabin fever', 'whisper', 'cube', 'the ring', 'a nightmare on elm street', 'Friday the 13th', 'the frighteners', 'haunted', '28 days later', 'anatomie', 'dawn of the dead', 'it', 'the crow', 'the shining', 'martyrs', 'the woman', "the devil's backbone", 'REC', 'saw', 'the deaths of ian stone', 'the craft', 'scream', 'urban legend', 'I know what you did last summer', 'tell no one', 'inside', 'wrong turn', 'Chances are', 'chocolat', 'under the tuscan sun', 'pretty woman', 'sabrina', 'music and lyrics', 'sleeping with other people', 'frankie & johnny', 'brown sugar', 'bride and prejudice', '13 going on 30', 'love actually', '10 things I hate about you', 'the five-year engagement', 'laggies', 'coming to america', 'reality bites', 'heartbreaker', 'doc hollywood', 'the wedding singer', 'fever pitch', 'tin cup', 'friends with kids', "you've got mail", 'keeping the faith', 'benny & joon', 'about time', 'hitch', 'in & out', 'baby boom', 'Hocus Pocus', 'Halloween', 'the nightmare before christmas', 'halloweentown', "trick 'r treat", 'the addams family', 'beetlejuice', 'casper', 'monster house', 'when good ghouls go bad', 'the haunting of hill house', 'the crow', "it's the great pumpkin, charlie brown", 'donnie darko', 'sleepy hollow', 'michael jackson: thriller', 'e.t the extra-terrestrial', 'the monster squad', 'the halloween tree', 'chilling adventures of sabrina', 'halloween wars', 'the midnight hour', 'the worst witch', 'the conjuring', 'ghostbusters', 'idle hands', "kiki's delivery service", 'scary stories to tell in the dark', 'house of 100 corpses', 'the rocky horror picture show', 'Perfectly prudence', 'Backyard Wedding', "A Valentine's Date", 'Smooch', 'Accidentally In Love', 'Time after time', 'The Shunning', 'Three Weeks, Three Kids', 'The Edge Of The Garden', 'Rock The House', 'Fixing Pete', 'A Taste of Romance', 'Undercover Bridesmaid', 'Notes From The Heart Healer', 'Kiss at Pine Lake', 'How to fall in love', 'The Music Teacher', 'Smart Cookies', 'Puppy Love', 'I married Who?', 'The Nearlyweds', 'The Sweeter Side Of Life', 'Be My Valentine', "Return to Nim's Island", 'Remember Sunday', 'Space Warriors', 'The Confession', 'Notes from Dad', 'Banner 4th of July', 'Second Chances']
    
    mov_name = ml[random.randint(0,209)]

    
    ia = IMDb()
    search = ia.search_movie(mov_name)
    mov_id = search[0].movieID
    movie = ia.get_movie(mov_id)
    mov_url = ia.get_imdbURL(movie)
    
    return redirect(mov_url) 
