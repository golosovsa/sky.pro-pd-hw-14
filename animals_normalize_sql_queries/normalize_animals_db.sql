-- 1. Create and fill kinds of animals
CREATE TABLE kinds (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name NVARCHAR(20) NOT NULL
);
INSERT INTO kinds (`name`)
SELECT DISTINCT animal_type FROM animals
WHERE animal_type IS NOT NULL
AND animal_type != "";

-- 2. Create and fill breads of animals with parsing if more that 1
CREATE TABLE breads (
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

