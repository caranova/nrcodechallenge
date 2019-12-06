# Code challenge
1. Build the docker container image `docker build -t codechallenge https://github.com/caranova/nrcodechallenge.git`

2. Run with `docker run -i codechallenge --file filename.txt` or `cat file1 file2 | docker run -i codechallenge --file -`

## Example of syntax:
 `cat file4 file5.txt | docker run -i codechallenge --file file1 file2.txt file3 -`

 ## Known issues
* can't pipe `cat` (maybe others?) without explicit `-` parameter after `--file` flag
* known compatibility issues on cmd and PowerShell 