import requests



def stems():
    url = input('Song url: ')
    headers={
        "authority": "api.stemplayer.com",
        "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
        "sec-ch-ua-mobile": "?0",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36",
        "sec-ch-ua-platform": "macOS",
        "content-type": "text/plain;charset=UTF-8",
        "accept": "*/*",
        "origin": "https://www.stemplayer.com",
        "sec-fetch-site": "same-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://www.stemplayer.com/",
        "Content-Length": "98",
        "Host": "api.stemplayer.com",
        "Connection": "keep-alive"

    }

    

    body= {"link":f"{url}","stem_codec":f"wav"}

    cl = str(len(body))
    headers["Content-Length"] = cl

    
    r = requests.post('https://api.stemplayer.com/tracks',headers=headers, json=body)

    if r.status_code >= 200:
        if r.json()['data']['status'] ==  'ready':
            bass = r.json()['data']['stems']['bass']
            drums = r.json()['data']['stems']['drums']
            other = r.json()['data']['stems']['other']
            vocals = r.json()['data']['stems']['vocals']
            return bass, drums, other, vocals
        else:
            while True:
                headers={
                    "authority": "api.stemplayer.com",
                    "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
                    "sec-ch-ua-mobile": "?0",
                    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36",
                    "sec-ch-ua-platform": "macOS",
                    "content-type": "text/plain;charset=UTF-8",
                    "accept": "*/*",
                    "origin": "https://www.stemplayer.com",
                    "sec-fetch-site": "same-site",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://www.stemplayer.com/",
                    "Host": "api.stemplayer.com",
                    "Connection": "keep-alive"
                    }
                id = r.json()['data']['id']
                r = requests.get(f'https://api.stemplayer.com/tracks/{id}',headers=headers)
                if r.json()['data']['status'] ==  'ready':
                    bass = r.json()['data']['stems']['bass']
                    drums = r.json()['data']['stems']['drums']
                    other = r.json()['data']['stems']['other']
                    vocals = r.json()['data']['stems']['vocals']
                    return bass, drums, other, vocals


            
            
    else:
        print(f'Error sending request{[r.status_code]}')
        
        

        
if __name__ == '__main__':
     bass,drums,other,vocals = stems()

     print(f'bass: {bass}')
     print(f'drums: {drums}')
     print(f'other: {other}')
     print(f'vocals: {vocals}')
     print('Opperation completed!')

input('Press enter to exit')