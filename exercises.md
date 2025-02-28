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
`tar xvfp course_data_for_participants.tar`

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

3. To what `groups` do you belong?

### b. 
1. Write a single-line Bash command that takes the contents of the file letters.txt, sorts them alphabetically and then writes them to a new file named `sorted.txt`.

### c. 
1. Write a Bash command to download the file: https://raw.githubusercontent.com/StevenWingett/lmb-nextflow/main/docs/README.md
(Hint: `curl` can name the downloaded file the same as the file on the remote server – look in the Linux man pages to find the relevant `curl` flag.)

### d.
1. Print the contents of the `$USER` variable to the screen.  Look familiar?

2. List your running processes with `ps`.  Then look at all jobs running on your current node with `top`.  Then look at ONLY YOUR jobs running on your current node using `top`.

3. Where is the `curl` program found on your system?  Check this location is indeed in the `$PATH` variable.

4. Use the `sleep` command to suspend execution on your system for 10 seconds.

5. Try the sleep command again, but stop the job once it has started and then `kill` it.

6. Try the sleep command once again, but this time background the job.


# Next-generation sequencing
## Exercise 6
### a.
You have received 3 FASTQ files named sample1.fastq.gz, sample2.fastq.gz and sample3.fastq.gz.

1.  View the first few lines of one of the files to confirm it is indeed a FASTQ file.

2.  Let’s check the file transfer was successful.  The file sizes (bytes) should be:

sample1.fastq.gz : 3444
sample2.fastq.gz : 3477
sample3.fastq.gz : 3761

Is this what you see?

3. Installed on the cluster is a program named md5sum that produces a string of letters, numbers and symbols to represent a file.  Even a small change in a file will cause different characters to be returned.  This is an excellent way to check files are identical before and after transfer.  The md5 checksums of the original files are:

sample1.fastq.gz : 58b3dcc9e3bc866b406aa58c3d4b07dd  
sample2.fastq.gz : d5849a41e5661e853c6d5e309e558a03  
sample3.fastq.gz : c563d467ee22582728d02280826fd15e

Do you agree with these results?

4. Using command line Linux, combine the 3 FASTQ files into a gzipped single file named combined.fastq.gz.

5. How many reads are there in your newly created FASTQ file?  Use the command line to ascertain this (the command wc may help you).

### b. 
We are now going to try out a couple of bioinformatics tools.  However, since they are not distributed with Linux as standard, your system will need to be told where to find them.  The executable files are kept in: /public/genomics/soft/bin/

1.  Let’s now temporarily add that location to our $PATH variable.  

export PATH="$PATH:/public/genomics/soft/bin/"

Confirm that this new folder has been added to your path.

2.  FastQC is software used by most labs to assess the overall QC of their data and we want to run it on our combined FASTQ file.  Let’s read the manual:

man fastqc

Ah!  Since FastQC is external software, help will not be provided in the Linux built-in manual.  However, most external software tools will provide help with one of the following commands:

[software_name] -help 
[software_name] --help

Try this for FastQC.

3.  Analyse your combined dataset combined.fastq.gz with FastQC.  When it has finished running, copy the resulting HTML file to your local machine and see if you can interpret the results (please note that this is a tiny dataset for demonstration purposes).

### c.
1. Try viewing the file mapping_results.bam with cat.  What do you see?  Does zcat help?

2. Read the help for samtools to learn how to read the BAM file.  Browse the file.  Can you see the headers?  Can you see the aligned reads?

3. Run samtools flagstat on the file.  How many mapped reads are there?

# Slurm
## Exercise 7
### a.
1. Look at all the currently running jobs submitted to the cluster.  Can you see any long-running jobs?  Are CPU / GPU nodes being used?  Who has most jobs running on the cluster?

2. Look at the sqsummary command.  What percentage of CPUs are currently available?

3. Look at the sinfo command.

4. Look at qinfo webpage: http://nagios2/qinfo/

Are most of the CPU nodes in use?  Are any nodes listed as “down”?  Which user is using the most CPU nodes?

### b.
1. Create a Bash script that creates a 60 second pause.

2. Run the script as an interactive job on a compute node.  

3. Exit the compute node and submit the Bash script as a non-interactive job. Check it is in the cluster queue.

### c.
Run FastQC as before, but this time submit as a non-interactive job.  Make sure the cluster emails you about the job’s progress.  Specify what seems an appropriate number of CPUs and memory.

### d.
Look at the available modules for the latest version of R.  Import this latest version of R as a cluster module.  Check this version of R is indeed now running on your system.


# Nextflow and nf-core
## Exercise 8
### a.
1. Let’s set up Nextflow on your system. Go to the head node and execute the following one-line command:
$ curl -s https://raw.githubusercontent.com/StevenWingett/lmb-nextflow/main/nextflow_setup_cluster.sh | bash

From what you have learnt in the course already, does this command make sense to you?  This command downloads a bash script from a remote server and then runs it.

2. There is a hidden Bash configuration file in your home directory named .bashrc.  Running the command above should have edited this file?  Has this happened (check the date).

(Remember that hidden files begin with a dot and can be viewed with ls --all).

3. Read the contents of the .bashrc file.  Changes will have been made to the end of the file.  Can you make sense of these?

4. Run the testing command:
$ nextflow run hello

What do you see? 

### b. 
1. Let’s use nf-core to download FASTQ files.  Navigate to the webpage: https://www.ncbi.nlm.nih.gov/sra/SRR5413016

We would like to download the FASTQ files for the accessions SRR5413015 and SRR5413016.  

Create a text file with each of these accessions listed on a separate line (make sure there are no spaces or blank lines in this file).  Name the file to_download.txt.

Now use GUIde Piper to create a Nextflow command to download these files.  

Go to the internal GUIde Piper website (http://nextflow.lmb.internal/) and select the “Download Data” option.  Input the name of your file (to_download.txt) and use GUIde Piper to generate a Nextflow command.  Now run this command on a head node.


2. Did the job complete successfully?  Did you receive an email?  Can you see the downloaded FASTQ files (look inside any folders generated)?

3. Can you see the metadata?  Copy it to your local machine (e.g. use FileZilla) and view in suitable software (e.g. Excel)?

4. Let’s make some nicer filenames.  Download this file:
https://raw.githubusercontent.com/StevenWingett/lmb-nextflow/main/ancillary_scripts/fetchngs_renamer.py

Go to the folder that contains the results folder and then run the command:
python3 fetchngs_renamer.py

What did this do?

### c.
Suppose you have received the results of a paired-end, non-strand specific Saccharomyces cerevisiae RNA-seq experiment.  There are 2 conditions, namely A and B.  The relevant files are:
yeast_rna_seq_A_1.fastq.gz
yeast_rna_seq_A_2.fastq.gz
yeast_rna_seq_B_1.fastq.gz
yeast_rna_seq_B_2.fastq.gz

[These are actually “toy” datasets which contain only a fraction of the original data in order to enable processing within the timeframe of the course.]

Process these datasets with the appropriate nf-core pipeline and settings.  To do this, read the nf-core documentation about the RNA-seq pipeline.  Then create a command using GUIde-Piper to process the RNA-seq datasets.

### d.
Let’s look at the results of the processing.  To start with, open the file muliqc_report.html that summarised the results of the pipeline.

1. What are the percentage of uniquely mapped reads for the Condition A and Condition B samples when using the aligner STAR?

2. Are the bulk of the aligned reads mapping to exonic, intronic or intergenic regions?

3. We specified that this was a non-strand specific library.  Were we correct in doing that?

4. What was the most frequent %GC for the reads in the input files?

5. Approximately what percentage of the reads terminated with adapter sequence?

5. What is the most frequent inner distance / insert size between the reads?  What does this mean?

7. It’s time to write up our Materials and Methods for a paper!  What version of STAR did we use to perform the alignment?

### e.
Let’s look at some more of the files we have produced.

1. Open the execution report.  Review the compute cluster resources used by the pipeline.  This is a good way to learn which tasks are more computationally intensive.

2. Can you find the BAM files?  Are you able to browse them using the command line?

3. View the file salmon.merged.gene_tpm.tsv.  Can you work out what is contained in here?
