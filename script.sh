wget -O - http://www.eoddata.com/stockquote/NYSE/FIT.htm > now.html
java -jar tagsoup-1.2.1.jar --files now.html