import requests
import facebook as fb


def gen_token(app_id, app_secret):
    """Gerando o token."""
    gen = 'client_id={app_id}&client_secret={app_secret}&grant_type=client_credentials'
    token = gen.format(app_id=app_id, app_secret=app_secret)
    return token


def access_token():
    """Obtendo acesso."""
    app_id = '181088029053296'
    app_secret = '4c40975da262042768b10273193e4f30'
    API_URL = 'https://graph.facebook.com/v2.8/oauth/access_token?'

    get_access = API_URL + gen_token(app_id, app_secret)
    return get_access

def get_dados_userFb(fb_id):
    r = requests.get(access_token())
    json = r.json()
    token = json['access_token']
    graph = fb.GraphAPI(access_token=token, version='2.7')
    dados = graph.get_object(fb_id, fields='gender,first_name,last_name')
    return dados

# fb_id = '562073097'
