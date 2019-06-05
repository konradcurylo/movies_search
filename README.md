# movie_search
movie_search Django Rest-Framework -  movie database interacting with external APi http://www.omdbapi.com

Additional features of this app are:
-saving all data fetched from OMDB-API to own database 
-add comments to movies existing in database (and also store them in internal database)


You can use it as normal Django app, f.e. run using manage.py or add it to Your own project 
(don't forget about adding info in urls.py and settings.py).
For convenience, working version of this app is currently hosted on Heroku 



- POST /movies: with required parameter title containing movie title, returning details for given movie title,

- POST/movies/{'title':'movie_title_name'} in order add movie from omdb-api 

- GET /movies - returns list of all movies.

- POST /comments: with required parameter movie_id containing id of movie existing in database
  and parameter comment_content containing text of a new comment, returning added comment 

- GET /comments: with optional parameter movie_id containing id of movie existing in database, returning all 
  comments in database or (with argument) all comments for given movie_id.
 -GET /comments {"movie_id": 5} - returns all comments for movie with id 5

- GET/top returns top movies already present in the database ranking based on a number 
  of comments added to the movie  in the specified date range. The response  includes 
  the ID of the movie, position inrank and total number of comments.

- GET /top {"from": <date>, "to": <date>} - returns list of movies with top comments. If from and/or to are provided,
  only comments created in given time range will be returned 
