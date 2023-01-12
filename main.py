from qbClient import AuthClient
import constants as cfg
import requests
from future.moves.urllib.parse import urlencode

auth_client = AuthClient(**cfg.client_secrets)

def getCustomerData(accessToken):
    #making Request
    base_url = 'https://production-quickbooks.api.intuit.com'
    url = '{0}/v3/company/{1}/companyinfo/{1}'.format(base_url, cfg.qBData["realm_id"])
    auth_header = 'Bearer {0}'.format(accessToken)
    headers = {
        'Authorization': auth_header,
        'Accept': 'application/json'
    }
    response = requests.get(url, headers=headers)

    print("Response = ",response)
    print("Response Data = ",response.text)

    print("Success")

def refresh_token():
    response = auth_client.refresh(refresh_token=cfg.refreshToken)
    return response

def getTransactionsData(accessToken):
    #making Request
    #base_url = f'https://production.api.intuit.com/quickbooks/v4/payments/charges/'
    print('your squiggly brackets print this')
    print('{1}')
    base_url = f'https://quickbooks.api.intuit.com/v3/company/{1}/reports/TransactionList?date_macro=This Month-to-date&minorversion=65'
    auth_header = 'Bearer {0}'.format(accessToken)
    data = {
        'Authorization': auth_header
    }
    headers = {
        'Authorization': auth_header,
        'Accept': 'application/json;charset=UTF-8',
        'Content-type': '*/*'
    }

    response = requests.get(base_url, headers=headers)

    print("Response 2 = ",response)
    print("Response Data 2 = ",response.text)

    print("Success")


if __name__ == "__main__":
    # fetchData()
    response = refresh_token()
    #getCustomerData(accessToken = response["access_token"])
    response2 = auth_client.get_user_info(access_token=response["access_token"])
    print(response2.text)
    print("\n\n\n")
    getTransactionsData(accessToken = response["access_token"])
    
    print(getTransactionsData(accessToken = response["access_token"]))
    
    
    
