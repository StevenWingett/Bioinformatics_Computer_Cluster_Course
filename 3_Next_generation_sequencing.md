![alt text](assets/lmb_logo.png)

# Course: Running Bioinformatics Software on a Linux Computer Cluster

## Licence
This manual is © 2025, Steven Wingett

This manual is distributed under the creative commons Attribution-Non-Commercial-Share Alike 2.0 licence. This means that you are free:

to copy, distribute, display, and perform the work

to make derivative works


Under the following conditions:

Attribution. You must give the original author credit.

Non-Commercial. You may not use this work for commercial purposes.

Share Alike. If you alter, transform, or build upon this work, you may distribute the resulting work only under a licence identical to this one.

Please note that:

For any reuse or distribution, you must make clear to others the licence terms of this work.
Any of these conditions can be waived if you get permission from the copyright holder.
Nothing in this license impairs or restricts the author's moral rights.

Full details of this licence can be found at 
http://creativecommons.org/licenses/by-nc-sa/2.0/uk/legalcode

 
 
# Next-generation sequencing
## Introduction
Next-generation sequencing (NGS) is a massively parallel sequencing technology that offers ultra-high throughput. The technology can be used for a wide range of applications, such as determining the genomic sequence of an organism, the expression levels of all the genes in a tissue, epigenetic modifications or even conformational changes.

The most commonly used NGS technology is the Illumina platform which generates millions to billions of short reads (typically 50 – 300bp in length) per run.  Should longer reads be required, then researchers can opt for PacBio or Oxford Nanopore platforms which generate much longer, but far fewer reads. Typical RNA-seq, ChIP-seq and ATAC-seq experiments use the Illumina technology and therefore this section discusses sequencing from the perspective of using this platform.

## Common types of analysis
In the past decade high-throughput sequencing has been widely adopted by the life sciences community, which in turn has led to an ever-expanding array of new molecular biology techniques.  

Common NGS-based protocols include:
    large whole-genome sequencing (human, plant, animal)	 	 	 	 
    small whole-genome Sequencing (microbe, virus)	
    exome & large panel sequencing (enrichment-based)	 	 	 	
    targeted gene sequencing (amplicon-based, gene panel)	
    single-cell profiling (scRNA-seq, scDNA-seq, oligo tagging assays)	 	 	
    transcriptome sequencing (total RNA-seq, mRNA-seq, gene expression profiling)	 
    targeted gene expression profiling	
    miRNA and small RNA analysis	
    DNA-protein interaction analysis (ChIP-seq)	 	 	
    methylation Sequencing	 	 	 	 
    16S metagenomic sequencing	 	
    metagenomic profiling (shotgun metagenomics, metatranscriptomics)	 	 	
    cell-free sequencing and liquid biopsy analysis
    chromosome capture sequencing (e.g. 3C, 4C, 5C, Hi-C, capture Hi-C)

While the library preparation and data analysis steps might be different for these applications, the sequencing process and data generated is broadly similar. 

## Equipment
There is currently a variety of different sequencers available which are tailored for different use cases.  Researchers need to balance experimental objectives in terms of coverage against cost factors and equipment availability in deciding what type of sequencing to perform.  Below gives an overview of the specifications of current (at the time of writing) Illumina sequencers.

    iSeq 100
    MiniSeq
    MiSeq Series 
    NextSeq 550 Series 
    NextSeq 1000 & 2000	NovaSeq 6000
Run Time (hours)		9.5–19 	4–24	4–55	12–30	11-48	13-44
Maximum Output (Gb)	1.2	7.5	15	120	330	6000
Maximum Reads	4 million		25 million		25 million	400 million		1.1 billion	20 billion
Maximum Read Length	2 × 150 bp	2 × 150 bp	2 × 300 bp	2 × 150 bp		2 × 150 bp	2 * 250

### Illumina sequencing process
The sequencing reaction takes place on equipment termed a flow cell.  The flow cell is subdivided into multiple lanes into which the sample libraries are added.  After addition of the sample, the flow cell is loaded into the sequencer.

Central to this sequencing methodology is the surface of the flow cell, which has been coated with a lawn of oligonucleotides.  Also, during library preparation, adapter sequences were appended to the sample DNA molecules.  Upon loading of the sample, the lawn olignonucleotides and adapter sequences  hybridise to one another, thereby anchoring the sample DNA to the flow cell surface.

Successive rounds of hybridisation, replication and then de-hybridisation on this oligonucleotide lawn leads to the target DNA molecules becoming amplified while, significantly, remaining in close proximity to all their clones.  This process is termed cluster generation by bridge amplification and generates millions of copies of single-stranded DNA. 

![Bridge Amplification](https://upload.wikimedia.org/wikipedia/en/7/75/DNA_Sequencing_Bridge_Amplification.png)

Figure 3 – bridge amplification, courtesy of Abizar, Wikipedia https://en.wikipedia.org/wiki/File:DNA_Sequencing_Bridge_Amplification.png

In a process called sequencing by synthesis (SBS), chemically modified nucleotides bind to the DNA template strand through base-pairing. Each of these synthetic nucleotides contains a fluorescent tag and a reversible terminator that blocks incorporation of the next base. A fluorescent emission signals when a nucleotide has been added, and the terminator is cleaved so the next base can bind.  Consequently, by recording the wavelength (colour) of the fluorescent emissions of each cluster, it is possible to deduce the sequence of the original “seeding” DNA molecule.

 ![Sequencing by synthesis](https://upload.wikimedia.org/wikipedia/commons/5/51/Sequence_By_Synthesis.png)

Figure 4 - sequencing by synthesis, courtesy of DMLapato, Wikipedia: https://commons.wikimedia.org/wiki/File:Sequence_By_Synthesis.png#filelinks

### Single-end / paired-end sequencing
For single-end sequencing, one read is reported for each sequenced DNA fragment.  In contrast, paired-end sequencing involves sequencing both ends of a fragment.  Paired-end sequencing aids the detection of genomic rearrangements and repetitive sequence elements, as well as gene fusions, novel transcripts and indels.

![Sequencing by synthesis](single_paired_end_sequencing.png)

Figure 5 - comparing single-end to paired-end sequencing

### Barcodes 
Different sample libraries can be pooled and then sequenced simultaneously by a process known as multiplexing.  With this strategy, barcode sequences are added to each DNA library preparation.  These barcodes are sequenced in addition to the DNA of interest, and thus different samples can be identified and separated from one another during the data analysis.

### UMIs
Unique molecular identifiers (UMIs) are a type of molecular barcoding that improves accuracy during sequencing.  The DNA molecules in the starting material are tagged with a UMI and therefore it is possible to bioinformatically identify and remove PCR sequence duplicates (as opposed to duplicates arising from independent DNA fragments of identical sequence).  This step is useful in a range of applications, such as RNA-seq expression analysis and variant calling, among others.

### File Formats
#### FASTQ
The standard data output format from these sequencers is known as FASTQ. Such FASTQ files are essentially text files which record the sequence of each read, along with an associated quality score which provides an estimate of the reliability of each base call. These files (usually in conjunction with genome reference and relevant metadata files) are what are processed by NGS bioinformatics pipelines.  Owing to their large size, FASTQ files are typically compressed using gzip.

You may already be familiar with FASTA format to report nucleotide sequences.  FASTQ format is similar to that, but it also reports a metric called a quality score, which reflects the likelihood of a given base-call being correct.

Look at the extract from a FASTQ file below, which shows the information pertaining to a single read.
  
    @SRR071233.197343 NRTG514-16_0001:3:2:6067:17258 length=40
    TGGGTAGTATTTGGTTACATGAGTAAGTTCTTTAATGGTG
    +
    CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCDC

Each read will comprise 4 lines of text:

Line1 – the contents of this line may vary, although it should always begin with the @ character and is then followed by the sequence identifier.  In this example, the identifier is a public repository accession number (SRR071233), followed by the number of reads within the file (197343). 

There is then additional information referring to the machine that was used to perform the sequencing.  There is also information about where the read was detected - 3:2:6067:17258 (lane3 : tile2 : x coo-ordinate 6067 : y co-ordinate 17258).  Also included in Line1 is the length of the read – which in this case is 40 base pairs.

Line 2 – the nucleotide sequence reported.  Bases that cannot be called with sufficient confidence are represented by an N.

Line 3 – by convention this is a + character (or sometimes a repeat of line 1).

Line 4 – the quality scores associated with each base-call.  In this case the quality score is either a C or a D.

##### Explanation of quality scores
This score reports the quality of the base-call two lines above and in the same column in the FASTQ file.  The quality score could be a number, but it could be a letter or a symbol.  Significantly, each of these characters can be converted to a numerical value. (This indirectly makes use of ASCII encoding, native to computers, in which every character has a numerical value.) Below lists the possible characters (which begin with an ! which corresponds to a score of 0, reaching a maximum score of 40 with the letter I).

    Character: !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHI
            |                                       |
    Quality:   0                                       40

So that is how each base call is assigned a quality score, but what is the meaning of a score of 0 as opposed to, say, a score of 40?  Well, the higher the score the better the quality.  Technically, quality scores are defined by the following equation:

Quality = -10 log_10⁡〖p/(1-p)〗
In which p is the probability the base call is incorrect.

FASTQ files are typically processed by aligners which use the base call and the alignment scores to map reads to a reference genome.

#### SAM / BAM
Sequence aligners that map FASTQ files to a reference genome typically produce output in SAM (Sequence Alignment / Map) format, or a bespoke compressed version of this known as BAM format.  SAM format files should end with the extension .sam, but under-the-hood they are actually regular text files.  BAM files need to be read with an application named samtools and end with the suffix .bam.

The SAM format contains much information relating to how a read was aligned to a reference genome, but we shall not cover this in depth here (but if you are interested in learning more, the canonical SAM format specification is described at: https://samtools.github.io/hts-specs/SAMv1.pdf ).

In brief, SAM format has two parts:

Firstly, at the top of a file, there are header lines that describe the reference genome and how the FASTQ reads were aligned.

    @HD	VN:1.6	SO:coordinate
    @SQ	SN:1	LN:248956422
    @SQ	SN:10	LN:133797422
    @SQ	SN:11	LN:135086622
    .
    .
    .

The rest of the file comprises lines describing every alignment (and sometimes non-alignments as well).   In the example below, the chromosome and genomic position of the alignment are shown in bold.  Notice the sequence and quality score information from the original FASTQ file is also retained in the SAM format alignment. 

    ERR1594715.1	419	1	11669	1	75M	=	1
    1883	289	CAGGTGAAGCCCTGGAGATTCTTATTAGTGATTTGGGCTGGGGCCTGGC
    CATGTGTATTTTTTTAAATTTCCACT	//BBBFFFFFFFFFFFF/FFFFFFFFFFFF/FF
    FFFFFFFFFFFFFFFFF<FFFFFFFFFFFFFFFFFFFFFFFF	MD:Z:75	PG:Z:Mark
    Duplicates	RG:Z:ERX1665301_ERR1594715	NH:i:4	HI:i:3	N
    M:i:0	AS:i:148

    These BAM files are often sorted and indexed to speed up access to the data.  BAM files mark a starting point for a range of computational analyses.

#### Data Repositories
Most journals now require the original FASTQ files from a sequencing experiment to be submitted to a public data repository (such as Gene Expression Omnibus https://www.ncbi.nlm.nih.gov/geo/).  Submitted data can be kept private here and only released once the relevant paper is published.  These data resources allow researchers across the world to download and subsequently analyse the results generated in other labs, and possibly make new discoveries without the need for further experiments.  Having said that, retrieving data from these repositories is not always transparent, but advice on how to do this is given later in this course.

<b>WARNING!  Sequencing facilities tend not to retain their data for more than a few weeks, so make sure you download your sequencing data promptly and store in a secure, clearly labelled and backed-up location.  Also, make sure the file transfer was successful by using a tool such as md5sum and checking file sizes before and after transfer are identical.  Remember, NO SUBMITTED FASTQ FILE, NO PUBLICATION.</>