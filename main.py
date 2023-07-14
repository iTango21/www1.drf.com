import requests
from bs4 import BeautifulSoup
import json


loginName = 'NWILDE@HTC-TX.COM'
password = 'Kiefer13@'

headers = {
    'authority': 'registration.drf.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6,vi;q=0.5,pt;q=0.4,ka;q=0.3',
    'content-type': 'application/json',
    'origin': 'https://www.drf.com',
    'referer': 'https://www.drf.com/',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
}

json_data = {
    'loginName': f'{loginName}',
    'password': f'{password}',
}

response = requests.post('https://registration.drf.com/v2/login', headers=headers, json=json_data)

data_ = json.loads(response.text)
customerId = data_['customerId']

cookies = {
    'drf_web_post_login_url': '/HorseBrowseMessages.do?null',
    '_gcl_au': '1.1.1611578912.1689261140',
    '_gid': 'GA1.2.1544736626.1689261143',
    '_rdt_uuid': '1689261144063.fb0dac1a-0ac1-47fd-9615-0b144895f32b',
    '_scid': '8ecaba1d-083e-42cd-9718-b63959dff82e',
    'rl_page_init_referrer': 'RudderEncrypt%3AU2FsdGVkX1%2F673NwwZSGRYW8BW9zokJagTbDBheBKfs%3D',
    'rl_page_init_referring_domain': 'RudderEncrypt%3AU2FsdGVkX18UG2zc2PVB5NhcqAW7%2FpV5wbJTo5pmjhM%3D',
    'DRF_UA': 'Mozilla%2F5.0%20(Windows%20NT%2010.0%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F114.0.0.0%20Safari%2F537.36',
    '_hp2_ses_props.2529982013': '%7B%22ts%22%3A1689261146097%2C%22d%22%3A%22shop.drf.com%22%2C%22h%22%3A%22%2Fcompare-pp-plans%22%7D',
    'DRF_IP': '154.28.188.234',
    'afUserId': '62c4c46c-643f-41cf-9c0d-aca2ac9fbee5-p',
    'AF_SYNC': '1689261161548',
    'DRF_SSO_AUTH': '%7B%22userId%22%3A1731580%2C%22userName%22%3A%22NWILDE%40HTC-TX.COM%22%2C%22firstName%22%3A%22Nancy%22%2C%22lastName%22%3A%22Wilde%22%2C%22email%22%3A%22forward4%40htc-tx.info%22%2C%22country%22%3A%22USA%22%2C%22state%22%3A%22NY%22%2C%22zipCode%22%3A%2213148%22%2C%22Domain%22%3A%22.drf.com%22%2C%22xpbUser%22%3A%7B%22displayName%22%3A%22Wilde%22%2C%22uid%22%3A%22forward4%40htc-tx.info%22%7D%2C%22hasAnsweredQuestionnaire%22%3Afalse%7D',
    'drf_web_customer_id': f'{customerId}',
    'WDAC_USER': f'"{loginName}"',
    'drf_news_customer_id': f'{customerId}',
    'drf_web_subs': '"{ \\"webSubs\\": ]} "',
    '_hp2_props.2529982013': '%7B%22loggedIn%22%3Atrue%7D',
    'IS_DEFAULT_DRF_HOMEPAGE': '"1"',
    'JSESSIONID': '9D8B807FCCAA7231691B50B67EF23B0C',
    '_ga_44VZPRLSCR': 'GS1.1.1689261142.1.1.1689262027.0.0.0',
    '_ga': 'GA1.1.320781379.1689261143',
    '_hp2_id.2529982013': '%7B%22userId%22%3A%226938076164353948%22%2C%22pageviewId%22%3A%226454993107218964%22%2C%22sessionId%22%3A%228866782527566854%22%2C%22identity%22%3A%221731580%22%2C%22trackerVersion%22%3A%224.0%22%2C%22identityField%22%3Anull%2C%22isIdentified%22%3A1%7D',
    'rl_user_id': 'RudderEncrypt%3AU2FsdGVkX1%2F7G60bI7cjwx8%2BWlpqTIPPDrq%2B9Q3hsU0%3D',
    'rl_trait': 'RudderEncrypt%3AU2FsdGVkX1%2BQ1IsKati3%2F9eQNrvoURmbPf%2FC15No%2FRo%3D',
    'rl_group_id': 'RudderEncrypt%3AU2FsdGVkX18RrtLfnPOQuZ0j7RvUSaeWJOC5P%2BtkmAA%3D',
    'rl_group_trait': 'RudderEncrypt%3AU2FsdGVkX19q0rW8uCI7p6znjW941dcCs4wfEcRRQy4%3D',
    'rl_anonymous_id': 'RudderEncrypt%3AU2FsdGVkX18TowqMf4Cmwse0r321KdbVa8OZBxyxAooV%2Fx3w7pQVA%2FYG33ljURyp3GhaV5ak7vAMM4Bq%2FqaMwQ%3D%3D',
    '_scid_r': '8ecaba1d-083e-42cd-9718-b63959dff82e',
    'rl_session': 'RudderEncrypt%3AU2FsdGVkX19NWNuAGEZpkCkUOrMYi6EpXFFSpV%2F9C0Wr8NihINd8ahZWY%2FqlgkW9TvOKiDi5vW8Y8jeF3%2BuTzhy88At%2BNVFhsIRn2YYoJElbCpyTsbRnvZvOA9ZbXEcfw%2F1LSuHDHbdOqH4aYq85ag%3D%3D',
    'closedTabs': '%5B%5D',
    'NSC_JOhqqceqe1gaw1tdkic3ehcweifu4c0': 'ffffffff09e0522f45525d5f4f58455e445a4a4229a0',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6,vi;q=0.5,pt;q=0.4,ka;q=0.3',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    # 'Cookie': 'drf_web_post_login_url=/HorseBrowseMessages.do?null; _gcl_au=1.1.1611578912.1689261140; _gid=GA1.2.1544736626.1689261143; _rdt_uuid=1689261144063.fb0dac1a-0ac1-47fd-9615-0b144895f32b; _scid=8ecaba1d-083e-42cd-9718-b63959dff82e; rl_page_init_referrer=RudderEncrypt%3AU2FsdGVkX1%2F673NwwZSGRYW8BW9zokJagTbDBheBKfs%3D; rl_page_init_referring_domain=RudderEncrypt%3AU2FsdGVkX18UG2zc2PVB5NhcqAW7%2FpV5wbJTo5pmjhM%3D; DRF_UA=Mozilla%2F5.0%20(Windows%20NT%2010.0%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F114.0.0.0%20Safari%2F537.36; _hp2_ses_props.2529982013=%7B%22ts%22%3A1689261146097%2C%22d%22%3A%22shop.drf.com%22%2C%22h%22%3A%22%2Fcompare-pp-plans%22%7D; DRF_IP=154.28.188.234; afUserId=62c4c46c-643f-41cf-9c0d-aca2ac9fbee5-p; AF_SYNC=1689261161548; DRF_SSO_AUTH=%7B%22userId%22%3A1731580%2C%22userName%22%3A%22NWILDE%40HTC-TX.COM%22%2C%22firstName%22%3A%22Nancy%22%2C%22lastName%22%3A%22Wilde%22%2C%22email%22%3A%22forward4%40htc-tx.info%22%2C%22country%22%3A%22USA%22%2C%22state%22%3A%22NY%22%2C%22zipCode%22%3A%2213148%22%2C%22Domain%22%3A%22.drf.com%22%2C%22xpbUser%22%3A%7B%22displayName%22%3A%22Wilde%22%2C%22uid%22%3A%22forward4%40htc-tx.info%22%7D%2C%22hasAnsweredQuestionnaire%22%3Afalse%7D; drf_web_customer_id=1731580; WDAC_USER="NWILDE@HTC-TX.COM"; drf_news_customer_id=1731580; drf_web_subs="{ \\"webSubs\\": ]} "; _hp2_props.2529982013=%7B%22loggedIn%22%3Atrue%7D; IS_DEFAULT_DRF_HOMEPAGE="1"; JSESSIONID=9D8B807FCCAA7231691B50B67EF23B0C; _ga_44VZPRLSCR=GS1.1.1689261142.1.1.1689262027.0.0.0; _ga=GA1.1.320781379.1689261143; _hp2_id.2529982013=%7B%22userId%22%3A%226938076164353948%22%2C%22pageviewId%22%3A%226454993107218964%22%2C%22sessionId%22%3A%228866782527566854%22%2C%22identity%22%3A%221731580%22%2C%22trackerVersion%22%3A%224.0%22%2C%22identityField%22%3Anull%2C%22isIdentified%22%3A1%7D; rl_user_id=RudderEncrypt%3AU2FsdGVkX1%2F7G60bI7cjwx8%2BWlpqTIPPDrq%2B9Q3hsU0%3D; rl_trait=RudderEncrypt%3AU2FsdGVkX1%2BQ1IsKati3%2F9eQNrvoURmbPf%2FC15No%2FRo%3D; rl_group_id=RudderEncrypt%3AU2FsdGVkX18RrtLfnPOQuZ0j7RvUSaeWJOC5P%2BtkmAA%3D; rl_group_trait=RudderEncrypt%3AU2FsdGVkX19q0rW8uCI7p6znjW941dcCs4wfEcRRQy4%3D; rl_anonymous_id=RudderEncrypt%3AU2FsdGVkX18TowqMf4Cmwse0r321KdbVa8OZBxyxAooV%2Fx3w7pQVA%2FYG33ljURyp3GhaV5ak7vAMM4Bq%2FqaMwQ%3D%3D; _scid_r=8ecaba1d-083e-42cd-9718-b63959dff82e; rl_session=RudderEncrypt%3AU2FsdGVkX19NWNuAGEZpkCkUOrMYi6EpXFFSpV%2F9C0Wr8NihINd8ahZWY%2FqlgkW9TvOKiDi5vW8Y8jeF3%2BuTzhy88At%2BNVFhsIRn2YYoJElbCpyTsbRnvZvOA9ZbXEcfw%2F1LSuHDHbdOqH4aYq85ag%3D%3D; closedTabs=%5B%5D; NSC_JOhqqceqe1gaw1tdkic3ehcweifu4c0=ffffffff09e0522f45525d5f4f58455e445a4a4229a0',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get('https://www1.drf.com/HorseBrowseMessages.do', cookies=cookies, headers=headers)

soup = BeautifulSoup(response.text, 'lxml')
pg__ = soup.find_all('tbody')

# Find all 'a' tags with the 'id' attribute
a_tags_with_id = pg__[0].find_all('a', id=True)

arr_ = []

# Read data from the file "all.json" into the list list_111
with open("all.json", "r") as file:
    list_111 = json.load(file)

list_222 = list_111[:]  # Create a copy of the list list_111
new_data = []  # List to store only new data
new_h = 0

cou_ = len(a_tags_with_id)

for i, tag in enumerate(a_tags_with_id):

    id_ = tag['id']
    print(f'{i + 1} / {cou_} --->>> {id_}')

    cookies = {
        'drf_web_post_login_url': '/HorseBrowseMessages.do?null',
        '_gcl_au': '1.1.1611578912.1689261140',
        '_gid': 'GA1.2.1544736626.1689261143',
        '_rdt_uuid': '1689261144063.fb0dac1a-0ac1-47fd-9615-0b144895f32b',
        '_scid': '8ecaba1d-083e-42cd-9718-b63959dff82e',
        'rl_page_init_referrer': 'RudderEncrypt%3AU2FsdGVkX1%2F673NwwZSGRYW8BW9zokJagTbDBheBKfs%3D',
        'rl_page_init_referring_domain': 'RudderEncrypt%3AU2FsdGVkX18UG2zc2PVB5NhcqAW7%2FpV5wbJTo5pmjhM%3D',
        'DRF_UA': 'Mozilla%2F5.0%20(Windows%20NT%2010.0%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F114.0.0.0%20Safari%2F537.36',
        'afUserId': '62c4c46c-643f-41cf-9c0d-aca2ac9fbee5-p',
        'AF_SYNC': '1689261161548',
        'overlay_cookie': '"Overlay Cancelled"',
        'DRF_SSO_AUTH': '%7B%22userId%22%3A1731580%2C%22userName%22%3A%22NWILDE%40HTC-TX.COM%22%2C%22firstName%22%3A%22Nancy%22%2C%22lastName%22%3A%22Wilde%22%2C%22email%22%3A%22forward4%40htc-tx.info%22%2C%22country%22%3A%22USA%22%2C%22state%22%3A%22NY%22%2C%22zipCode%22%3A%2213148%22%2C%22Domain%22%3A%22.drf.com%22%2C%22xpbUser%22%3A%7B%22displayName%22%3A%22Wilde%22%2C%22uid%22%3A%22forward4%40htc-tx.info%22%7D%2C%22hasAnsweredQuestionnaire%22%3Afalse%7D',
        'drf_web_customer_id': f'{customerId}',
        'WDAC_USER': f'"{loginName}"',
        'drf_news_customer_id': f'{customerId}',
        'drf_web_subs': '"{ \\"webSubs\\": ]} "',
        '_hp2_props.2529982013': '%7B%22loggedIn%22%3Atrue%7D',
        'DRF_IP': '217.146.13.85',
        '_ga_44VZPRLSCR': 'GS1.1.1689268324.3.1.1689272492.0.0.0',
        '_scid_r': '8ecaba1d-083e-42cd-9718-b63959dff82e',
        'rl_user_id': 'RudderEncrypt%3AU2FsdGVkX1%2FjGwB%2FwWetiHzFUS880oXxMStSg3VMs1k%3D',
        'rl_trait': 'RudderEncrypt%3AU2FsdGVkX1%2FE9ut1B7oJJTIlYh06mIWZ5EgeNYhCwA8%3D',
        'rl_group_id': 'RudderEncrypt%3AU2FsdGVkX1%2FZNGuwQ1bWW8GDxxHXWYN%2FfxUpdvPbvAA%3D',
        'rl_group_trait': 'RudderEncrypt%3AU2FsdGVkX18n3%2F8YLAEPB9oDry61Xkg9DOfL8DZva14%3D',
        'rl_anonymous_id': 'RudderEncrypt%3AU2FsdGVkX19qUhfs9J9zNtBGVKdpxVCN8mgqYYYNUbxmi%2BAfthVfo1fTkFrIRy0t5YgvFBx4bi8aapwtkfK7ZQ%3D%3D',
        'rl_session': 'RudderEncrypt%3AU2FsdGVkX1%2F%2BXuGbddqjYMNIsNeR0AGE8iOrI7E%2FenzqztkUz7OSoEgX0kUkKy0Yp%2Fbq21hN80b3iqq72PxAsmqUfOXkTepje8TlGZgRupkK4fT6ml96VZClyGoK6f4wxx%2FEhkTwmMsPUNzWUwt6Wg%3D%3D',
        '_ga': 'GA1.2.320781379.1689261143',
        'JSESSIONID': '8FD27E6E8C8097EAC1B314B43B21F6E8',
        'NSC_JOhqqceqe1gaw1tdkic3ehcweifu4c0': 'ffffffff09e0522e45525d5f4f58455e445a4a4229a0',
        '_hp2_id.2529982013': '%7B%22userId%22%3A%226938076164353948%22%2C%22pageviewId%22%3A%225267731843396930%22%2C%22sessionId%22%3A%225157960364891099%22%2C%22identity%22%3A%221731580%22%2C%22trackerVersion%22%3A%224.0%22%2C%22identityField%22%3Anull%2C%22isIdentified%22%3A1%7D',
        '_hp2_ses_props.2529982013': '%7B%22ts%22%3A1689275336483%2C%22d%22%3A%22www1.drf.com%22%2C%22h%22%3A%22%2FHorseBrowseMessages.do%22%7D',
        'closedTabs': '%5B%5D',
    }

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6,vi;q=0.5,pt;q=0.4,ka;q=0.3',
        'Connection': 'keep-alive',
        # 'Content-Length': '0',
        # 'Cookie': 'drf_web_post_login_url=/HorseBrowseMessages.do?null; _gcl_au=1.1.1611578912.1689261140; _gid=GA1.2.1544736626.1689261143; _rdt_uuid=1689261144063.fb0dac1a-0ac1-47fd-9615-0b144895f32b; _scid=8ecaba1d-083e-42cd-9718-b63959dff82e; rl_page_init_referrer=RudderEncrypt%3AU2FsdGVkX1%2F673NwwZSGRYW8BW9zokJagTbDBheBKfs%3D; rl_page_init_referring_domain=RudderEncrypt%3AU2FsdGVkX18UG2zc2PVB5NhcqAW7%2FpV5wbJTo5pmjhM%3D; DRF_UA=Mozilla%2F5.0%20(Windows%20NT%2010.0%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F114.0.0.0%20Safari%2F537.36; afUserId=62c4c46c-643f-41cf-9c0d-aca2ac9fbee5-p; AF_SYNC=1689261161548; overlay_cookie="Overlay Cancelled"; DRF_SSO_AUTH=%7B%22userId%22%3A1731580%2C%22userName%22%3A%22NWILDE%40HTC-TX.COM%22%2C%22firstName%22%3A%22Nancy%22%2C%22lastName%22%3A%22Wilde%22%2C%22email%22%3A%22forward4%40htc-tx.info%22%2C%22country%22%3A%22USA%22%2C%22state%22%3A%22NY%22%2C%22zipCode%22%3A%2213148%22%2C%22Domain%22%3A%22.drf.com%22%2C%22xpbUser%22%3A%7B%22displayName%22%3A%22Wilde%22%2C%22uid%22%3A%22forward4%40htc-tx.info%22%7D%2C%22hasAnsweredQuestionnaire%22%3Afalse%7D; drf_web_customer_id=1731580; WDAC_USER="NWILDE@HTC-TX.COM"; drf_news_customer_id=1731580; drf_web_subs="{ \\"webSubs\\": ]} "; _hp2_props.2529982013=%7B%22loggedIn%22%3Atrue%7D; DRF_IP=217.146.13.85; _ga_44VZPRLSCR=GS1.1.1689268324.3.1.1689272492.0.0.0; _scid_r=8ecaba1d-083e-42cd-9718-b63959dff82e; rl_user_id=RudderEncrypt%3AU2FsdGVkX1%2FjGwB%2FwWetiHzFUS880oXxMStSg3VMs1k%3D; rl_trait=RudderEncrypt%3AU2FsdGVkX1%2FE9ut1B7oJJTIlYh06mIWZ5EgeNYhCwA8%3D; rl_group_id=RudderEncrypt%3AU2FsdGVkX1%2FZNGuwQ1bWW8GDxxHXWYN%2FfxUpdvPbvAA%3D; rl_group_trait=RudderEncrypt%3AU2FsdGVkX18n3%2F8YLAEPB9oDry61Xkg9DOfL8DZva14%3D; rl_anonymous_id=RudderEncrypt%3AU2FsdGVkX19qUhfs9J9zNtBGVKdpxVCN8mgqYYYNUbxmi%2BAfthVfo1fTkFrIRy0t5YgvFBx4bi8aapwtkfK7ZQ%3D%3D; rl_session=RudderEncrypt%3AU2FsdGVkX1%2F%2BXuGbddqjYMNIsNeR0AGE8iOrI7E%2FenzqztkUz7OSoEgX0kUkKy0Yp%2Fbq21hN80b3iqq72PxAsmqUfOXkTepje8TlGZgRupkK4fT6ml96VZClyGoK6f4wxx%2FEhkTwmMsPUNzWUwt6Wg%3D%3D; _ga=GA1.2.320781379.1689261143; JSESSIONID=8FD27E6E8C8097EAC1B314B43B21F6E8; NSC_JOhqqceqe1gaw1tdkic3ehcweifu4c0=ffffffff09e0522e45525d5f4f58455e445a4a4229a0; _hp2_id.2529982013=%7B%22userId%22%3A%226938076164353948%22%2C%22pageviewId%22%3A%225267731843396930%22%2C%22sessionId%22%3A%225157960364891099%22%2C%22identity%22%3A%221731580%22%2C%22trackerVersion%22%3A%224.0%22%2C%22identityField%22%3Anull%2C%22isIdentified%22%3A1%7D; _hp2_ses_props.2529982013=%7B%22ts%22%3A1689275336483%2C%22d%22%3A%22www1.drf.com%22%2C%22h%22%3A%22%2FHorseBrowseMessages.do%22%7D; closedTabs=%5B%5D',
        'Origin': 'https://www1.drf.com',
        'Referer': 'https://www1.drf.com/HorseBrowseMessages.do',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    params = {
        'watchMessageId': f'{id_}',
    }

    response = requests.post('https://www1.drf.com/HorseNotification.do', params=params, cookies=cookies, headers=headers)

    data__ = json.loads(response.text)

    # Check for equality with the blocks in list_111
    data_exists = False
    for item in list_111:
        if item == data__:
            data_exists = True
            break

    if not data_exists:
        list_222.insert(0, data__)  # Add data to the beginning of list_222
        new_data.append(data__)  # Add new data to the new_data list
        new_h += 1

        print(f'{id_} --->>> New = {new_h} !!!!!!!!!!!!!!!')
    else:
        # break  # Прерывание цикла
        print(f'{id_} --->>> is on the list!')

# Write data from list_222 to the file qwerty.json
with open("all.json", "w") as file:
    json.dump(list_222, file, indent=4, ensure_ascii=False)

# Write only new data to the file new.json
with open("new.json", "w") as file:
    json.dump(new_data, file, indent=4, ensure_ascii=False)
