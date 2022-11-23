import requests
from bs4 import BeautifulSoup
import re

def clean_text(text):
    cleaned_text = re.sub('[a-zA-Z]', '', text)
    cleaned_text = re.sub('[\{\}\[\]\/?.,;:|\)*~`!^\-_+<>@\#$%&\\\=\(\'\"]',
                          '', cleaned_text)
    return cleaned_text

result_title = []
result_time = []

special_char = '\n\t'
for page in range(24):
    url = f"https://ece.cbnu.ac.kr/index.php?mid=ece0602&page={page+1}"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    for content in soup.select('td > a'):
        # print(content.getText('title'))
        result_title.append(content.getText('title').replace('\t\n', ''))

    for content in soup.select('td.time'):
        # print(content.getText('16:24'))
        result_time.append(content.getText('16:24'))


print(result_time)
print(result_title)




