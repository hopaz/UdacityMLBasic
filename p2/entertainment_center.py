import media
import fresh_tomatoes

# implement my favourate movies
ready_player_one = media.Movie("Ready Player One", "Story about virtual reality game in 2045","https://img1.doubanio.com/view/photo/raw/public/p2516499649.jpg","https://www.youtube.com/watch?v=cSp1dM2Vj48")

interstellar = media.Movie("Interstellar", "Dystopian future where humanity is struggling to survive", "https://img3.doubanio.com/view/photo/raw/public/p2206088801.jpg", "https://www.youtube.com/watch?v=zSWdZVtXT7E")

flipped = media.Movie("Flipped", "Beautiful love story of gilr and boy", "https://img3.doubanio.com/view/photo/raw/public/p663036666.jpg", "https://www.youtube.com/watch?v=cSxJTxSKHpw")

blade_runner_2049 = media.Movie("Blade Runner 2049", "Gosling plays K, a blade runner uncovers a secret between humans and replicants", "https://img1.doubanio.com/view/photo/raw/public/p2501864539.jpg","https://www.youtube.com/watch?v=gCcx85zbxz4")

three_idiots = media.Movie("3 idiots", "The film is about the friendship of three students at an Indian engineering college", "https://img3.doubanio.com/view/photo/raw/public/p579729551.jpg","https://www.youtube.com/watch?v=xvszmNXdM4w")

hunger_games = media.Movie("Hunger games", "A really real reality show", "https://img3.doubanio.com/view/photo/raw/public/p1460591675.jpg", "https://www.youtube.com/watch?v=mfmrPu43DF8")

# add moviews to list and open static html
movies = [ready_player_one, interstellar, flipped, blade_runner_2049, three_idiots, hunger_games]
fresh_tomatoes.open_movies_page(movies)
