# 2fa-datacollector
<p>Collect random numbers that will be made by 2FA's you can give it a secret key and also determine how long it can work and collect It's raw idea I'm working on it then I can write a program that predict 2FA cods faster .</p>

<h3>Requirement</h3>
<ul>
  <li> based on python3 so you need to install python3 </li>
  <li> then install pyotp module by running this command on linux : </li>
<p><code style="display:block">pip3 install pyotp</code></p>
  <p>in windows machine :</p>
  <p><code>pip install pyotp</code>
</ul>
<h3>Usage instruction:</h3>

<p>It accepts up to 4 switches :</p>
<p>the ORDER of SWITCHES is important!!!!</p>
<p>&nbsp;Without applying the first switch next number means second but you can use m for Minute and h for Hour so the next parameter it must be a number.
third parameter if you use m or h switch or the second parameter if you don't use any previous switch stand for the secret key and the last parameter is the output file name also it has an output on the terminal. by default the output file name "totp.txt" .</p>

<h3>example:</h3>

<p>In Linux:</p>
<p><code>python3 2fa.py m 1 JBSWY3DPEHPK3PXP log.txt </code></p>
<p>In windows:</p>
<p><code>python 2fa.py m 1 JBSWY3DPEHPK3PXP log.txt</code></p> 

<p>The m stand for minute and the 1 means one minute the next parametr is the secret key and the last is the file name. </p>

In Linux:
<p><code>python3 2fa.py 60 JBSWY3DPEHPK3PXP log.txt </code></p>

In Windows:
<p><code>python 2fa.py 60 JBSWY3DPEHPK3PXP log.txt</code></p>

<p>In this eample 60 means sixty seconds .</p>

<p>Windows:</p>
<p><code>python 2fa.py h 1 JBSWY3DPEHPK3PXP log.txt</code></p>

linux:
<p><code>python3 2fa.py h 1 JBSWY3DPEHPK3PXP log.txt</code></p>

<p>The h means Hour and the 1 stand for one-hour working.</p>

<div><h5>NOTE : </h5>"JBSWY3DPEHPK3PXP" is the test key from : </div>

<a href="https://github.com/pyauth/pyotp" target="_blank">https://github.com/pyauth/pyotp</a>

<h2>Output description:</h2>

<p>sample output after 1-minute work :</p>
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

<p>The "Inputs" means total input or total number that received. </p>
<p>"count" means the iteration time.</p>
<p>"All Digits" mean total number in all places Digit1 to Digit 6. 
then "Digit1" means in the place of the first digit that numbers with that count iterated, and also for other digits.</p>



