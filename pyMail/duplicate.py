import requests


def cat_facts(num):
    r = requests.get(f'https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount={num}')
    response = r.json()
    p_cat_facts = response["text"]
    print(p_cat_facts)


def run():
    cat_facts(num=input("Enter 1 only, After each run it will show different cat fact : "))


if __name__ == "__main__":
    run()
