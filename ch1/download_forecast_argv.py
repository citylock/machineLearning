# library
import sys
import urllib.request as req
import urllib.parse as parse

# command with parameters - read parameters
if len(sys.argv) <= 1 :
    print ("USAGE: download-forecast-argv <Region Number>")
    sys.exit()
regionNumber = sys.argv[1]

api = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
values = {
    'stnId' : regionNumber
}

params = parse.urlencode(values)
url = api + "?" + params
print ("url=", url)

# download
data = req.urlopen(url).read()
text = data.decode("utf-8")

print(text)