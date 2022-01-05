# Custom_Wordlist
This repo is about steps to take in order to create a effective custom wordlist in a few clicks. this comes handing in pentesting engagement where you need to do brute force attacks, so the main probleme is when you use a random wordlist that contain passwords that don't match your client password policy, so you have 0 chance to get that valide account. 
Well to build this effective custom wordlist: 
### Create rich text file
we start with some OSINT to gather commun words used by the client such as : company name, company's services, ... then save this in a file.txt 
### Tamper with the wordlist  
start thempering with it (add 2020 at the end, change a with @, and so on) . for i in $(cat words.txt);do echo $i; echo ${i}2020; echo ${i}2021; echo ${i}2022;done > words2.txt Now use hashcat rules to temper further hashcat --force words2.txt -r /usr/share/hashcat/rules/best64.rule -r /usr/share/hashcat/rules/toggles5.rule --stdout > wordlistfinal.txt 
you cloud also create your own rules, it's pretty fun. 
### Filter result 
Now that you have created a custom wordlist, you need to remove all passwords that don't match your client password policy (mostly Microsoft default password complexity) for that i create this small python script which do just that for you. 
./filter.py test1.txt -c
