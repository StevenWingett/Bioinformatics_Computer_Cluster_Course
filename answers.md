# Answers
## Getting to grips with Linux
### Exercise 4
#### a
`date > date.txt`

`date >> date.txt`

Version

#### b
1.    `grep Scotland uk_counties.csv > scotland_counties.csv`
   
2.    `grep -v Scotland uk_counties.csv > other_counties.csv`

3.    `head -39 uk_counties.csv | tail -13`

#### c 
`mkdir TSV_links TXT_links`

1.    `cd TSV_links`
      `ln -s ../files_list/*.tsv .`
       
2.    `cd ../TXT_links`
      `ln -s ../files_list/[BC]*.txt .`


### Exercise 5
#### a
1.    `echo Steven >> add_name1.txt`

2.    `echo Steven >> /usr/bin/who` – Permission denied

      `ls -l /usr/bin/who`

3.    `groups`

#### b
`sort letters.txt > sorted.txt`

#### c
`curl -O https://raw.githubusercontent.com/StevenWingett/Bioinformatics_Computer_Cluster_Course/refs/heads/main/README.md`

#### d
1.    `echo $USER`

2.    `ps `

`top `

`top -u $USER`

3.    `which curl`

      `echo $PATH`

4.    `sleep 10`

5.    `sleep 10`  CTRL + C

6.    `sleep 10 &`


## Slurm
### Exercise 6
#### a
`module avail`

`module load R`

`Rscript --version`

#### c

1.    
`srun --pty bash`
`exit`

2.
`srun -c 4 --mem=5G --pty bash`
`exit` 

#### d

      #!/bin/bash
      Rscript norm_dist_1_billion.R

`sbatch -J Rscript_job -c 1 --mail-type=ALL --mail-user=$USER@mrc-lmb.cam.ac.uk --mem=3G norm_dist.sh`

`sbatch -J Rscript_job -c 1 --mail-type=ALL --mail-user=$USER@mrc-lmb.cam.ac.uk --mem=30G norm_dist.sh`

`sacct --format=jobID%20,CPUTime,MaxRSS -j [job id]`

