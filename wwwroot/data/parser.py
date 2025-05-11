#!/usr/bin/python3

#https://api.hakush.in/gi/data/en/character/10000049.json
#filter: drop-shadow(0 0 0.75rem black);

import requests
import json
import os
import traceback
import time

c0_const = ['cyno', 'diluc', 'mona', 'nahida', 'nilou', 'qin', 'venti', 'wanderer', 'xiao', 'yaemiko', 'yelan', 'yoimiya', 'zhongli', 'eula', 'ganyu', 'hutao', 'itto', 'jean', 'kazuha', 'keqing', 'klee', 'kokomi', 'raiden', 'shenhe', 'shougun', 'tartaglia', 'qiqi', 'tighnari', 'albedo', 'ayaka', 'ayato', 'baizhu', 'alhaitham', 'lyney', 'neuvillette', 'furina', 'navia', 'wriothesley', 'xianyun', 'chiori', 'emilie', 'sigewinne', 'clorinde', 'arlecchino', 'mualani', 'kinich', 'chasca', 'xilonen', 'citlali', 'mavuika', 'athousandblazingsuns', 'starcallerswatch']

five_weapons = ['mistsplitterreforged', 'kagura', 'kagurasverity', 'redhornstonethresher', 'athousandfloatingdreams', 'thefirstgreatmagic', 'tomeoftheeternalflow', 'verdict', 'cranesechoingcall', 'urakumisugiri', 'silvershowerheartstrings', 'crimsonmoonssemblance', 'lumidouceelegy', 'absolution', 'astralvulturescrimsonplumage', 'peakpatrolsong', 'silvershowerheartstrings', 'surfsup', 'fangofthemountainking']

blacklist_teams = ['jn8qcb8TjjqK', 'JnDMB8gPQwLp', '69nzHHMNJ8cJ', 'n6n68DhqBmQc', 'mhHBcrhKKQGN']

limit = 100
offset = 0

main_api_url = 'https://simpact.app/api/db'
leaderboard = {}
end_of_list = False

while not end_of_list:
    print(f'Parsing offset = %d' % offset)
    params = {
    'q': json.dumps({"query":{},"limit":limit,"skip":offset}),
    }
    response = requests.get(main_api_url, params=params).json()
    if 'data' not in response: break
    teams = response['data']

    for team in teams:
        if team['_id'] in blacklist_teams:
            continue
        #if team['summary']['target_count'] > 1: continue
        chars = []
        chars_list = []

        brokenTeam = False
        if 'summary' not in team: continue
        team_info = team['summary']['team']
        for char in team_info:
            if (char['name'] in c0_const) and ('cons' in char):
                if char['cons'] > 0:
                    brokenTeam = True

                for talent in char['talents']:
                    if char['talents'][talent] > 9: brokenTeam = True


            if (char['weapon']['name'] in five_weapons):
                brokenTeam = True

            if char['name'] in c0_const:
                for talent in char['talents']:
                    if char['talents'][talent] > 9: brokenTeam = True

            char_info = {
                'name': char['name'],
                'weapon': char['weapon']['name'],
            }
            if 'sets' not in char:
                brokenTeam = True
            else:
                char_info['artifacts'] = [i for i in char['sets'] if char['sets'][i] > 1]

            chars.append(char_info)
            chars_list.append(char['name'])

            imgs_download = [
                [f'images/characters/{char_info["name"]}.png', f'https://simpact.app/api/assets/avatar/{char_info["name"]}.png'],
                [f'images/weapons/{char_info["weapon"]}.png', f'https://simpact.app/api/assets/weapons/{char_info["weapon"]}.png'],
            ]
            try:
                imgs_download.append(
                    [f'images/artifacts/{char_info["artifacts"][0]}.png', f'https://simpact.app/api/assets/artifacts/{char_info["artifacts"][0]}_flower.png']
                )
                imgs_download.append(
                    [f'images/artifacts/{char_info["artifacts"][1]}.png', f'https://simpact.app/api/assets/artifacts/{char_info["artifacts"][1]}_flower.png']
                )
            except:
                pass

            for img in imgs_download:
                if not os.path.isfile(img[0]):
                    open(img[0],'wb').write(requests.get(img[1]).content)


        if brokenTeam: continue

        name = team['summary']['char_names'].copy()
        name.sort()
        name = '-'.join(name)

        id = team['_id']
        desc = team['description']

        dps = team['summary']['mean_dps_per_target']

        if name not in leaderboard:
            leaderboard[name] = {
                'id': id,
                'desc': desc,
                'dps': dps,
                'characters': chars,
                'characters_list': chars_list
            }
        elif leaderboard[name]['dps'] < dps:
            leaderboard[name] = {
                'id': id,
                'desc': desc,
                'dps': dps,
                'characters': chars,
                'characters_list': chars_list
            }

    if len(teams) == limit:
        offset += limit
    else:
        end_of_list = True

leaderboard = dict(sorted(leaderboard.items(), key=lambda item: item[1]['dps']))
leaderboard = dict(reversed(list(leaderboard.items())))

open('db.json','w').write(json.dumps(leaderboard, indent=4))
