wget -O - http://www.eoddata.com/stockquote/NASDAQ/MSFT.htm > now.html
java -jar tagsoup-1.2.1.jar --files now.html
python3 scraper.py now.xhtml