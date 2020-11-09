# Scrape the market value of a bond/stock/ETF

This is an example - absolutely basic - how to scrape some information of a website, for example the value of a bond.

What to do:

0. In the code you have to replace:
   EXAMPLE1 = placeholder for the name of the bond, you want to search, for example the Vanguard FTSE All-World UCITS ETF 'A1JX52'  
   EXAMPLE2 = placeholder for the website, on which the value of the bond is available..e.g. website of a bank'  
   EXAMPLE3 = placeholder for the id which refer to the value of the bond, e.g. 'u_385016294', you can find it in the source code of the website  

1. Run the file

2. Use the class bond:
   e.g. type in the command window: 	
   ETF1=bond()  
   ETF1.search('A1JX52')  
	
3. You'll get the value of the ETF A1JX52 as the output.	

note: There are many different ways, to extract information of a website. In this code is used the fact that the value we want to get has an id in the source code of the website.

