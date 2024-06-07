import requests, json, os

def isPrime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
counter = 1

numposts = input('Ingrese el número de Posts a crear, entre 1 y 100: ')

if not numposts.isdigit() or int(numposts) < 1 or int(numposts) > 100:
    numposts = input('problema con su numero ingresado, ingrese un numero entre 1 y 100: ')

response = requests.get(f"https://jsonplaceholder.typicode.com/posts?_limit={numposts}")
posts = response.json()

primes_dict = {}
no_primes_dict = {}

for post in posts:
    if isPrime(post["id"]):
        primes_dict[post["id"]] = post
    else:
        no_primes_dict[post["id"]] = post

if not os.path.exists("Downloads"):
    os.makedirs("Downloads")

with open(f"Downloads/dl{counter}Primes.json", "w") as file:
    json.dump(primes_dict, file)

with open(f"Downloads/dl{counter}NotPrimes.json", "w") as file:
    json.dump(no_primes_dict, file)