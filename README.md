# pyPBS_EL

## Table of Contents
  * [Installation](#installation)
  * [Quick start](#quick-start)
  * [Instruction](#instruction)
  * [Features](#features)
  
## Installation

Download using pip via pypi.

```bash
$ pip install pyPBS_EL
```
(Mac/homebrew users may need to use ``pip3``)

## Quick start example

When using pyPBS_EL in RaxML, Please reference following command.

```
$ pyPBS_EL -P "/home/<usrdir>/*.phy" -c "raxml-ng --threads 32 --model JTT --msa (base)"
```

## Instruction

This tool was devised for 'Generate bash script for PBS command and excute it' in 'just one command line'.

The options are classified into two categories, required and optional.

```
$ pyPBS_EL -P -c -m -p -M -o

<Required arguments>
'-P', '--path' : Path of input file(s)
'-c', '--command' : Command line

<Optional arguments>
'-t', '--thread' : Number of thread (ppn)
'-m', '--memory' : Memory for process (gb)
'-p', '--prefix' : Prefix of the output file
'-w', '--walltime' : Time set for usage
'-o', '--outdir' : Output dir name
```

That is all.

Additional using case are shown below.


### Case 1. multiple input files (multiple file names in -P option)
```
$ pyPBS_EL -P /PATH/test1.phy /PATH/test2.phy -c "raxml-ng --threads 32 --model JTT --msa (base)"
```
This command line will create bash scripts for both '/PATH/test1.phy' and '/PATH/test2.phy'. Then two processes of 'raxml-ng' command will be submitted to the server.


### Case 2. multiple input files (regular expression)
```
$ pyPBS_EL -P "/PATH/*.phy" -c "raxml-ng --threads 32 --model JTT --msa (base)"
```
This command line will create bash scripts for all '/PATH/\*.phy' file format. Then the number of \*.phy processes of 'raxml-ng' command will be submitted to the server.

### Case 3. set walltime and thread for user
```
$ pyPBS_EL -P "/PATH/*.phy" -c "raxml-ng --threads 32 --model JTT --msa (base)" -w "64:00:00 -t 32"
```
This command line will create bash scripts for all '/PATH/\*.phy' file format. Then the number of \*.phy processes of 'raxml-ng' command will be submitted to the server with user-set walltime and thread option (64h, 32threads).

### Case 4. Create output file in another path
```
$ pyPBS_EL -P "/PATH/*.phy" -c "raxml-ng --threads 32 --model JTT --msa (base) -o (dir)" -o /Different/PATH/
```
This command will create output file in another path. For example,

Input file path : /PATH/\*.phy
Output file path : /Different/PATH/raxml.out

### Case 5. Set the conda environment
```
$ pyPBS_EL -P "/PATH/*.phy" -c "raxml-ng --threads 32 --model JTT --msa (base) -o (dir)" -e /home/msjeon27/works/anaconda3/envs/RaxML
```
or
```
$ pyPBS_EL -P "/PATH/*.phy" -c "raxml-ng --threads 32 --model JTT --msa (base) -o (dir)" -e ~/works/anaconda3/envs/RaxML
```
This command will submit the process to proceed in your conda environment. In this case, you should set your conda path.


## Features
  * Python script to generate PBS command lines by python code
