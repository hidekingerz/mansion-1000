from bs4 import BeautifulSoup
import requests
import pandas as pd


# from pandas import Series, DataFrame
# import time

def make_soup(url):
    result = requests.get(url)
    soup = BeautifulSoup(result.text, 'lxml')
    return soup


def get_content(data):
    summary = data.find(id='js-bukkenList')
    return summary


def get_urls(data, url):
    max_url = data.select('ol[class="pagination-parts"] > li:last-child > a')
    list_urls = []
    for i in range(1, int(max_url[0].get_text()) + 1):
        page_url = url + "?page=" + str(i)
        list_urls.append(page_url)
    return list_urls


def analize_urls(list_urls):
    bukken_data = []
    for url in list_urls:
        print(url)
        soup_url = make_soup(url)
        cassette_items = soup_url.select('div[class="cassetteitem"]')
        for i in range(len(cassette_items)):
            tr = cassette_items[i].select('tr[class="js-cassette_link"]')
            for sub_data in tr:
                plan_data = {}
                sub_title = cassette_items[i].find("div", {'class': 'cassetteitem_content-title'}).get_text()
                sub_address = cassette_items[i].find("li", {'class': 'cassetteitem_detail-col1'}).get_text()
                plan_data["name"] = sub_title
                plan_data["address"] = sub_address
                sub_locations = cassette_items[i].find_all("div", {'class': 'cassetteitem_detail-text'})
                if len(sub_locations) == 1:
                    plan_data["locations0"] = sub_locations[0].get_text()
                elif len(sub_locations) == 2:
                    plan_data["locations0"] = sub_locations[0].get_text()
                    plan_data["locations1"] = sub_locations[1].get_text()
                elif len(sub_locations) == 3:
                    plan_data["locations0"] = sub_locations[0].get_text()
                    plan_data["locations1"] = sub_locations[1].get_text()
                    plan_data["locations2"] = sub_locations[2].get_text()

                sub_age_height = cassette_items[i].select('li[class="cassetteitem_detail-col3"] > div')
                if len(sub_age_height) == 1:
                    plan_data["age"] = sub_age_height[0].get_text()
                elif len(sub_age_height) == 2:
                    plan_data["age"] = sub_age_height[0].get_text()
                    plan_data["height"] = sub_age_height[1].get_text()
                cols = sub_data.find_all('td')
                plan_data["floor"] = cols[2].get_text().strip()
                data_rent = cols[3].select('span[class="cassetteitem_price cassetteitem_price--rent"] > span')
                plan_data["rent"] = data_rent[0].get_text()
                data_admin = cols[3].select('span[class="cassetteitem_price cassetteitem_price--administration"]')
                plan_data["admin"] = data_admin[0].get_text()
                data_deposit = cols[4].select('span[class="cassetteitem_price cassetteitem_price--deposit"]')
                plan_data["deposit"] = data_deposit[0].get_text()
                data_gratuity = cols[4].select('span[class="cassetteitem_price cassetteitem_price--gratuity"]')
                plan_data["gratuity"] = data_gratuity[0].get_text()
                data_floor_plan = cols[5].select('span[class="cassetteitem_madori"]')
                plan_data["floor_plan"] = data_floor_plan[0].get_text()
                data_area = cols[5].select('span[class="cassetteitem_menseki"]')
                plan_data["area"] = data_area[0].get_text()
                bukken_data.append(plan_data)
    return bukken_data


def loop_tokyo(target_list):
    base_url = 'https://suumo.jp/chintai/tokyo/'

    for target in target_list:
        target_url = base_url + target + '/mansion/'
        soup = make_soup(target_url)
        urls = get_urls(soup, target_url)
        data = analize_urls(urls)
        suumo_df = pd.io.json.json_normalize(data)
        filename = target + '.csv'
        suumo_df.to_csv(filename, sep='\t', encoding='utf-16')


if __name__ == "__main__":
    target_list = ['sc_adachi',
                   'sc_arakawa',
                   'sc_bunkyo',
                   'sc_chiyoda',
                   'sc_chuo',
                   'sc_edogawa',
                   'sc_itabashi',
                   'sc_katsushika',
                   'sc_kita',
                   'sc_koto',
                   'sc_meguro',
                   'sc_minato',
                   'sc_nakano',
                   'sc_nerima',
                   'sc_ota',
                   'sc_shinjuku',
                   'sc_shibuya',
                   'sc_shinagawa',
                   'sc_setagaya',
                   'sc_suginami',
                   'sc_sumida',
                   'sc_taito',
                   'sc_toshima'
                   # 'sc_hachioji',
                   # 'sc_tachikawa',
                   # 'sc_musashino',
                   # 'sc_mitaka'
                   ]
    loop_tokyo(target_list)
