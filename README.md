# OpTC Data Analysis Challenge

Included in this repository is a sample set of data from the
[OpTC Data Release](https://github.com/FiveDirections/OpTC-data). The data
in `data.json` is a small snippet of host-based eCAR data.

## Objectives

Answer the following questions based on the data provided in `data.json`:
1. How many unique `"action"` values are there?
2. List the number of occurrences of each `"action"` value in the sample data.
3. Give a breakdown on how many `"src_ip"`s are IPv4 vs IPv6. (Hint: you may
   need to also keep track of cases where this does not apply for cases of
   missing or invalid data)
4. How many records are there with the `"dest_ip"` in the 224.0.0.0/8 subnet.

Answers should be printed to standard output when running your solution program.
Be sure each question response is clearly labeled.

## Submission

Fork this repository for your own work, and submit a GitHub Pull Request (PR)
to this repository containing your solution.
The solution PR should consist of the following:

1. Source code containing the solution
2. A build/install script, if necessary, to install dependencies, compile,
   or package the solution. Give instructions in this `README.md` file
   to include installation steps (even if it is just the execution of a
   provided script).
3. Additional documentation, included in the "Execution" section of this
   `README.md` file, to specify exactly how the solution should be
   executed. For the instructions, assume your starting location is the root
   directory of this repository.

## Solution

Solution was a combination of utilizing python's builtin modules of regex, collections.Counter, and ipaddress to perform the tasks at hand.

### Installation

Installation is easy, simply make sure that you have python3 installed and it's version is 3.7 or higher
`sudo apt install python3`

for other non Debian based systems go to the site[https://www.python.org/downloads/] for installation instructions

Navigate to the base directory for this repo (ecar-challenge).
Make sure that you have execute permission on data_analysis.py.
To check run `ls -latr`
if not run `chmod +x data_analysis.py`

### Execution

Simply run `./data_analysis.py` or `python3 data_analysis.py` to obtain the solution


