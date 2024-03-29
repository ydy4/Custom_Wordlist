
# Custom Wordlist
In brute force attacks, you need to create a effective wordlist, one that is adapted to your target in termes of **used words** and **password complexity requirements**
This python script help to filter out of scope password in termes complexity.
the necessary steps to make a wordlsit are :
- create rich text file 
- tamper with the words
- replace with special chars
- filter out the result
## Create rich text file
we start with some OSINT to gather commun words used by the client such as : company name, company's services, ... then save this in a file.txt 
## Tamper with the wordlist  
start tampering with it (add **2020 - 2021 - 2022** at the end) . 
```bash 
for i in $(cat words.txt);do echo $i; echo ${i}2020; echo ${i}2021; echo ${i}2022;done > words2.txt 
```
Now use hashcat rules to tamper further 
```bash
hashcat --force words2.txt -r /usr/share/hashcat/rules/best64.rule -r /usr/share/hashcat/rules/toggles5.rule --stdout > wordlistfinal.txt 
```
you cloud also create your own rules, here is a simple rule file to add special chars at the end 

![image](https://user-images.githubusercontent.com/95150458/150603010-bd32f461-0be3-41f7-99a9-5f719d510586.png)

using this rule 

![image](https://user-images.githubusercontent.com/95150458/150603051-68f7412c-2895-43cd-82e1-b698b62f65c7.png)
## Replace
We replace **o** with **0** and **a** with **@**
so that words like **Password** become like this **P@ssw0rd**
```bash
# Read in the file
ourfile = input( "file name> " )
with open(ourfile, 'r') as file :
  filedata = file.read()

# Replace the target string
filedata = filedata.replace('o', '0').replace('a', '@')

# Write the file out again
with open(ourfile, 'w') as file:
  file.write(filedata)
```

![image](https://user-images.githubusercontent.com/95150458/150602669-d5398e30-0def-49b1-949a-76d07b56bd50.png)

## Filter result 
Now that you have created a custom wordlist, you need to remove all passwords that don't match your client password policy (mostly Microsoft default password complexity) for that i create this small python script which do just that for you. 
```bash
python3 filter.py -h                                                                                                                        1 ⚙

 ____    _  _____  _                    _            _   
|  _ \  / \|_   _|/ \   _ __  _ __ ___ | |_ ___  ___| |_ 
| | | |/ _ \ | | / _ \ | '_ \| '__/ _ \| __/ _ \/ __| __|
| |_| / ___ \| |/ ___ \| |_) | | | (_) | ||  __/ (__| |_ 
|____/_/   \_\_/_/   \_\ .__/|_|  \___/ \__\___|\___|\__|
                       |_|                               

usage: filter.py [-h] [-c] [-m MIN_LENGTH] [--max-length MAX_LENGTH] [-w WORD [WORD ...]] [-s] [-t TOP] file [file ...]

positional arguments:
  file                  Wordlist file

optional arguments:
  -h, --help            show this help message and exit
  -c, --complexity      Filter with Microsoft complexity filter (does not affect minimum length)
  -m MIN_LENGTH, --min-length MIN_LENGTH
                        Minimum length
  --max-length MAX_LENGTH
                        Maximum length
  -w WORD [WORD ...], --word WORD [WORD ...]
                        Wordlist on command line
  -s, --sort            Sort unique
```
