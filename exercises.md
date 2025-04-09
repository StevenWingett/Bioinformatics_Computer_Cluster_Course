![LMB Logo](assets/lmb_logo.png)
 
 <hr> 

Licence
This manual is © 2025, Steven Wingett

This manual is distributed under the creative commons Attribution-Non-Commercial-Share Alike 2.0 licence. This means that you are free:

•	to copy, distribute, display, and perform the work

•	to make derivative works


Under the following conditions:

•	Attribution. You must give the original author credit.

•	Non-Commercial. You may not use this work for commercial purposes.

•	Share Alike. If you alter, transform, or build upon this work, you may distribute the resulting work only under a licence identical to this one.

Please note that:

•	For any reuse or distribution, you must make clear to others the licence terms of this work.
•	Any of these conditions can be waived if you get permission from the copyright holder.
•	Nothing in this license impairs or restricts the author's moral rights.

Full details of this licence can be found at 
http://creativecommons.org/licenses/by-nc-sa/2.0/uk/legalcode

<hr>

# Accessing the Cluster
## Exercise 1
### a.
1. Connect to the LMB cluster (you should already be connected to the LMB intranet) using a Mac terminal or Putty for Windows.

2.	What message do you see when you log in?

3.	Is your username displayed when you log in?

### b.
1.	Connect to the cluster using FileZilla.

2.	Using FileZilla, create a folder in your cluster home directory named `LMB_Cluster_Course_Exercises`.
Note: your home directory will be your username (e.g. `/lmb/home/jsmith`).

3. Copy the data files given to you at the start of this course into the directory on the cluster you just created.
   
<hr>

# Getting to grips with Linux
## Exercise 2
### a.
1.	Change your working directory to `LMB_Cluster_Course_Exercises` (which should already be in your home directory).

2. Confirm your new working directory with `pwd`.

3. Create a folder in here named `Exercise2`.

4. Rename this directory to `Exercise_2`.

### b.
1. Go into the folder `Exercise_2`.

2. Type `ls` to confirm the folder is empty.

3. We’ve not introduced the `touch` command so far, so let’s try it now.  Enter in the command line:
   
    touch file1.txt

Has anything happened?

### c.
1. What is the size of `file1.txt`?  (You will need to use a command to do this.)
`
2. Make a copy of `file1.txt` named `file2.txt`.

3. Are the file sizes the same?

4. Delete `file1.txt`.

### d.
1. Go “up a level” in the filesystem hierarchy (when you have done this you should be able to see the folder `Exercise_2` when you run the command `ls`).

2. Delete the folder `Exercise_2` with the command `rmdir`.

3. Did that work?  If not, why not, and find a way to delete `Exercise_2` (look in the manual about recursive deletions).

4. Display the recent Bash commands you have entered.

## Exercise 3
### a.
**Only perform this step if you were given the data files in the form of `tar` archive.**

If you did not extract the files before copying to the cluster, then let’s open the archive file we copied from your local machine to the cluster:
`tar xvzfp [course_title].tar.gz`

(The `tar` command is useful, as it allows multiple files and the associated file hierarchy to be stored within a single archive file.  You don’t need to understand this command at the moment.)

### b.
Explore the `MAZE` folder.  Use `cd` to move around the maze and `ls` to check what is in each room.  Can you find the treasure?

### c.
1. In the folder `Exercise_3` you will find a file entitled `poem.txt`.  Write out the contents to the screen using the command `cat`.

2. Now run a command so you can scroll through the text one page at a time.

3. Write out the first 7 lines of the poem to the screen.

4. Write out the bottom 3 lines of poem to the screen.

5. Add the line “The Waste Land by T. S. Elliot” to the start of the file.  And a blank line below this.  Save the file.

6. Compress the file.  Notice whether the file size changed after compression.  Did the filename change?

7. Read the compressed file with `cat` and then `zcat`.  What happens in each case?  

## Exercise 4
### a.
1. What does the command `date` do?
   
2. Try this command and redirect the output to a file named `date.txt`. 
   
3. Now try the command again, but this append the output to `date.txt`.
   
4. View the contents of date.txt.
   
5. What is the result of adding the flag `--version` to `date`? 

### b.
1. Look at the file named `uk_counties.csv`.  Using the `grep` command, create a new file named `scotland_counties.csv` that contains only Scottish counties.  

2. Using the `grep` command, create a new file named `other_counties.csv` that contains all counties except Scottish counties.  We advise reading the manual on `grep` to assist with this.  (Hint: this is inverting the grep matching.)

3. Using the commands `head` and `tail` and also using a pipe, create a file named `subset_counties.csv` that contains the counties on lines 27-39 of the original file.

### c.
Using a single wildcard, create symbolic links to files in the `files_list` folder that meet the following criteria:
1. end with the file extension `.tsv`.
2. start with `B` or `C` and end with the file extension `.txt`.

The links should be generate outside the file_list folder, in separate folders named `TSV_links` and `TXT_links`.

## Exercise 5
### a.
1. View the contents of the file `add_name1.txt` and then edit the file by adding your name to the end of the file.  However, don’t do this with a text editor (such as `nano`), but instead use a single Bash command which contains a re-direct.

2. Repeat 1., but this time edit the file `/usr/bin/who`.  Where you able to do this?  If not, why not?  Maybe checking the file permissions will clarify the situation?

3. To what groups do you belong (the name of the required Linux command is quite intuitive)?  To what groups does the person who is running the course belong?  If you can't work out how to do this, then look in the `man` pages.

### b. 
1. Write a single-line Bash command that takes the contents of the file letters.txt, sorts them alphabetically and then writes them to a new file named `sorted.txt`.

### c. 
1. Write a Bash command to download the file: https://raw.githubusercontent.com/StevenWingett/Bioinformatics_Computer_Cluster_Course/refs/heads/main/README.md
(Hint: `curl` can name the downloaded file the same as the file on the remote server – look in the Linux man pages to find the relevant `curl` flag.)

### d.
1. Print the contents of the `$USER` variable to the screen.  Look familiar?

2. List your running processes with `ps`.  Then look at all jobs running on your current node with `top`.  Then look at ONLY YOUR jobs running on your current node using `top` (look in the `man` pages for `top`, there is a flag that enables users to do this).

3. Where is the `curl` program found on your system?  Check this location is indeed in the `$PATH` variable.

4. Use the `sleep` command to suspend execution on your system for 10 seconds.

5. Try the `sleep` command again, but cancel the job once it has started.

6. Execute the sleep command for 60s, but this time background the job.  Can you see the running sleep command with `ps` and `top`? 

7. Try again, but set the sleep to 100s.  Suspend the command.  Can you see the suspended command with `ps`?  Now `kill` the sleep command. 

<hr>

# Slurm
## Exercise 6
### a.
Look at the available modules for the latest version of R.  Import this latest version of R as a cluster module.  Check this version of R is indeed now running on your system using the command: `Rscript --version`. [Note: to run R code already saved to a file, you need to execute the `Rscript` command.]

### b.
1. Look at all the currently running jobs submitted to the cluster.  Can you see any long-running jobs?  Are CPU / GPU nodes being used?  Who has most jobs running on the cluster?

2. Look at the `sqsummary` command.  What percentage of CPUs are currently available?

3. Look at the `sinfo` command.

4. Look at `qinfo` webpage: http://nagios2/qinfo/

Are most of the CPU nodes in use?  Are any nodes listed as “down”?  Which user is using the most CPU nodes?

### c.
1. Log in to a compute node, try some commands and then exit the compute node.

2.  Log in to a compute node, but this time reserve 4 cores and 5GB RAM.

### d.
Let's run the R script `norm_dist_1_billion.R` by submitting the job to the cluster as a non-interactive job.

This R script randomly generates 1 billion data values from a Normal Distribution.  The results are then plotted as a histogram.

Firstly, make a bash script named `norm_dist.sh` which contains the command:
`Rscript norm_dist_1_billion.R`.

(Don't forget the link to the Bash Shell at the top of the file!)

Now run the job, allocating 1 core and 1GB RAM.  Make sure the cluster emails you about the job’s progress.

Did the job succeed?  If not, try again but increase the RAM allocation to 30Gb.

Check how much RAM was actually used by this job.
