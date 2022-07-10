-- 1. Create and fill kinds of animals
CREATE TABLE kinds (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name NVARCHAR(20) NOT NULL
);
INSERT INTO kinds (`name`)
SELECT DISTINCT LOWER(TRIM(animal_type)) FROM animals
WHERE animal_type IS NOT NULL
AND animal_type != "";

-- 2. Create and fill breeds of animals with parsing if more that 1
CREATE TABLE breeds (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name NVARCHAR(60) NOT NULL
);
INSERT INTO breeds (`name`)
WITH RECURSIVE split(breed, data) AS (
    SELECT NULL, TRIM(breed)||"/"
    FROM animals
    UNION ALL
    SELECT
        TRIM(SUBSTR(data, 0, INSTR(data, "/"))),
        SUBSTR(data, INSTR(data, "/")+1)
    FROM split WHERE data != ""
)
SELECT DISTINCT breed FROM split
WHERE breed IS NOT NULL
AND breed != "";

-- 3. Create and fill possible colors of animals
CREATE TABLE colors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name NVARCHAR(20) NOT NULL
);
INSERT INTO colors (`name`)
SELECT DISTINCT `color` FROM (
    SELECT DISTINCT TRIM(`color1`) AS `color` FROM animals
    UNION ALL
    SELECT DISTINCT TRIM(`color2`) AS `color` FROM animals
)
WHERE `color` IS NOT NULL
AND `color` != ""
ORDER BY `color`;

-- 4. Create and fill table with name, birthday and kind_id of animals
CREATE TABLE the_animals (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name NVARCHAR(60),
    kind_id INTEGER NOT NULL,
    birthday VARCHAR(30),
    old_id VARCHAR(10),
    FOREIGN KEY (kind_id) REFERENCES kinds(id)
);
INSERT INTO the_animals (name, kind_id, birthday, old_id)
SELECT animals.name, kinds.id, animals.date_of_birth, animals.animal_id
FROM animals
LEFT JOIN kinds ON LOWER(TRIM(animals.animal_type)) = kinds.name
GROUP BY animals.animal_id;

-- 5. Create and fill table with animal colors
CREATE TABLE animal_colors (
    color_id INTEGER NOT NULL,
    animal_id INTEGER NOT NULL,
    PRIMARY KEY (color_id, animal_id),
    FOREIGN KEY (color_id) REFERENCES colors(id),
    FOREIGN KEY (animal_id) REFERENCES the_animals(id)
);
INSERT INTO animal_colors (color_id, animal_id)
SELECT DISTINCT * FROM (
    SELECT colors.id, the_animals.id
    FROM animals
             LEFT JOIN colors ON TRIM(animals.color1) = colors.name
             LEFT JOIN the_animals ON animals.animal_id = the_animals.old_id
    WHERE animals.color1 IS NOT NULL
      AND animals.color1 != ""
    GROUP BY animals.animal_id
    UNION ALL
    SELECT colors.id, the_animals.id
    FROM animals
             LEFT JOIN colors ON TRIM(animals.color2) = colors.name
             LEFT JOIN the_animals ON animals.animal_id = the_animals.old_id
    WHERE animals.color2 IS NOT NULL
      AND animals.color2 != ""
    GROUP BY animals.animal_id
);

-- 5. Create and fill table with animal breads
CREATE TABLE animal_breeds (
    breed_id INTEGER,
    animal_id INTEGER,
    PRIMARY KEY (breed_id, animal_id),
    FOREIGN KEY (breed_id) REFERENCES breeds(id),
    FOREIGN KEY (animal_id) REFERENCES the_animals(id)
);
INSERT INTO animal_breeds
WITH RECURSIVE split(breed, data, animal_id) AS (
    SELECT
        NULL,
        animals.breed||"/",
        animals.animal_id
    FROM animals
    UNION ALL
    SELECT
        TRIM(SUBSTR(split.data, 0, INSTR(split.data, "/"))),
        SUBSTR(split.data, INSTR(split.data, "/")+1),
        split.animal_id
    FROM split WHERE data != ""
)
SELECT DISTINCT breeds.id, the_animals.id
FROM split
LEFT JOIN breeds on split.breed = breeds.name
LEFT JOIN the_animals on split.animal_id = the_animals.old_id
WHERE split.breed IS NOT NULL
AND split.breed != "";

-- 6. Create and fill table with programs for animals
CREATE TABLE "stray-services" (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name NVARCHAR(20) NOT NULL
);
INSERT INTO "stray-services" (name)
SELECT DISTINCT outcome_subtype FROM animals
WHERE outcome_subtype IS NOT NULL
AND outcome_subtype != "";

-- 7. Create and fill table with statuses for animals
CREATE TABLE statuses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name NVARCHAR(20) NOT NULL
);
INSERT INTO statuses (name)
SELECT DISTINCT outcome_type FROM animals
WHERE outcome_type IS NOT NULL
AND outcome_type != "";

-- 8. Create and fill outcomes
CREATE TABLE outcomes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    animal_id INTEGER,
    service_id INTEGER,
    status_id INTEGER,
    year INTEGER NOT NULL,
    month INTEGER NOT NULL,
    FOREIGN KEY (animal_id) REFERENCES the_animals(id),
    FOREIGN KEY (service_id) REFERENCES "stray-services"(id),
    FOREIGN KEY (status_id) REFERENCES statuses(id)
);
INSERT INTO outcomes (animal_id,
                      service_id,
                      status_id,
                      year,
                      month)
SELECT
    the_animals.id,
    "stray-services".id,
    statuses.id,
    animals.outcome_year,
    animals.outcome_month
FROM animals
LEFT JOIN the_animals ON animals.animal_id = the_animals.old_id
LEFT JOIN "stray-services" ON animals.outcome_subtype = "stray-services".name
LEFT JOIN statuses ON animals.outcome_type = statuses.name;

-- 9. Delete temporally column old_id in the the_animals table
ALTER TABLE the_animals DROP COLUMN old_id;

-- 10. Delete source table
DROP TABLE animals;

-- 11. Rename table the_animals to the animals
ALTER TABLE the_animals RENAME TO animals;


