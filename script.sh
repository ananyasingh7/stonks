echo "Please enter the stock symbol: "
read symbol
wget -O - http://www.eoddata.com/stockquote/NASDAQ/$symbol.htm > now.html
java -jar tagsoup-1.2.1.jar --files now.html
python3 scraper.py now.xhtml