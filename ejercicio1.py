import requests

param1= "1"
param2= "2"
url = "https://ammtp.pythonanywhere.com/testapp/post_example"

parametros = {
    "param1": param1,
    "param2": param2,

}
data="123"

response = requests.get(url, params=parametros, data=data)

valor1 = response.json()['request']['params']['param1']
valor2 = response.json()['request']['params']['param2']
valor3 = response.json()['request']['body']

response = requests.get(url)
assert valor1 == param1
assert valor2 == param2
assert valor3 == data
#valor = response.json()['request']['path']



#assert (valor == "/testapp/get_example")