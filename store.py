import requests

def get_categories():
    r= requests.get('https://api.escuelajs.co/api/v1/categories')
    print(r.status_code)
    print(r.text)
    print(r.content)
    print(type(r.text))
    categori= r.json()
    print(type(categori))

    for catego in categori:
        print(catego['name'])