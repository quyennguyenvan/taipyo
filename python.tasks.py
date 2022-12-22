import requests
import json


def get_result(content, params):
    v = json.loads(content)[f'{params}']
    return v


try:
    billURL = "https://taipy-algorithms.azurewebsites.net/api/HttpTrigger1?Code=jsm60ZCLycr7u25YpL0ywPQqGBR0soXwGhP4dx_HzACRAzFu59gikA=="

    linusURL = "https://taipy-algorithms.azurewebsites.net/api/HttpTrigger2?Code=wbe-sW9v0_bAmF0XFLNfJl_oF5V623ksHwdWr_BgRRI6AzFu-1JF2Q=="

    hitURL = "https://taipy-algorithms.azurewebsites.net/api/HttpTrigger3?Code=sVzxyopyebY2fPv-YJJvmY5IUqB4M6a-2x7iwGH9339SAzFu_Hc5Nw=="

    params = {'number': '1'}
    x1 = requests.get(billURL, params)
    number = get_result(x1.text, 'res')
    print(f"request 1: {number}")

    params2 = {
        'number': number,
        'bill': 3
    }

    x2 = requests.get(linusURL)
    linus = get_result(x2.text, 'res')

    print(f"request 2: {linus}")

    params3 = {
        'linus': 11,
        'bill': 3
    }
    x3 = requests.get(hitURL)
    print(x3)


except Exception as er:
    print(er)
