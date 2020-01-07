import requests 

champlist = {}
game_champ = {}
api_key = "RGAPI-83ecfc71-e71d-4c2e-82e9-c710892bdea3"
# mysummoner = input("Enter Summoner Name: ")

# summoner = requests.get('https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/'+mysummoner+'?api_key='+api_key)
summoner = requests.get(
    'https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/trollmerito?api_key=' + api_key)
champ = requests.get('http://ddragon.leagueoflegends.com/cdn/9.11.1/data/en_US/champion.json')

#print(summoner.text)

account = summoner.json()['accountId']
# print(account)

matches = requests.get(
    'https://euw1.api.riotgames.com/lol/match/v4/matchlists/by-account/' + account + '?api_key=' + api_key)

#print("\n\n\n", matches.json())

platform = matches.json()["matches"]
mychamp = champ.json()['data']

#print("\n\n\n", platform[1])
#print("\n\n\n", "gameId: ", platform[1]["gameId"])


for i in platform:
    print("gameId:", i["gameId"], "champion:", i["champion"])
    game_champ = (i["champion"])
    print(game_champ)

# print("\n\n\n", champ.text)
#print("\n\n\n", champ.json())



#print("\n\n\n", mychamp)


for key in mychamp:
    print(mychamp[key]['id'], ": ", mychamp[key]['key'])
    champlist[mychamp[key]['id']] = {mychamp[key]['key']}



print(mychamp['Sylas'])


#for key, value in mychamp.items():
#    if value == '517':
#        print(key)

print("\n\n\n")
print(champlist.items())

#print(champlist.keys())
#print(champlist.values())

#print(game_champ)
