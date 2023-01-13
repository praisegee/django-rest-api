# import requests

# response = requests.get('http://127.0.0.1:8000/')

# # print(dir(response))
# print(response.json())

def add(x, y, *args, **kwargs):
    name = kwargs['name']
    num = args[0]
    print("Name: ", name)
    print("Num: ", num)
    # try:
    #     name = kwargs['name']
    #     print("Name: ", name)
    # except KeyError:
    #     pass
    print("TMP: ", args)
    print("KWA: ", kwargs)
    return x + y

print(add(3, 6, 7, 8, name="Kay", b=12))