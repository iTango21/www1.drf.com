import requests
import json

date_ = '07-23-2023'

cookies = {
    '_gcl_au': '1.1.2097689326.1689248122',
    'lastREF': 'https://www.upwork.com/',
    '_scid': '13888b88-aac5-4d31-8b09-fdbf8f8f6fe8',
    '_rdt_uuid': '1689248122132.9a62648a-455d-4cd8-91ce-6765f5611405',
    'rl_page_init_referrer': 'RudderEncrypt%3AU2FsdGVkX19M3BIPDHO9J7%2Fz%2FfLygrMy8bl7kKw8NIlI7C%2FVSUZdwr9cU1lkFil5',
    'rl_page_init_referring_domain': 'RudderEncrypt%3AU2FsdGVkX19R7ww0q8HQTrvpU1kmy4lyu3zwHXnLtHT4skarP87neMJfDyUpNpSB',
    'afUserId': '41cbcd2a-49ce-46bd-92c0-fb8556119970-p',
    'drf_web_post_login_url': '/HorseBrowseMessages.do?null',
    'ppLineCount': '6',
    'DRF_SSO_AUTH': '%7B%22userId%22%3A1920165%2C%22userName%22%3A%22ITANGO21%40GMAIL.COM%22%2C%22firstName%22%3A%22-%22%2C%22lastName%22%3A%22-%22%2C%22email%22%3A%22itango21%40gmail.com%22%2C%22country%22%3A%22DE%22%2C%22state%22%3A%22%20%22%2C%22zipCode%22%3A%22%20%22%2C%22Domain%22%3A%22.drf.com%22%2C%22xpbUser%22%3A%7B%22displayName%22%3Anull%2C%22uid%22%3Anull%7D%2C%22hasAnsweredQuestionnaire%22%3Afalse%7D',
    'drf_web_customer_id': '1920165',
    'WDAC_USER': '"ITANGO21@GMAIL.COM"',
    'drf_news_customer_id': '1920165',
    'drf_web_subs': '"{ \\"webSubs\\": ]} "',
    '_hp2_props.2529982013': '%7B%22loggedIn%22%3Atrue%7D',
    '_gid': 'GA1.2.2106723135.1690196652',
    'DRF_UA': 'Mozilla%2F5.0%20(Windows%20NT%2010.0%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F115.0.0.0%20Safari%2F537.36',
    'DRF_IP': '156.146.59.32',
    '_hp2_ses_props.2529982013': '%7B%22ts%22%3A1690196653653%2C%22d%22%3A%22shop.drf.com%22%2C%22h%22%3A%22%2Fcompare-pp-plans%22%7D',
    'promoREF': 'https://www.upwork.com/',
    'AF_SYNC': '1690196773707',
    '_sctr': '1%7C1690146000000',
    'closedTabs': '%5B%5D',
    'PHPSESSID': 'u1ll0rlgbsongjqa53fikqmbo2',
    'ba52a9d4895bdfeacc2d0e3559ec207a': '1431361f5f7c5021e582f5c31761dde2e6d07de9a%3A4%3A%7Bi%3A0%3Bs%3A18%3A%22ITANGO21%40GMAIL.COM%22%3Bi%3A1%3Bs%3A18%3A%22ITANGO21%40GMAIL.COM%22%3Bi%3A2%3Bi%3A604800%3Bi%3A3%3Ba%3A0%3A%7B%7D%7D',
    '_gat_UA-973056-1': '1',
    '_hp2_id.2529982013': '%7B%22userId%22%3A%2275492345499248%22%2C%22pageviewId%22%3A%221785109113557584%22%2C%22sessionId%22%3A%226186303560965945%22%2C%22identity%22%3A%221920165%22%2C%22trackerVersion%22%3A%224.0%22%2C%22identityField%22%3Anull%2C%22isIdentified%22%3A1%2C%22oldIdentity%22%3Anull%7D',
    '_ga_44VZPRLSCR': 'GS1.1.1690196654.2.1.1690197949.0.0.0',
    'rl_user_id': 'RudderEncrypt%3AU2FsdGVkX18nEnNmkMIXIO%2FIwOJbulBA5LGAbR%2BUaoU%3D',
    'rl_trait': 'RudderEncrypt%3AU2FsdGVkX1%2B9GetfNHOLocsXcTO%2FvSBQmDIgLXsMSZM%3D',
    'rl_group_id': 'RudderEncrypt%3AU2FsdGVkX1%2FZPxeqtmVUIpqCHqyjAbJQK8C2JN8XYX4%3D',
    'rl_group_trait': 'RudderEncrypt%3AU2FsdGVkX1%2FDdcxkVdhKtuBM9jZbkI0VWzDHvPqeXu4%3D',
    'rl_anonymous_id': 'RudderEncrypt%3AU2FsdGVkX1%2BZY9Iwrg8V44qbTGV%2Fi4u3%2FTRxEfH%2FzDs4gtnhEsur6BGh51pAIEIkD0WkD0rTv9BRcO37137uHw%3D%3D',
    '_scid_r': '13888b88-aac5-4d31-8b09-fdbf8f8f6fe8',
    'rl_session': 'RudderEncrypt%3AU2FsdGVkX1%2Bn9n5xkcNJy9SBHthuRx6BlYzcPEuK08th%2Fh%2F9gOg3pSEQlCMcBIzNr4VjGt%2Fy0EptHhdmD8G%2BeBMWWcPyhIAxGjiXWxe1OQycmDM%2BCe61QTm9PQ6pZqDRz3FL4iaiwsm7GPBr42nV7A%3D%3D',
    '_ga': 'GA1.2.726945326.1689248122',
}

headers = {
    'authority': 'www.drf.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6,vi;q=0.5,pt;q=0.4,ka;q=0.3',
    # 'cookie': '_gcl_au=1.1.2097689326.1689248122; lastREF=https://www.upwork.com/; _scid=13888b88-aac5-4d31-8b09-fdbf8f8f6fe8; _rdt_uuid=1689248122132.9a62648a-455d-4cd8-91ce-6765f5611405; rl_page_init_referrer=RudderEncrypt%3AU2FsdGVkX19M3BIPDHO9J7%2Fz%2FfLygrMy8bl7kKw8NIlI7C%2FVSUZdwr9cU1lkFil5; rl_page_init_referring_domain=RudderEncrypt%3AU2FsdGVkX19R7ww0q8HQTrvpU1kmy4lyu3zwHXnLtHT4skarP87neMJfDyUpNpSB; afUserId=41cbcd2a-49ce-46bd-92c0-fb8556119970-p; drf_web_post_login_url=/HorseBrowseMessages.do?null; ppLineCount=6; DRF_SSO_AUTH=%7B%22userId%22%3A1920165%2C%22userName%22%3A%22ITANGO21%40GMAIL.COM%22%2C%22firstName%22%3A%22-%22%2C%22lastName%22%3A%22-%22%2C%22email%22%3A%22itango21%40gmail.com%22%2C%22country%22%3A%22DE%22%2C%22state%22%3A%22%20%22%2C%22zipCode%22%3A%22%20%22%2C%22Domain%22%3A%22.drf.com%22%2C%22xpbUser%22%3A%7B%22displayName%22%3Anull%2C%22uid%22%3Anull%7D%2C%22hasAnsweredQuestionnaire%22%3Afalse%7D; drf_web_customer_id=1920165; WDAC_USER="ITANGO21@GMAIL.COM"; drf_news_customer_id=1920165; drf_web_subs="{ \\"webSubs\\": ]} "; _hp2_props.2529982013=%7B%22loggedIn%22%3Atrue%7D; _gid=GA1.2.2106723135.1690196652; DRF_UA=Mozilla%2F5.0%20(Windows%20NT%2010.0%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F115.0.0.0%20Safari%2F537.36; DRF_IP=156.146.59.32; _hp2_ses_props.2529982013=%7B%22ts%22%3A1690196653653%2C%22d%22%3A%22shop.drf.com%22%2C%22h%22%3A%22%2Fcompare-pp-plans%22%7D; promoREF=https://www.upwork.com/; AF_SYNC=1690196773707; _sctr=1%7C1690146000000; closedTabs=%5B%5D; PHPSESSID=u1ll0rlgbsongjqa53fikqmbo2; ba52a9d4895bdfeacc2d0e3559ec207a=1431361f5f7c5021e582f5c31761dde2e6d07de9a%3A4%3A%7Bi%3A0%3Bs%3A18%3A%22ITANGO21%40GMAIL.COM%22%3Bi%3A1%3Bs%3A18%3A%22ITANGO21%40GMAIL.COM%22%3Bi%3A2%3Bi%3A604800%3Bi%3A3%3Ba%3A0%3A%7B%7D%7D; _gat_UA-973056-1=1; _hp2_id.2529982013=%7B%22userId%22%3A%2275492345499248%22%2C%22pageviewId%22%3A%221785109113557584%22%2C%22sessionId%22%3A%226186303560965945%22%2C%22identity%22%3A%221920165%22%2C%22trackerVersion%22%3A%224.0%22%2C%22identityField%22%3Anull%2C%22isIdentified%22%3A1%2C%22oldIdentity%22%3Anull%7D; _ga_44VZPRLSCR=GS1.1.1690196654.2.1.1690197949.0.0.0; rl_user_id=RudderEncrypt%3AU2FsdGVkX18nEnNmkMIXIO%2FIwOJbulBA5LGAbR%2BUaoU%3D; rl_trait=RudderEncrypt%3AU2FsdGVkX1%2B9GetfNHOLocsXcTO%2FvSBQmDIgLXsMSZM%3D; rl_group_id=RudderEncrypt%3AU2FsdGVkX1%2FZPxeqtmVUIpqCHqyjAbJQK8C2JN8XYX4%3D; rl_group_trait=RudderEncrypt%3AU2FsdGVkX1%2FDdcxkVdhKtuBM9jZbkI0VWzDHvPqeXu4%3D; rl_anonymous_id=RudderEncrypt%3AU2FsdGVkX1%2BZY9Iwrg8V44qbTGV%2Fi4u3%2FTRxEfH%2FzDs4gtnhEsur6BGh51pAIEIkD0WkD0rTv9BRcO37137uHw%3D%3D; _scid_r=13888b88-aac5-4d31-8b09-fdbf8f8f6fe8; rl_session=RudderEncrypt%3AU2FsdGVkX1%2Bn9n5xkcNJy9SBHthuRx6BlYzcPEuK08th%2Fh%2F9gOg3pSEQlCMcBIzNr4VjGt%2Fy0EptHhdmD8G%2BeBMWWcPyhIAxGjiXWxe1OQycmDM%2BCe61QTm9PQ6pZqDRz3FL4iaiwsm7GPBr42nV7A%3D%3D; _ga=GA1.2.726945326.1689248122',
    'referer': 'https://www.drf.com/race-results/tracks/PRM/country/USA/date/07-23-2023',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

response = requests.get(
    f'https://www.drf.com/results/resultDetails/id/PRM/country/USA/date/{date_}',
    cookies=cookies,
    headers=headers,
)

data_ = json.loads(response.text)

# Write only new data to the file new.json
with open("main_test.json", "w", encoding='utf-8') as file:
    json.dump(data_, file, indent=4, ensure_ascii=False)