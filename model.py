import sqlite3

class Model:

    def __init__(self, title):
        self.title = title
        self.conn = sqlite3.connect("movie-library.db")
        self.cur = self.conn.cursor()

    def title_search(self):
        input_title = "%"+self.title+"%"
        self.cur.execute("""SELECT title, language, popularity, genre 
            FROM movies m
            JOIN genres g
            ON m.genre_id = g._id
            WHERE title LIKE :part_title
            ORDER BY popularity DESC
            LIMIT 5;""", 
            {
                'part_title': input_title
            }
            )
        movies= self.cur.fetchall()

        # need to return queried result to controller which sends it to view   
