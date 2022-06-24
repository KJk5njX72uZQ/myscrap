import requests
import json


def get_data():
	cookies = {
		'__js_p_': '631,3600,0,1,0',
		'__jhash_': '1092',
		'__jua_': 'Mozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F103.0.0.0%20Safari%2F537.36',
		'__hash_': '11ba3e51e004380fc74b4783a7b54964',
		'__lhash_': 'd7c91c5969566d6ccfbdfe49f76a6971',
		'CACHE_INDICATOR': 'false',
		'COMPARISON_INDICATOR': 'false',
		'HINTS_FIO_COOKIE_NAME': '1',
		'MAIN_PAGE_VARIATION_1': '2',
		'MVID_2_exp_in_1': '1',
		'MVID_AB_SERVICES_DESCRIPTION': 'var4',
		'MVID_ADDRESS_COMMENT_AB_TEST': '2',
		'MVID_BLACK_FRIDAY_ENABLED': 'true',
		'MVID_CALC_BONUS_RUBLES_PROFIT': 'true',
		'MVID_CART_MULTI_DELETE': 'true',
		'MVID_CATALOG_STATE': '1',
		'MVID_CITY_ID': 'CityCZ_975',
		'MVID_FILTER_CODES': 'true',
		'MVID_FILTER_TOOLTIP': '1',
		'MVID_FLOCKTORY_ON': 'true',
		'MVID_GEOLOCATION_NEEDED': 'true',
		'MVID_GET_LOCATION_BY_DADATA': 'DaData',
		'MVID_GIFT_KIT': 'true',
		'MVID_GUEST_ID': '19294784673',
		'MVID_IS_NEW_BR_WIDGET': 'true',
		'MVID_KLADR_ID': '7700000000000',
		'MVID_LAYOUT_TYPE': '1',
		'MVID_LP_SOLD_VARIANTS': '2',
		'MVID_NEW_ACCESSORY': 'true',
		'MVID_NEW_DESKTOP_FILTERS': 'true',
		'MVID_NEW_LK': 'true',
		'MVID_NEW_LK_CHECK_CAPTCHA': 'true',
		'MVID_NEW_LK_LOGIN': 'true',
		'MVID_NEW_LK_MENU_BUTTON': 'true',
		'MVID_NEW_LK_OTP_TIMER': 'true',
		'MVID_NEW_MBONUS_BLOCK': 'true',
		'MVID_NEW_SUGGESTIONS': 'true',
		'MVID_PROMO_CATALOG_ON': 'true',
		'MVID_REGION_ID': '1',
		'MVID_REGION_SHOP': 'S002',
		'MVID_SERVICES': '111',
		'MVID_SERVICES_MINI_BLOCK': 'var2',
		'MVID_TAXI_DELIVERY_INTERVALS_VIEW': 'new',
		'MVID_TIMEZONE_OFFSET': '3',
		'MVID_WEBP_ENABLED': 'true',
		'NEED_REQUIRE_APPLY_DISCOUNT': 'true',
		'PICKUP_SEAMLESS_AB_TEST': '2',
		'PRESELECT_COURIER_DELIVERY_FOR_KBT': 'false',
		'PROMOLISTING_WITHOUT_STOCK_AB_TEST': '2',
		'flacktory': 'no',
		'MVID_ENVCLOUD': 'primary',
		'searchType2': '1',
		'BIGipServeratg-pilot-pool': '572500490.20480.0000',
		'JSESSIONID': '38qyv0cQhwvZ26jhyZ0TQXW0gLqvKnmN82GWH2v9vLV9zry0Lhhw!-2000628220',
		'bIPs': '-1323973254',
		'ADRUM_BT': 'R:102|g:c0cd6d74-617d-4a3e-a567-d36de14c1af673399',
	}

	headers = {
		'authority': 'www.mvideo.ru',
		'accept': 'application/json',
		'accept-language': 'en-GB,en;q=0.9,et-EE;q=0.8,et;q=0.7,ru-RU;q=0.6,ru;q=0.5,en-US;q=0.4',
		'cache-control': 'no-cache',
		'pragma': 'no-cache',
		'referer': 'https://www.mvideo.ru/noutbuki-planshety-komputery-8/planshety-195/f/category=planshety-na-android-930',
		'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
		'sec-ch-ua-mobile': '?0',
		'sec-ch-ua-platform': '"Windows"',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'same-origin',
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
		'x-set-application-id': '8f26bda0-b117-4603-bd5b-45b7a8b1d711',
	}

	params = {
		'categoryId': '195',
		'offset': '0',
		'limit': '24',
		'filterParams': 'WyJjYXRlZ29yeSIsIiIsInBsYW5zaGV0eS1uYS1hbmRyb2lkLTkzMCJd',
		'doTranslit': 'true',
	}

	response = requests.get('https://www.mvideo.ru/bff/products/listing', params=params, cookies=cookies, headers=headers).json()
	print(response)
    
def main():
    get_data()
    # get_result()
    
    
if __name__ == '__main__':
    main()