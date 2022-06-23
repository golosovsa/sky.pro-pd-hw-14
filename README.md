# Homework 14
[link to the source](https://skyengpublic.notion.site/14-SQL-19417ff81e514e78a183c5a49b2d5c39)
### Task:
We will start working with SQL and learn basic database queries. First, use the knowledge gained in the simulator (on the sky.pro platform), and then make your simple project.
## What should you do:
### Step 0:
* Create a project in PyCharm, put the database file in the same folder.
* [The database is here.](https://github.com/skypro-008/lesson14/blob/master/part1/netflix.db)
* Import the `sqlite3` module to work with the database.
* Create a database connection using the `sqlite3.connect` method.

### Step 1:
* Implement search by `title`.
* If there are several films, output the latest one.
* Write a SQL query
* Write a function that takes a `title` and returns data in the following format:

```json
{
		"title": "title",
		"country": "country",
		"release_year": 2021,
		"genre": "listed_in",
		"description": "description"
}
```
* Write a view for /movie/<title> to display information about the movie.

# Step 2:
* Implement search by year.
* Write an SQL query. Limit output to 100 titles.
* Write a function that takes two years and returns data in the following format:
```json
[
	{"title":"title", "release_year": 2021},
	{"title":"title", "release_year": 2020},
	...
]
```
* Write a view for the /movie/<year>/to/<year> route with a list of dictionaries.

# Step 3:
* Implement a search by `rating`. Define groups: for children, for family viewing, for adults.

| `rating`    | Description |
| :-- | :-- |
| G | No age limit. |
| PG | Presence of the parents is desirable. |
| PG-13 | For children 13 years of age and older with the presence of parents. |
| R | Children under 16 years old are allowed to the session only in the presence of their parents. |
| NC-17 | Children under 17 are not admitted. |

* Write an SQL query.
* write a function that takes a list of valid `rating`s and returns data in the following format:

```json
[
	{
	 "title":"title",
	 "rating": "rating",
	 "description":"description"
	},
	{
		"title":"title",
	 "rating": "rating",
	 "description":"description"
   },
   ...
]
```

* Write multiple views that handle routes according to specific groups. Output in each list of dictionaries containing information about the name, rating and description.
 
| route | `rating` |
| :-- | :-- |
| /rating/children | G |
| /rating/family | G, PG, PG-13 |
| /rating/adult | R, NC-17 |

### Step 4:
* Write a function that takes a genre name as an argument and returns the 10 latest movies in json format.
* Write an SQL query (column name `listed_in`).
* Write a function that takes a genre and returns data in the following format:

```json
[
    {"title":"title", "description":"description"},
    ...
]
```

* Write a view `/genre/<genre>` that would return a list. The result should contain the title and description of each movie.

# Step 5:
* Implement a function that takes the names of two actors as an argument, stores all the actors in the cast column, and returns a list of those who have played with them more than 2 times.
* As a test, you can pass: `Rose McIver` and `Ben Lamb`, `Jack Black` and `Dustin Hoffman`.
* You __don't need to create a view__ for this task

# Step 6:
* Implement a function that can pass in a `type` (movie or series), a `release_year` and its `genre` and output a list of movie titles and descriptions in JSON format.
* Write a SQL query, then write a function that accepts `type`, `year`, `genre`.
* You __don't need to create a view__ for this task

## How it should be implemented  
### What will be checked in the homework:
- [ ] Correct database connection.
- [ ] Correct SELECT query with single field selection.
- [ ] Correct SELECT query with multiple field selection.
- [ ] Correct SELECT query with LIKE operator.
- [ ] Correct SELECT query with GROUP BY and count (correct use of the aggregation function).
- [ ] Correct usage of the LIMIT and OFFSET keywords.
- [ ] Correct usage of the data sorting keywords.


