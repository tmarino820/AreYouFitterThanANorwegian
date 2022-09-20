# Database setup procedure

A transcript (of sorts) of the actions I took to set up my database on perlman, from the in-class demo in Week 5.

**Note**: this transcript assumes the following:

- I've already "cleaned up" my data and it only contains the columns I want to insert into my database.

- My data is in CSV format with no header row.

- I've already written my SQL scripts.

- I've made a directory within my local repository named `database` and my CSV file(s) and SQL scripts are located there.

## Step 1: Put CSV files and SQL scripts on perlman.

### Option 1: using git

On your machine (replace `[username]` with your CARLETON username)

    cd [YOUR LOCAL REPO DIRECTORY]
    git add database/*
    git commit -m "data files and sql scripts"
    git push

    ssh [username]@perlman.mathcs.carleton.edu
    [type yes if you get a scary looking question]
    [enter your CARLETON password when prompted]
    git clone [YOUR REPOSITORY URL].git
    
### Option 2: using sftp

On your machine (replace `[username]` with your CARLETON username)

    cd [YOUR LOCAL REPO DIRECTORY]
    cd database
    sftp [username]@perlman.mathcs.carleton.edu
    [type yes if you get a scary looking question]
    [enter your CARLETON password when prompted]
    put *
    quit

    ssh [username]@perlman.mathcs.carleton.edu
    
## Part 2: Create the database table and populate it

**Note**: you should still be ssh'ed into perlman for this part. I will be using the table names and filenames for my earthquakes dataset, but you should replace these with your own filenames and table names.

    psql -f createtable.sql  
    [enter your DATABASE PASSWORD if prompted.]

    psql
    \dt
    \copy earthquakes FROM 'all_month.csv' DELIMITER ',' CSV
    \quit

## Part 3: Run your query script to test your installation

Still on perlman:

    psql -f quakeQueries.sql

Assuming everything worked beautifully (ha!) and you're done, log off of perlman

    exit