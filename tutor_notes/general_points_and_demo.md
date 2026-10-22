**Save the course data for participants as "course_data.tar.gz"**

**Bring a departmental laptop - just in case it is needed on the day**



**Demo Linux commands and the filesystem**
* ls (-l) and ls to path : folder/subfolder
* pwd
* cd  (. .. - ~)
* cp  (-r)
* mv  (move and rename)
* mkdir
* rmdir
* rm (-f -r)
* arrows/history/autocomplete/ CTRL A + CTRL E
* Briefly mention CTRL + C in case people get "locked" e.g. if they type cat, but nothing to follow

**Demo reading and writing to files**
* cat (don't show cat on a binary file, as this is a question)
* head  (wonderland.txt, demo numeric flags)
* tail
* more
* nano  (demo with / without filename)
* gzip
* zcat
* gunzip

**Demo VS Code**
* File browser
* Text editor
* Terminal
* Explain the marketplace
* FTP
* Show rainbow rendering of CSV files
* Show python file
* Show R file
* Show Jupyter Notebook file

**Leave at least half an hour after participants have attempted Exercise 6 to wrap up the course**

* Move to a compute node:
`srun --pty bash`

    Prompt change: username@fmb376

    There are options: 
    `srun -c 8 --pty bash`

* Execute script on a head node:
  `bash sleep.sh`

* Modules:

Don't actually import R, since this is an exercise
  
    `module avail`

    `module load [module name]`