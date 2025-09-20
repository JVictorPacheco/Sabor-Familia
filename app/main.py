from fastapi import FastAPI


app = FastAPI()


@app.get('/')
def teste_api():
    return {"Mensagem": "Mensagem de teste"}