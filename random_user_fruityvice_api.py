from randomuser import RandomUser
import pandas as pd
import requests
import json

# r = RandomUser()
# some_list = r.generate_users(100)
# name = r.get_first_name()

# for user in some_list:
#     print(user.get_full_name(),"",user.get_email())
#     print(user.get_picture())

# def get_users():
#     users =[]
#     for user in RandomUser.generate_users(100):
#         users.append({
#             "Name":user.get_full_name(),
#             "Gender":user.get_gender(),
#             "City":user.get_city(),
#             "Country":user.get_country()
#         })
#     return pd.DataFrame(users)
# print(get_users())

url = "https://web.archive.org/web/20240929211114/https://fruityvice.com/api/fruit/all"

r = requests.get(url)
results = json.loads(r.text)
df = pd.DataFrame(results)
df2 = pd.json_normalize(results)

