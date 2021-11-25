import sqlite3

class Model:

    def __init__(self, title, date=None):
        self.title = title
        self.date = date
        self.conn = sqlite3.connect("movie-library.db")
        self.cur = self.conn.cursor()

    def title_search(self):
        input_title = "%"+self.title+"%"
        self.cur.execute("""SELECT title, language, popularity, genre, 'https://image.tmdb.org/t/p/w500' || movie_poster as movie_poster 
            FROM movies m
            JOIN genres g
            ON m.genre_id = g._id
            WHERE title LIKE :part_title
            ORDER BY popularity DESC
            LIMIT 1;""", 
            {
                'part_title': input_title
            }
            )
        self.movies= self.cur.fetchall()
        self.conn.commit()

        return self.movies

    def date_search(self):
        input_date = self.date
        self.cur.execute("""SELECT title, release_date, popularity, genre, 'https://image.tmdb.org/t/p/w500' || movie_poster 
            FROM movies m
            FROM movies m 
            JOIN genres g 
            ON m.genre_id= g._id
            WHERE release_date < :search_date
            ORDER BY release_date DESC
            LIMIT 1;""",
            {
                "search_date": input_date
            }
            )
        self.movies = self.cur.fetchall()
        self.conn.commit()
        return self.movies


    # def send_back(self):
        
    #     pass

        # need to return queried result to controller which sends it to view   
