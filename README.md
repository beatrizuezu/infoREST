# infoREST

## Procedimentos
### Clone o repositório

```console
git clone git@github.com:beatrizuezu/infoREST.git infoREST
cd infoREST
```

### Crie um virtualenv com Python 3.5 e ative
```console
virtualenv .env -p python3
source .env/bin/activate
```
### Instale as dependencias
```console
pip install -r requirements.txt
```

### Criar o banco de dados
```console
./manage.py migrate
```
## Rodar o servidor
```console
 ./manage.py runserver
 ```

 ## CURL

 ### POST
 ```console
 curl -X POST -F fb_id=562073097 -u admin:password123 http://127.0.0.1:8000/UserFb/
  ```

 ### GET
 ```console
 curl -X GET -F fb_id=562073097 -u admin:password123 http://127.0.0.1:8000/UserFb/
  ```
