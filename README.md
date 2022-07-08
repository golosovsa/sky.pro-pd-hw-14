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


# Cancelled 15 homework
[link to the source](https://skyengpublic.notion.site/15-SQL-2b9b172c85a5406389413b7bd7b23944)

### Task:

We have finished studying queries for creating tables, relationships between them, and also learned how to normalize the database. 
Let's try something else.
You will be working with a simple and non-normalized database.
You have to normalize it and create all the tables to implement it.
Now there is only one table in the database, which contains data from one of the American animal shelters. 
It contains information about pets and events associated with them: who was given to new owners, who got lost, and so on.

* `'age_upon_outcome'` is the age of the animal (at the time of arrival at the shelter).
* `'animal_id'` - animal ID.
* `'animal_type'` is the type of the animal.
* `'name'` is the name (alias).
* `'breed'` - breed.
* `'color1', 'color2'` - color or combination of colors.
* `'date_of_birth'` is the date of birth.
* `'outcome_subtype'` is the participant program. (In America there are different programs for homeless animals)
* `'outcome_type'` what is happening to the animal now.
* `'outcome_month'` is the month of the outcome.
* `'outcome_year'` is the year of the outcome.

## What should you do:

### Step 0:

* Create a project with PyCharm IDE and put the [database file](https://github.com/skypro-008/lesson15/blob/main/animal.db) there.

### Step 1:
* Import the `sqlite3` module to work with the database.
* Create a database connection using the `sqlite3.connect` method.

### Step 2:
* design a new, normalized-form database.

### Step 3:
* Write a SQL query to create new tables.

### Step 4:
* Create all tables and transfer the data into them.

### Step 5:
* Create a Flask application
* Create an /<itemid> route, such as /2 or /4, that would return information about a single object (choose the data format and key names yourself).

### Step 6:
* create a github repository and push the project in it.
* Don't forget about  `readme.md` and .`gitignore`.
* If you have used SQL to create and modify tables, push it too.

## How it should be implemented  
### What will be checked in the homework:
- [ ] Tables are correctly created.
- [ ] Relationships between tables are created.
- [ ] Tables are normalized to NF (normal form).
- [ ] Table columns are named correctly and clearly.
- [ ] Flask application written and working.

# Project status

- [x] HW14 done.
- [ ] HW15 in process
