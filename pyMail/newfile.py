import bs4
import requests


def handle_task_three():
    url = "https://wiz.pwr.edu.pl/pracownicy?letter=d"
    page = requests.get(url)
    page.raise_for_status()
    content = bs4.BeautifulSoup(page.text, 'html.parser')
    repr(content)

    print("The list of researchers - ")
    div_list = content.select('div .news-box')
    if len(div_list) == 0:
        print("There are no researchers on PWR with such last name!")
        return
    for element in div_list:
        par = element.select('a')
        par2 = element.select('p')
        print(par[0].contents[0], par2[0].contents[0])


def run():
    handle_task_three()


if __name__ == "__main__":
    run()
