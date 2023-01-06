import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app= FastAPI()

@app.get('/')
def get_list():
    return [2,4,6,865,4]

@app.get('/contact', response_class=HTMLResponse)
def get_lists():
    return """
        <h1>hola mundo</h1>
        <p>hola soy un parrafo</p>
    """


def run():
    store.get_categories()

if __name__=='__main__':
    run()