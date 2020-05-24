import requests
from lxml import html
base_url = "http://34.245.197.221"


#Login call for setting the seesion
s = requests.Session()
response = s.get(base_url+'/login')

#getting token for login
tree = html.fromstring(response.content)
token = tree.xpath('//*[@id="login_form2"]/input/@value')

#Login the user
res1 = s.post(base_url+'/login', json={"_token": token[0], "username": "hit1", "password": "hiten12345"})
print(res1.status_code)

#Getting token for logout
tree = html.fromstring(res1.content)
token = tree.xpath('//*[@id="logout-form"]/input/@value')

#logout user using token
res2 = s.post(base_url+'/logout', data={"_token": token[0]})
print(res2.status_code)
