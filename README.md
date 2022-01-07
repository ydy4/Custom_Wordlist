
## Custom Wordlist
In brute force attacks, you need to create a effective wordlist, one that is adapted to your target in termes of **used words** and **password complexity requirements**
This python script help to filter out of scope password in termes complexity.
the necessary steps to make a wordlsit are :
- create rich text file 
- tamper with the words
- filter out the result
### Create rich text file
we start with some OSINT to gather commun words used by the client such as : company name, company's services, ... then save this in a file.txt 
### Tamper with the wordlist  
start thempering with it (add **2020 - 2021 - 2022** at the end, change **a** with **@**, and so on) . 
```bash 
for i in $(cat words.txt);do echo $i; echo ${i}2020; echo ${i}2021; echo ${i}2022;done > words2.txt 
```
Now use hashcat rules to temper further 
```bash
hashcat --force words2.txt -r /usr/share/hashcat/rules/best64.rule -r /usr/share/hashcat/rules/toggles5.rule --stdout > wordlistfinal.txt 
```
you cloud also create your own rules, it's pretty fun. 
### Filter result 
Now that you have created a custom wordlist, you need to remove all passwords that don't match your client password policy (mostly Microsoft default password complexity) for that i create this small python script which do just that for you. 
```bash
./filter.py -h           
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
  -t TOP, --top TOP     Take the top X words
```
