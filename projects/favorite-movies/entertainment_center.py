import media
import fresh_tomatoes

#Movie object created using Movie class
mr_ms_smith = media.Movie("Mr and Mrs Smith",
                        "Two secret angents who fall for eachother",
                        "http://gephardtdaily.com/wp-content/uploads/2015/05/Mr-Mrs-Smith-Poster.jpeg",
                        "https://www.youtube.com/watch?v=7C1miwFdQOQ")

over_the_hedge = media.Movie("Over The Hedge",
                     "Animals go over the hedge to see the human world",
                     "http://www.impawards.com/2006/posters/over_the_hedge.jpg",
                     "https://www.youtube.com/watch?v=9p-0FxJ6kvQ")


men_in_black = media.Movie("Men in Black",
                           "Agency who fights aliens and protects Earth",
                           "http://www.impawards.com/1997/posters/men_in_black.jpg",
                           "https://www.youtube.com/watch?v=HYUd7AOw_lk")


love_and_basketball = media.Movie("Love and Basketball",
                             "Two highschool ballers fall in love",
                             "http://moviefiles.alphacoders.com/933/poster-9330.jpg",
                             "https://www.youtube.com/watch?v=Ur83i6_BjbE")

ace_ventura = media.Movie("Ace Ventura",
                          "Pet detective looking to solve crime",
                          "http://www.impawards.com/1994/posters/ace_ventura_pet_detective.jpg",
                          "https://www.youtube.com/watch?v=cXcH0f2B2vA")

dodgeball = media.Movie("Dodgeball",
                           "small gym tries to save itself with winnings from dodgeball tournament",
                           "http://moviefiles.alphacoders.com/120/poster-1209.jpg",
                           "https://www.youtube.com/watch?v=W-XbDZUnUmw")

#Array of movie objects used to create website
movies =[mr_ms_smith, over_the_hedge, men_in_black, love_and_basketball,
        ace_ventura, dodgeball]

#Call to fresh tomatoes file to create movie trailer website
fresh_tomatoes.open_movies_page(movies)

