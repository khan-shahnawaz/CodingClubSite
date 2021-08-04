import requests
def authenticate(cfid):
    response=requests.get("https://codeforces.com/api/user.info?handles="+cfid)
    response_dict=response.json()
    if response_dict['status']=='FAILED':
        return False
    else:
        return True
def get_rating(cfid):
    response=requests.get("https://codeforces.com/api/user.info?handles="+cfid)
    response_dict=response.json()
    try:
        return response_dict['result'][0]['rating']
    except:
        return 0