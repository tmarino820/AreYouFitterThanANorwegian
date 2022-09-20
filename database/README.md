
##Database Setup Individual:
##Are You Fitter Than a Norwegian?


#Antonio Marino
#Department of Computer Science
#CS 257.00: Software Design
#Professor Amy Csizmar Dalal
#February 11, 2022

The back end of this project needs to utilize statistics
about runs in order to tell users where they currently
rank among Norwegians or how well Norwegians can perform
their runs.

Our original dataset included data surrounding the
performance of Norwegians across percentiles over
many measures, and we removed values unrelated to
run performance. Also, the number of participants
in each exercise test was removed because it didn’t
relate to user goals. Because we were left with
relatively few categories, I selected one table
to represent the data: each row includes an
estimated VO2 max score, a run time on the max
treadmill test, and the percentile rank – *100 –
corresponding to these values. Each of these values
can be used to tell users how they rank among
Norwegians and how fast Norwegians can perform
their runs: the VO2 max score is a measure of
cardiovascular fitness, and the percentile rank
tells us how a particular score compares to the
body of data. We can output the corresponding
VO2 max score of Norwegians given a percentile
or calculate the percentile of users among
Norwegians given this VO2 score. Because the
original dataset represented VO2 max scores as
decimal values, we chose to represent them as
floats. While the current conception of this project
won’t directly use the treadmill run time data, I
included it because this project might use this data
in the future as another predictor of run performance.
We would likely apply it to the jack daniels equation,
which relates VO2 max scores and run descriptions
using seconds. This was why we chose to store this
value as an int in seconds. Lastly, we chose to
represent the percentile rank as 100*the percentile
converted to an int. Because we generated 10,000
values uniformly across percentiles in order,
storing the data this way allows us to avoid using
a slow, complex algorithm to find desired
percentiles. Our table contains columns for men,
women, and the averages between men and women
because users can choose to select or omit their
gender.


Two main queries will be performed on the data
in order to meet user goals:

One query finds the closest VO2 Max score to
a given score and outputs the corresponding
percentiles. This query allows users to enter
their VO2 Max score and see their percentile
rank among Norwegians. Likewise, by converting
their run description into a VO2 Max score
through the Jack Daniels equation, we can use
this same query to let users enter a description
of their runs and calculate their percentile
rank among Norwegians. The goal of the audience
is to see where they currently stand by
entering their statistics and receiving a
percentile, and this query does that. Another
query uses a given percentile to effectively
index into the data table. Then, the corresponding
VO2 Max Score is returned. The audience wants
to enter a percentile and get either the VO2
Max score or run performance of Norwegians in
that percentile. By using the percentile to
index into the dataset, this query quickly
finds the VO2 max score and fulfills the first
goal. Then, solving the Jack Daniels equation
in terms of this VO2 max score and the run
description allows us to output the run performance
of Norwegians in that percentile and meets the
second goal.

In the sampleQueries.sql file, I have also
implemented these two queries with the VO2
Max Score replaced with the Treadmill Max
Runtime. Even though the current plan is
to refrain from using the Treadmill Max Runtime,
we might change our minds as the project
progresses, and that was why I included these q
ueries.

##References

McKinney, Trenton. (2013). Change Column Type
in Pandas. Stack Overflow.
https://stackoverflow.com/questions/15891038/change-column-type-in-pandas.
