# script-languages

University Based course on Python Programming

List of topics covered during classes

1. Regex and JSON
2. Web Scraping
3. Image Processing
4. Sending E-Mails
5. GUI programming
6. Interacting with databases
7. Interacting with CSV and docs file
8. Data visualisation and Exploration
9. Pytest Framework

import datetime
today = datetime.date.today()
first = today.replace(day=1)
lastMonth = first - datetime.timedelta(days=1)
print(lastMonth.strftime("%Y.%m"))




------ Download Picture function

def downloadPic():
    picLink = "https://upload.wikimedia.org/wikipedia/commons/b/b5/Warsaw_rice_mn_sign.JPG"
    response = requests.get(picLink)
    file = open("boardsign.jpg", "wb")
    file.write(response.content)
    file.close()
