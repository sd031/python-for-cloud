# python3 -m pip install requests
# if install using pip requirements.txt: pip install -r requirements.txt

#get request
import requests
x = requests.get('https://httpbin.org/get')
print(x.text)

#head request
# import requests
# x = requests.head('https://httpbin.org/head')
# print(x.headers)

#post request
# import requests
# url = 'https://httpbin.org/post'
# myobj = {'somekey': 'somevalue'}
# x = requests.post(url, data = myobj)
# print(x.text)

#put request
# import requests
# url = 'https://httpbin.org/put'
# myobj = {'somekey': 'somevalue'}
# x = requests.put(url, data = myobj)
# print(x.text)

#patch request
# import requests
# url = 'https://httpbin.org/patch'
# myobj = {'somekey': 'somevalue'}
# x = requests.patch(url, data = myobj)
# print(x.text)

#delete request
# import requests
# url = 'https://httpbin.org/delete'
# myobj = {'somekey': 'somevalue'}
# x = requests.delete(url, data = myobj)
# print(x.text)

