import pandas as pd


def format():
    df_adachi = pd.read_csv('sc_adachi.csv', sep='\t', encoding='utf-16')
    df_arakawa = pd.read_csv('sc_arakawa.csv', sep='\t', encoding='utf-16')
    df_bunkyo = pd.read_csv('sc_bunkyo.csv', sep='\t', encoding='utf-16')
    df_chiyoda = pd.read_csv('sc_chiyoda.csv', sep='\t', encoding='utf-16')
    df_chuo = pd.read_csv('sc_chuo.csv', sep='\t', encoding='utf-16')
    df_edogawa = pd.read_csv('sc_edogawa.csv', sep='\t', encoding='utf-16')
    df_itabashi = pd.read_csv('sc_itabashi.csv', sep='\t', encoding='utf-16')
    df_katsushika = pd.read_csv('sc_katsushika.csv', sep='\t', encoding='utf-16')
    df_kita = pd.read_csv('sc_kita.csv', sep='\t', encoding='utf-16')
    df_koto = pd.read_csv('sc_koto.csv', sep='\t', encoding='utf-16')
    df_meguro = pd.read_csv('sc_meguro.csv', sep='\t', encoding='utf-16')
    df_minato = pd.read_csv('sc_minato.csv', sep='\t', encoding='utf-16')
    # df_mitaka = pd.read_csv('sc_mitaka.csv', sep='\t', encoding='utf-16')
    # df_musashino = pd.read_csv('sc_musashino.csv', sep='\t', encoding='utf-16')
    df_nakano = pd.read_csv('sc_nakano.csv', sep='\t', encoding='utf-16')
    df_nerima = pd.read_csv('sc_nerima.csv', sep='\t', encoding='utf-16')
    df_ota = pd.read_csv('sc_ota.csv', sep='\t', encoding='utf-16')
    df_setagaya = pd.read_csv('sc_setagaya.csv', sep='\t', encoding='utf-16')
    df_shibuya = pd.read_csv('sc_shibuya.csv', sep='\t', encoding='utf-16')
    df_shinagawa = pd.read_csv('sc_shinagawa.csv', sep='\t', encoding='utf-16')
    df_shinjuku = pd.read_csv('sc_shinjuku.csv', sep='\t', encoding='utf-16')
    df_suginami = pd.read_csv('sc_suginami.csv', sep='\t', encoding='utf-16')
    df_sumida = pd.read_csv('sc_sumida.csv', sep='\t', encoding='utf-16')
    # df_tachikawa = pd.read_csv('sc_tachikawa.csv', sep='\t', encoding='utf-16')
    df_taito = pd.read_csv('sc_taito.csv', sep='\t', encoding='utf-16')
    df_toshima = pd.read_csv('sc_toshima.csv', sep='\t', encoding='utf-16')
    df = pd.concat(
        [df_adachi, df_arakawa, df_bunkyo, df_chiyoda, df_chuo, df_edogawa, df_itabashi, df_katsushika, df_kita,
         df_koto, df_meguro, df_minato, df_nakano, df_nerima, df_ota, df_setagaya, df_shibuya, df_shinagawa,
         df_shinjuku, df_suginami, df_sumida, df_taito, df_toshima], axis=0, ignore_index=True)
    df.drop(['Unnamed: 0'], axis=1, inplace=True)
    return df


def format_location_summary(data):
    split_location0 = data['locations0'].str.split(' 歩', expand=True)
    split_location0.columns = ['locations_A', 'locations_A_min']
    split_location1 = data['locations1'].str.split(' 歩', expand=True)
    split_location1.columns = ['locations_B', 'locations_B_min']
    split_location2 = data['locations2'].str.split(' 歩', expand=True)
    split_location2.columns = ['locations_C', 'locations_C_min']
    new_df = pd.concat([data, split_location0, split_location1, split_location2], axis=1)
    new_df.drop(['locations0', 'locations1', 'locations2'], axis=1, inplace=True)
    return new_df


def format_location_detail(data):
    split_location_a = data['locations_A'].str.split('/', expand=True)
    split_location_a.columns = ['locations_A_path', 'locations_A_station']
    split_location_b = data['locations_B'].str.split('/', expand=True)
    split_location_b.columns = ['locations_B_path', 'locations_B_station']
    split_location_c = data['locations_C'].str.split('/', expand=True)
    split_location_c.columns = ['locations_C_path', 'locations_C_station']
    new_df = pd.concat([data, split_location_a, split_location_b, split_location_c], axis=1)
    new_df.drop(['locations_A', 'locations_B', 'locations_C'], axis=1, inplace=True)
    return new_df


def format_string_encode(data):
    # 不要な文字列を除去し、数字のみに変換
    data['rent'] = data['rent'].str.replace(u'万円', u'')
    data['deposit'] = data['deposit'].str.replace(u'万円', u'')
    data['gratuity'] = data['gratuity'].str.replace(u'万円', u'')
    data['admin'] = data['admin'].str.replace(u'円', u'')
    data['age'] = data['age'].str.replace(u'新築', u'0')
    data['age'] = data['age'].str.replace(u'築', u'')
    data['age'] = data['age'].str.replace(u'年', u'')
    data['area'] = data['area'].str.replace(u'm', u'')
    data['locations_A_min'] = data['locations_A_min'].str.replace(u'分', u'')
    data['locations_B_min'] = data['locations_B_min'].str.replace(u'分', u'')
    data['locations_C_min'] = data['locations_C_min'].str.replace(u'分', u'')
    # 「-」を0に変換
    df['admin'] = df['admin'].replace('-', 0)
    df['deposit'] = df['deposit'].replace('-', 0)
    df['gratuity'] = df['gratuity'].replace('-', 0)
    # 文字列から数値に変換
    df['rent'] = pd.to_numeric(df['rent'])
    df['admin'] = pd.to_numeric(df['admin'])
    df['deposit'] = pd.to_numeric(df['deposit'])
    df['gratuity'] = pd.to_numeric(df['gratuity'])
    df['age'] = pd.to_numeric(df['age'])
    df['area'] = pd.to_numeric(df['area'])
    df['locations_A_min'] = pd.to_numeric(df['locations_A_min'])
    df['locations_B_min'] = pd.to_numeric(df['locations_B_min'])
    df['locations_C_min'] = pd.to_numeric(df['locations_C_min'])
    # 単位を合わせるために、管理費以外を10000倍。
    df['rent'] = df['rent'] * 10000
    df['deposit'] = df['deposit'] * 10000
    df['gratuity'] = df['gratuity'] * 10000
    return data


def format_monthly_pay(data):
    data['monthly_payment'] = data['rent'] + data['admin']
    return data


def format_address(data):
    split_address = data['address'].str.split('区', expand=True)
    split_address.columns = ['pref', 'city']
    split_address['pref'] = split_address['pref'] + '区'
    split_address['pref'] = split_address['pref'].str.replace(u'東京都', '')
    data = pd.concat([data, split_address], axis=1)
    return data


def format_building(data):
    # 部屋の階数を整形
    split_floor = data['floor'].str.split('-', expand=True)
    split_floor.columns = ['floor1', 'floor2']
    split_floor['floor1'] = split_floor['floor1'].str.replace(u'階', u'')
    split_floor['floor1'] = split_floor['floor1'].str.replace(u'B', u'-')
    split_floor['floor1'] = pd.to_numeric(split_floor['floor1'])
    data = pd.concat([data, split_floor], axis=1)
    # heightを数値化。地下は無視。
    data['height'] = data['height'].str.replace(u'地下1地上', u'')
    data['height'] = data['height'].str.replace(u'地下2地上', u'')
    data['height'] = data['height'].str.replace(u'地下3地上', u'')
    data['height'] = data['height'].str.replace(u'地下4地上', u'')
    data['height'] = data['height'].str.replace(u'地下5地上', u'')
    data['height'] = data['height'].str.replace(u'地下6地上', u'')
    data['height'] = data['height'].str.replace(u'地下7地上', u'')
    data['height'] = data['height'].str.replace(u'地下8地上', u'')
    data['height'] = data['height'].str.replace(u'地下9地上', u'')
    data['height'] = data['height'].str.replace(u'平屋', u'1')
    data['height'] = data['height'].str.replace(u'階建', u'')
    data['height'] = pd.to_numeric(data['height'])
    # indexを振り直す（これをしないと、以下の処理でエラーが出る）
    data = data.reset_index(drop=True)
    # 間取りを「部屋数」「DK有無」「K有無」「L有無」「S有無」に分割
    data['floor_plan_DK'] = 0
    data['floor_plan_K'] = 0
    data['floor_plan_L'] = 0
    data['floor_plan_S'] = 0
    data['floor_plan'] = data['floor_plan'].str.replace(u'ワンルーム', u'1')  # ワンルームを1に変換
    for x in range(len(data)):
        if 'DK' in data['floor_plan'][x]:
            data.loc[x, 'floor_plan_DK'] = 1
        elif 'K' in data['floor_plan'][x]:
            data.loc[x, 'floor_plan_K'] = 1
        elif 'L' in data['floor_plan'][x]:
            data.loc[x, 'floor_plan_L'] = 1
        elif 'S' in data['floor_plan'][x]:
            data.loc[x, 'floor_plan_S'] = 1
    data['floor_plan'] = data['floor_plan'].str.replace(u'DK', u'')
    data['floor_plan'] = data['floor_plan'].str.replace(u'K', u'')
    data['floor_plan'] = data['floor_plan'].str.replace(u'L', u'')
    data['floor_plan'] = data['floor_plan'].str.replace(u'S', u'')
    data['floor_plan'] = pd.to_numeric(data['floor_plan'])
    return data


def export_dataframe(data):
    # カラムを入れ替えて、csvファイルとして出力
    data = data[['name', 'address', 'pref', 'city', 'floor_plan', 'floor_plan_DK', 'floor_plan_K', 'floor_plan_L',
                 'floor_plan_S', 'age', 'height', 'floor1', 'area', 'monthly_payment', 'locations_A_path',
                 'locations_A_station', 'locations_A_min', 'locations_B_path', 'locations_B_station', 'locations_B_min',
                 'locations_C_path', 'locations_C_station', 'locations_C_min', 'rent', 'admin', 'deposit', 'gratuity']]
    data.to_csv('suumo_tokyo.csv', sep='\t', encoding='utf-16')


if __name__ == "__main__":
    pd.options.display.max_columns = None
    df = format()
    df = format_location_summary(df)
    df = format_location_detail(df)
    df = df.dropna(subset=['rent'])
    df = format_string_encode(df)
    df = format_monthly_pay(df)
    df = format_address(df)
    df = format_building(df)
    export_dataframe(df)
