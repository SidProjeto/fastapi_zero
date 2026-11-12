from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fastapi_zero.schemas import Message, UserSchema

app = FastAPI(title='Api')


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá mundo!'}


@app.get('/html', status_code=HTTPStatus.OK, response_class=HTMLResponse)
def page_html():
    return '''
    <html>
        <head>
            <title>Pagina HTML</title>
        <head>
        <body>
            <h1>Olá Mundo!</h1>
        </body>
    </html>'''


@app.post('/users/')
def create_user(user: UserSchema):
    return user
