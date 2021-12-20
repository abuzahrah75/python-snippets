import bs4
import requests
import os.path

getPage = requests.get(
    'https://readmanganato.com/manga-bn978870')  # martial peak

# print("THIS SCRIPTS WILL CHECK MARTIAL PEAK MANGA UPDATE.")
senarai = bs4.BeautifulSoup(getPage.text, 'html.parser')
# foods = senarai.select('.panel-story-chapter-list')
foods = senarai.select('.chapter-name')
# for food in foods:
# print(food.text)
# print(foods)

# print(foods[0].text)
# print(foods[0])
# print(foods[0].href
save_path = 'e:/DEV2021/PYTHON/python_snippets/'
completeName = os.path.join(save_path, "martial_peak.txt")

# check latest chapter compared to saved name
file1 = open(completeName, "r")
last_chapter = file1.read()
file1.close()
if (last_chapter == foods[0].text):
    print('NO CHANGE')
else:
    file1 = open(completeName, "w")
    file1.write(foods[0].text)
    file1.close()
    print(f'New Cahpter Available : {foods[0].text}')


# file1 = open(completeName, "w")
# file1.write(foods[0].text)
# file1.close()
