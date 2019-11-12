from bs4 import BeautifulSoup
import re           # 정규 표현식 관련 library

html = """
<ul>
    <li><a href="hoge.html">hoge</a>
    <li><a href="https://example.com/fuga">fuga*</a>
    <li><a href="https://example.com/foo">foo*</a>
    <li><a href="http://example.com/aaa">aaa</a>
</ul>
"""

soup = BeautifulSoup(html, "html.parser")

# 정규식 표현으로 href에서 https 인 것 추출하기
li = soup.find_all(href=re.compile(r"^https://"))

for e in li:
    print(e.attrs['href'])