import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to life","http://movie.mtime.com/12058/posters_and_images/254592/","https://www.youtube.com/watch?v=5bMDPpxNbys")
# print(toy_story.storyline)

avatar = media.Movie("Avatar", "A marine on an alien planet", "https://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg", "https://www.youtube.com/watch?v=d1_JBMrrYw8")
# print(avatar.storyline)

flipped = media.Movie("Flipped", "Beautiful love story of gilr and boy", "http://huaban.com/pins/161970014/", "https://www.youtube.com/watch?v=cSxJTxSKHpw")
# print(flipped.storyline)
# flipped.show_trailer()
school_of_rock = media.Movie("School of Rock", "Using rock music to learn", "https://en.wikipedia.org/wiki/School_of_Rock#/media/File:School_of_Rock_Poster.jpg","https://www.youtube.com/watch?v=yMvpJDbWX_c")

ratatouille = media.Movie("Ratatouille", "A rat is a chef in Paris", "https://en.wikipedia.org/wiki/Ratatouille#/media/File:Ratatouille.jpg","https://www.youtube.com/watch?v=KSVKF0o2kfg")

midnight_in_paris = media.Movie("Midnight in Paris", "Going back in time to meet authors", "https://en.wikipedia.org/wiki/Midnight_in_Paris#/media/File:Midnight_in_Paris_Poster.jpg","https://www.youtube.com/watch?v=FAfR8omt-CY")

hunger_games = media.Movie("Hunger games", "A really real reality show", "http://www.mask9.com/node/137139", "https://www.youtube.com/watch?v=mfmrPu43DF8")

movies = [toy_story, avatar, school_of_rock, ratatouille, midnight_in_paris, hunger_games]
fresh_tomatoes.open_movies_page(movies)
