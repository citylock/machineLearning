# Library
import urllib.request

# url and savename
url = "http://uta.pw/shodou/img/28/214.png"
savename = "test.png"

# Download
urllib.request.urlretrieve(url, savename)
print( "저장되었습니다. ")
