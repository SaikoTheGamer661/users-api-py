import requests

URL = "http://localhost:5000"

# registrar usuarios
usuarios = [{"usuario":"juan","password":"1234"},
            {"usuario":"maria","password":"abcd"}]

for u in usuarios:
    r = requests.post(f"{URL}/register", json=u)
    print(r.json())

# login correcto
r = requests.post(f"{URL}/login", json={"usuario":"juan","password":"1234"})
print("Login juan:", r.json())

# login incorrecto
r = requests.post(f"{URL}/login", json={"usuario":"juan","password":"9999"})
print("Login juan mal:", r.json())
