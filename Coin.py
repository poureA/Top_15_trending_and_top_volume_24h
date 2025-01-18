from requests import get
from pandas import DataFrame
from os import system

class Coins_and_Trending(object):
    '''Class Docstring'''

    def coinmarketcap_process(self,Max_rows):
        '''Function Docstring'''
        API_key = 'xxxx' # Your API key here
        url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
        df = list()
        parameters = {'start':'1','limit':'5000','convert':'USD'}
        headers = {'Accepts': 'application/json','X-CMC_PRO_API_KEY': API_key}
        response = get(url, headers=headers, params=parameters)
        if response.status_code==200:
            result = response.json()
            for i in result['data']:
                df.append([i['name'],i['quote']['USD']['volume_24h']])
            df = DataFrame(df,columns=['Name','Volume 24h'])
            df = df.sort_values(by='Volume 24h',ascending=False)
            return df.head(Max_rows)
        else : return response.status_code

    def coingecko_process(self):
        '''Function Docstring'''
        url_t = "https://api.coingecko.com/api/v3/search/trending"
        API_key_t = 'xxxx' # Your API key here
        trending_tokens = list()
        headers_t = {"accept": "application/json",'x-cg-demo-api-key':API_key_t}
        result_t = get(url_t,headers=headers_t)
        if result_t.status_code == 200:
            response_t = result_t.json()
            for i in response_t['coins']:
                val = i['item']['name']
                trending_tokens.append(val)
            trending_tokens = DataFrame(trending_tokens,columns=['Top 15 trending tokens'])
            return trending_tokens 
        else : return result_t.status_code

    def Run(self)->None:
        '''Function Docstring'''
        while ask:=input('For info please enter number of top rows that you want to get:'):
            try:
                ask = int(ask)
                system('cls')
                print('Please wait while working on your request...')
                coinmarketcap_data = self.coinmarketcap_process(ask)
                coingecko_data = self.coingecko_process()
                if type(coinmarketcap_data) != int and type(coingecko_data) != int:
                    system('cls')
                    print(coinmarketcap_data,'\n'*3,'-'*50,'\n'*3,coingecko_data,f'\n{"-"*50}')
                else:
                    system('cls')
                    print(f'Something went wrong when scraping data from the website please try again!')
                    if type(coinmarketcap_data) == int and type(coingecko_data) == int:
                        print(f'Status code from coinmarketcap: {coinmarketcap_data}\nStatus code from coingecko: {coingecko_data}')
                    elif type(coinmarketcap_data) == int:
                        print(f'Status code from coinmarketcap: {coinmarketcap_data}')
                    else: 
                        print(f'Status code from coingecko: {coingecko_data}')
            except: 
                system('cls')
                print(f'Please enter an integer value. "{ask}" is not a valid input!')

info = Coins_and_Trending()
if __name__=='__main__':
    info.Run()