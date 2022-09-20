/*
sampleQueries.sql
author: Antonio Marino

ASSUMPTIONS and NOTES:
- each query should return a single percentile,
VO2 Max Score, or Treadmill runtime.

- The percentile rank is represented as 100*the percentile
and must be reformatted before being outputted to the user.

- Assume that the percentile rank is an int that ranges from
0 to 9999 inclusive (In other words the percentile entered
by the user is between 0 and 99.99%), and every value between
0 and 9999 is present within the dataset.

- Selecting values based on Men_Treadmill_run_time,
Women_Treadmill_run_time, and Combined_Treadmill_run_time
assumes that the user has chosen "Male", "Female", or
"Other" respectively as their gender.
If Gender was not provided, then the
Combined_Treadmill_run_time will be used

- The lower bound percentile rank must be less than or equal to
the upper bound percentile rank
*/

/*
Given a VO2 Max Score, determine the user's percentile rank
among Norwegians.
*/

WITH cte
AS
(
SELECT percentile, ROW_NUMBER() over(order by abs(Men_Est_VO2peak - 43.3769999999995)) as rw
FROM run
)SELECT *
FROM cte
WHERE rw<=1;

WITH cte
AS
(
SELECT percentile, ROW_NUMBER() over(order by abs(Women_Est_VO2peak - 43.3769999999995)) as rw
FROM run
)SELECT *
FROM cte
WHERE rw<=1;

WITH cte
AS
(
SELECT percentile, ROW_NUMBER() over(order by abs(Combined_Est_VO2peak - 43.3769999999995)) as rw
FROM run
)SELECT *
FROM cte
WHERE rw<=1;

/*
Edge Cases:
*/
WITH cte
AS
(
SELECT percentile, ROW_NUMBER() over(order by abs(Men_Est_VO2peak - 0.000)) as rw
FROM run
)SELECT *
FROM cte
WHERE rw<=1;

WITH cte
AS
(
SELECT percentile, ROW_NUMBER() over(order by abs(Women_Est_VO2peak - 0.000)) as rw
FROM run
)SELECT *
FROM cte
WHERE rw<=1;

WITH cte
AS
(
SELECT percentile, ROW_NUMBER() over(order by abs(Combined_Est_VO2peak - 0.000)) as rw
FROM run
)SELECT *
FROM cte
WHERE rw<=1;

WITH cte
AS
(
SELECT percentile, ROW_NUMBER() over(order by abs(Men_Est_VO2peak - 1000.0)) as rw
FROM run
)SELECT *
FROM cte
WHERE rw<=1;

WITH cte
AS
(
SELECT percentile, ROW_NUMBER() over(order by abs(Women_Est_VO2peak - 1000.0)) as rw
FROM run
)SELECT *
FROM cte
WHERE rw<=1;

WITH cte
AS
(
SELECT percentile, ROW_NUMBER() over(order by abs(Combined_Est_VO2peak - 1000.0)) as rw
FROM run
)SELECT *
FROM cte
WHERE rw<=1;

WITH cte
AS
(
SELECT percentile, ROW_NUMBER() over(order by abs(Men_Est_VO2peak - 50.3769999999995)) as rw
FROM run
)SELECT *
FROM cte
WHERE rw<=1;

WITH cte
AS
(
SELECT percentile, ROW_NUMBER() over(order by abs(Women_Est_VO2peak - 50.3769999999995)) as rw
FROM run
)SELECT *
FROM cte
WHERE rw<=1;

WITH cte
AS
(
SELECT percentile, ROW_NUMBER() over(order by abs(Combined_Est_VO2peak - 50.3769999999995)) as rw
FROM run
)SELECT *
FROM cte
WHERE rw<=1;



/*
Given a percentile among Norwegians, determine the user's
VO2 Max Score.
*/


SELECT Men_Est_VO2peak FROM run WHERE percentile::float BETWEEN 4999 AND 4999 ORDER BY percentile;

SELECT Women_Est_VO2peak FROM run WHERE percentile::float BETWEEN 5000 AND 5000 ORDER BY percentile;

SELECT Combined_Est_VO2peak FROM run WHERE percentile::float BETWEEN 9990 AND 9990 ORDER BY percentile;


/*
Edge Cases:
*/
SELECT Men_Est_VO2peak FROM run WHERE percentile::float BETWEEN 0 AND 0 ORDER BY percentile;
SELECT Men_Est_VO2peak FROM run WHERE percentile::float BETWEEN 9999 AND 9999 ORDER BY percentile;
SELECT Men_Est_VO2peak FROM run WHERE percentile::float BETWEEN 5000 AND 5000 ORDER BY percentile;

SELECT Women_Est_VO2peak FROM run WHERE percentile::float BETWEEN 0 AND 0 ORDER BY percentile;
SELECT Women_Est_VO2peak FROM run WHERE percentile::float BETWEEN 9999 AND 9999 ORDER BY percentile;
SELECT Women_Est_VO2peak FROM run WHERE percentile::float BETWEEN 5000 AND 5000 ORDER BY percentile;

SELECT Combined_Est_VO2peak FROM run WHERE percentile::float BETWEEN 0 AND 0 ORDER BY percentile;
SELECT Combined_Est_VO2peak FROM run WHERE percentile::float BETWEEN 9999 AND 9999 ORDER BY percentile;
SELECT Combined_Est_VO2peak FROM run WHERE percentile::float BETWEEN 5000 AND 5000 ORDER BY percentile;

/*
Given a percentile, determine how long a Norwegian would last on the
Max Treadmill test.
Note: The current plan is to not include this query in the database
project, but it does allow users to gage how fast Norwegians
can run, and accomplishes user goals relating to that objective.
*/
SELECT Men_Treadmill_run_time FROM run WHERE percentile::float BETWEEN 4999 AND 4999 ORDER BY percentile;

SELECT Women_Treadmill_run_time FROM run WHERE percentile::float BETWEEN 4999 AND 4999 ORDER BY percentile;

SELECT Combined_Treadmill_run_time FROM run WHERE percentile::float BETWEEN 4999 AND 4999 ORDER BY percentile;


/*
Edge Cases:
*/
SELECT Men_Treadmill_run_time FROM run WHERE percentile::float BETWEEN 0 AND 0 ORDER BY percentile;
SELECT Men_Treadmill_run_time FROM run WHERE percentile::float BETWEEN 9999 AND 9999 ORDER BY percentile;
SELECT Men_Treadmill_run_time FROM run WHERE percentile::float BETWEEN 5000 AND 5000 ORDER BY percentile;

SELECT Women_Treadmill_run_time FROM run WHERE percentile::float BETWEEN 9999 AND 9999 ORDER BY percentile;
SELECT Women_Treadmill_run_time FROM run WHERE percentile::float BETWEEN 9999 AND 9999 ORDER BY percentile;
SELECT Women_Treadmill_run_time FROM run WHERE percentile::float BETWEEN 5000 AND 5000 ORDER BY percentile;

SELECT Combined_Treadmill_run_time FROM run WHERE percentile::float BETWEEN 0 AND 0 ORDER BY percentile;
SELECT Combined_Treadmill_run_time FROM run WHERE percentile::float BETWEEN 9999 AND 9999 ORDER BY percentile;
SELECT Combined_Treadmill_run_time FROM run WHERE percentile::float BETWEEN 5000 AND 5000 ORDER BY percentile;



/*
Given a treadmill runtime, determine the user's percentile rank
among Norwegians.
Note: The current plan is to not include this query in the database
project, but it does allow users to compare their athletic performance
to Norwegians, and accomplishes user goals relating to that objective
such as beginner runners who want to learn where they currently stand.
*/
WITH cte
AS
(
SELECT percentile, ROW_NUMBER() over(order by abs(Men_Treadmill_run_time - 500)) as rw
FROM run
)SELECT *
FROM cte
WHERE rw<=1;

WITH cte
AS
(
SELECT percentile, ROW_NUMBER() over(order by abs(Women_Treadmill_run_time - 500)) as rw
FROM run
)SELECT *
FROM cte
WHERE rw<=1;

WITH cte
AS
(
SELECT percentile, ROW_NUMBER() over(order by abs(Combined_Treadmill_run_time - 500)) as rw
FROM run
)SELECT *
FROM cte
WHERE rw<=1;

/*
Edge Cases:
*/
WITH cte
AS
(
SELECT percentile, ROW_NUMBER() over(order by abs(Men_Treadmill_run_time - 0)) as rw
FROM run
)SELECT *
FROM cte
WHERE rw<=1;

WITH cte
AS
(
SELECT percentile, ROW_NUMBER() over(order by abs(Women_Treadmill_run_time - 0)) as rw
FROM run
)SELECT *
FROM cte
WHERE rw<=1;

WITH cte
AS
(
SELECT percentile, ROW_NUMBER() over(order by abs(Combined_Treadmill_run_time - 0)) as rw
FROM run
)SELECT *
FROM cte
WHERE rw<=1;

WITH cte
AS
(
SELECT percentile, ROW_NUMBER() over(order by abs(Men_Treadmill_run_time - 600)) as rw
FROM run
)SELECT *
FROM cte
WHERE rw<=1;

WITH cte
AS
(
SELECT percentile, ROW_NUMBER() over(order by abs(Women_Treadmill_run_time - 600)) as rw
FROM run
)SELECT *
FROM cte
WHERE rw<=1;

WITH cte
AS
(
SELECT percentile, ROW_NUMBER() over(order by abs(Combined_Treadmill_run_time - 600)) as rw
FROM run
)SELECT *
FROM cte
WHERE rw<=1;


WITH cte
AS
(
SELECT percentile, ROW_NUMBER() over(order by abs(Men_Treadmill_run_time - 1000)) as rw
FROM run
)SELECT *
FROM cte
WHERE rw<=1;

WITH cte
AS
(
SELECT percentile, ROW_NUMBER() over(order by abs(Women_Treadmill_run_time - 1000)) as rw
FROM run
)SELECT *
FROM cte
WHERE rw<=1;

WITH cte
AS
(
SELECT percentile, ROW_NUMBER() over(order by abs(Combined_Treadmill_run_time - 1000)) as rw
FROM run
)SELECT *
FROM cte
WHERE rw<=1;

/*
References

Unitech, SE. (2021). How to Find Nearest Match Value in SQL.
  Youtube. https://www.google.com/search?q=how+to+select+value+that+is+closest+to+a+given+value+in+sql&oq=how+to+select+value+that+is+closest+to+a+given+value+in+sql&aqs=chrome..69i57j33i160.15231j0j7&sourceid=chrome&ie=UTF-8#kpvalbx=_-xYHYtXbM7qiptQPi86XuAw31
*/
