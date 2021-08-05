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
def get_best(profiles):
    if len(profiles)==0:
        return([])
    ids=[]
    for i in profiles:
        ids.append(i.cfid)
    handles=";".join(i for i in ids)
    response=requests.get("https://codeforces.com/api/user.info?handles="+handles)
    best=[]
    for dict in response.json()['result']:
        best.append({"rating":dict['rating'],"id":dict['handle']})
    best.sort(reverse=1,key=lambda x: x['rating'])
    return(best[:5])