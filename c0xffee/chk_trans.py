import requests
from bs4 import BeautifulSoup


def beauti4(res):
    soup = BeautifulSoup(res.text, 'html.parser')

    rand_addr = soup.find('a', class_="hash", href=True)['href'].split('/')[-1]
    print(rand_addr)
    data = soup.find_all('span', class_="wb-ba", text=True)
    received_bch = float(data[0].text)
    tx_ago = data[4].text
    tx_date = data[5].text
    tx_gas = float(data[2].text)
    sent_bch = received_bch + tx_gas
    sent_bch = round(sent_bch, 10))
    '''
    print(received_bch)
    print(tx_ago)
    print(tx_date)
    print(tx_gas)
    print(sent_bch)
    '''
    
    #print(money)
    #title = soup.find('h1', class_='entry-title').text

    return rand_addr, sent_bch, received_bch, tx_gas, tx_ago, tx_date


def chk_tx(url, temp_addr, send_bch):
    res = requests.get(url)
    rand_addr, sent_bch, received_bch, tx_gas, tx_ago, tx_date = beauti4(res)
    failed = 0
    if 'seconds' not in tx_ago:
        failed = 1
    if temp_addr != rand_addr:
        failed = 1
    if sent_bch != send_bch:
        if abs(send_bch - sent_bch) > sent_bch/100:
            failed = 1
            
    return failed, sent_bch
    
    
    
    
      
    
    #print(len(money))

'''
url = "https://blockchair.com/bitcoin-cash/transaction/542efdb29882888dc7b1c6dd9bc2573ab4eb509e4f97930c10894a7f31e1dff1?from=bitcoin.com"
url = input()
chk_tx(url, '123')
'''