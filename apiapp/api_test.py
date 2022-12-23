# import requests
# import json

# url = "https://justforpay.in/production/testapi/dmt_reqeust"

# payload = json.dumps({
#   "api_key": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiMTAwOTE5MCIsInVzZXJfbW9iIjoiOTg3NjU0MzIxMCIsIm9yZGVyX2lkIjoiMTY3MTYzMzQ0NTU4MjQifQ.3xHs3C7VHPzflxJR5VsY6fHGBEgJAJhFNYalgqK-Q-U",
#   "action": "add_beneficiary",
#   "name": "SONU KUMAR MISHRA",
#   "bank_account": "919599103826",
#   "mobile_no": "9599103826",
#   "channel": "NEFT",
#   "ifsc_code": "PYTM0123456",
#   "modbile": "9876543210",
#   "Orderd": "12358774587",
#   "address": "new delhi",
#   "email": "mishrasonu9211@gmail.com",
#   "state": "haryana",
#   "city": "Faridabad",
#   "pincode": "121009",
#   "bank_name": "Paytm payment bank"
# })
# headers = {
#   'Content-Type': 'application/json',
#   'authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiMTAwOTE5MCIsInVzZXJfbW9iIjoiOTg3NjU0MzIxMCIsIm9yZGVyX2lkIjoiMTY3MTYzMzQ0NTU4MjQifQ.3xHs3C7VHPzflxJR5VsY6fHGBEgJAJhFNYalgqK-Q-U'
# }

# response = requests.request("POST", url, headers=headers, data=payload)

# print(response.text)



import requests
import json

url = "https://api.covid19api.com/countries"

payload = json.dumps({
  "Country": "sanfransisco",
  "Slug": "fnon",
  "ISO2": "SO"
})
headers = {
  'Content-Type': 'application/json',
  'authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiMTAwOTE5MCIsInVzZXJfbW9iIjoiOTg3NjU0MzIxMCIsIm9yZGVyX2lkIjoiMTY3MTYzMzQ0NTU4MjQifQ.3xHs3C7VHPzflxJR5VsY6fHGBEgJAJhFNYalgqK-Q-U'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)