# 2fa-datacollector
collect random numbers that will be made by 2FA's you can give it a secret key and also determine how long it can work and collect It's raw idea I'm working on it then I can write a program that predict 2FA cods faster .

Requirement

--- based on python3 so you need to install python3 
--- then install pyotp module by running this command on linux :
pip3 install pyotp
in windows machine :
pip install pyotp

Usage instruction:

It accepts up to 4 switches :
the ORDER of SWITCHES is important!!!!
without applying the first switch next number means second but you can use m for Minute and h for Hour so the next parameter it must be a number.
third parameter if you use m or h switch or the second parameter if you don't use any previous switch stand for the secret key and the last parameter is the output file name also it has an output on the terminal. by default the output file name "totp.txt" .

example:

In Linux:
python3 2fa.py m 1 JBSWY3DPEHPK3PXP log.txt 
in windows:
python 2fa.py m 1 JBSWY3DPEHPK3PXP log.txt 

the m stand for minute and the 1 means one minute the next parametr is the secret key and the last is the file name. 

In Linux:
python3 2fa.py 60 JBSWY3DPEHPK3PXP log.txt 

In Windows:
python 2fa.py 60 JBSWY3DPEHPK3PXP log.txt

In this eample 60 means sixty seconds .

Windows:
python 2fa.py h 1 JBSWY3DPEHPK3PXP log.txt

linux:
python3 2fa.py h 1 JBSWY3DPEHPK3PXP log.txt

the h means Hour and the 1 stand for one-hour working.

NOTE : "JBSWY3DPEHPK3PXP" is the test key from : 

<a href="https://github.com/pyauth/pyotp" target="_blank">https://github.com/pyauth/pyotp</a>

<h1>Output description:<h1>

sample output after 1-minute work :
<pre>
total
Inputs:	2
------------------------------------------------------------------------------------------
count:1	 number:174071
count:1	 number:567867
All DigitS
------------------------------------------------------------------------------------------
count:4	 number:7
count:2	 number:1
count:2	 number:6
count:1	 number:4
count:1	 number:0
count:1	 number:5
count:1	 number:8
Digit	1
------------------------------------------------------------------------------------------
count:1	 number:1
count:1	 number:5
Digit	2
------------------------------------------------------------------------------------------
count:1	 number:7
count:1	 number:6
Digit	3
------------------------------------------------------------------------------------------
count:1	 number:4
count:1	 number:7
Digit	4
------------------------------------------------------------------------------------------
count:1	 number:0
count:1	 number:8
Digit	5
------------------------------------------------------------------------------------------
count:1	 number:7
count:1	 number:6
Digit	6
------------------------------------------------------------------------------------------
count:1	 number:1
count:1	 number:7
</pre>

The "Inputs" means total input or total number that received. 
"count" means the iteration time.
"All Digits" mean total number in all places Digit1 to Digit 6. 
then "Digit1" means in the place of the first digit that numbers with that count iterated, and also for other digits.



