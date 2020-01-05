#!/bin/bash

while read SYM
do 
	if [ $1 = $SYM ]
	then
		wget -q -O - http://www.eoddata.com/stockquote/NASDAQ/$1.htm > now.html
		java -jar tagsoup-1.2.1.jar --files now.html 2> errorOutput.log > output.log &
		sleep 2
		python3 scraper.py now.xhtml
		exit 1
	fi
done < symbolList

echo "Sorry, your symbol does not exist within the Exchange List"
