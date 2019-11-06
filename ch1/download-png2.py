import urllib.request

# url and savename
url = "http://uta.pw/shodou/img/28/214.png"
savename = "test2.png"

# download image
mem = urllib.request.urlopen(url).read()

# save image as a file
with open(savename, mode="wb") as f:
    f.write(mem)
    print("저장되었습니다. !!!")
