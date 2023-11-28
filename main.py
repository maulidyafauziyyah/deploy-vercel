from fastapi import FastAPI, HTTPException, Request
# import pandas as pd

# panggil class FastAPI
app = FastAPI()

# read file csv
# data = pd.read_csv('data.csv')

# key untuk akses endpoint
key = "secret123"

# define url/endpoint
@app.get('/')
def handler():
    return {'message': 'voila'}

@app.get('/secret')
def handler(request: Request):
    # retrieve headers content from request
    headers = request.headers

    #retrieve User-Agent key in headers
    agent = headers.get("User-Agent")

    token = headers.get('Token')


    if token == None:  # jika key token tidak ada dalam header
        return {
            'message': 'belum login',
        }
    else: # jika ada key Token
        if token!= key:
            raise HTTPException(status_code=500, detail='Key Tidak Sesuai')
        else:
            return {
                'message': 'Main Page',
                'agent': agent
                }

# # merubah data csv menjadi dict/json
# @app.get('/data')
# def handler():
#     return data.to_dict(orient='records') # orientnya udah pasti records

@app.get('/home/{user}')
def handler(user):
    if user == 'maudy':
        return {
            'message': 'Welcome Home',
            'user': user
        }
    else:
        # handle error: gunanya agar jika banyak org yg akses sistemnya ga down
        raise HTTPException(status_code=400, detail='not found')
    