import urllib.request
import urllib.parse

api = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"

# encoding for parameters
values = {
    'stnId' : '108'
}

params = urllib.parse.urlencode(values)

# request url
url = api + "?" + params
print (url)

# download weather forecast
data = urllib.request.urlopen(url).read()

text = data.decode("utf-8")
print (text)
