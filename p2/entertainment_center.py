import media
import fresh_tomatoes

# implement my favourate movies
ready_player_one = media.Movie("Ready Player One", "Story about virtual reality game in 2045",r"https://upload.wikimedia.org/wikipedia/en/7/74/Ready_Player_One_%28film%29.png","https://www.youtube.com/watch?v=cSp1dM2Vj48")

interstellar = media.Movie("Interstellar", "Dystopian future where humanity is struggling to survive", "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg", "https://www.youtube.com/watch?v=zSWdZVtXT7E")

flipped = media.Movie("Flipped", "Beautiful love story of gilr and boy", "https://upload.wikimedia.org/wikipedia/en/3/3a/Flipped_poster.jpg", "https://www.youtube.com/watch?v=cSxJTxSKHpw")

blade_runner_2049 = media.Movie("Blade Runner 2049", "Gosling plays K, a blade runner uncovers a secret between humans and replicants", "https://upload.wikimedia.org/wikipedia/en/9/9b/Blade_Runner_2049_poster.png","https://www.youtube.com/watch?v=gCcx85zbxz4")

three_idiots = media.Movie("3 idiots", "The film is about the friendship of three students at an Indian engineering college", "https://upload.wikimedia.org/wikipedia/en/d/df/3_idiots_poster.jpg","https://www.youtube.com/watch?v=xvszmNXdM4w")

hunger_games = media.Movie("Hunger games", "A really real reality show", "https://upload.wikimedia.org/wikipedia/en/3/39/The_Hunger_Games_cover.jpg", "https://www.youtube.com/watch?v=mfmrPu43DF8")

# add moviews to list and open static html
movies = [ready_player_one, interstellar, flipped, blade_runner_2049, three_idiots, hunger_games]
fresh_tomatoes.open_movies_page(movies)
