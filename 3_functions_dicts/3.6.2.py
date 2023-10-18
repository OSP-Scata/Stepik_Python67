import requests

with open('dataset_3378_3.txt', 'r') as f1:
    url = f1.readline().strip()

folder = 'https://stepic.org/media/attachments/course67/3.6.3/'
text = ''

while text[:2] != 'We':
    r = requests.get(url)
    text = r.text
    url = folder + text
    print(text)
    
print('Thats all. Check "output/step03.text')

with open('step03.txt', 'w') as f2:
    f2.write(text)