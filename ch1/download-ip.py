# API for check IP information
# library module.
import urllib.request

# read the data
url = "http://api.aoikujira.com/ip/ini"
res = urllib.request.urlopen(url)
data = res.read()


# change binary to text
text = data.decode("utf-8")
print (text)