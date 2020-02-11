#exemplo de requestId: https://<region>.api.riotgames.com/lol/summoner/v4/summoners/by-name/<summonerName>?api_key=<APIkey>
import requests

def requestPlayerId(region, summonerName, APIkey):
    URL = "https://" + region + ".api.riotgames.com/lol/summoner/v4/summoners/by-name/" + summonerName + "?api_key=" + APIkey

    response = requests.get(URL)

    return  response.json()

#exemplo de requestInfo: https://<region>.api.riotgames.com/lol/league/v4/entries/by-summoner/<ID>?api_key=<APIkey>
def requestPlayerInfo(region, ID, APIkey):
    URL = "https://" + region + ".api.riotgames.com/lol/league/v4/entries/by-summoner/" + ID + "?api_key=" + APIkey

    response = requests.get(URL)

    return response.json()

def main():
    print("[BR1/NA1/EUW1/EUNE/LAN/LAS/KR/OCE/TR/RU/PBE]")

    region = input("Insira sua região: ")
    summonerName = input("Insira seu Nickname: ")
    APIkey = input('Insira sua API key: ')

    responseJSON = requestPlayerId(region, summonerName, APIkey)
    
    ID = responseJSON['id']
    ID = (ID)

    responseJSON_2 = requestPlayerInfo(region, ID, APIkey)

    print("Nickname: ", responseJSON_2[0]['tier'])
    print("Elo: ", responseJSON_2[0]['tier'])
    print("tier: ", responseJSON_2[0]['rank'])
    print("pontos: ",  responseJSON_2[0]['leaguePoints'])
    print("vitórias: ", responseJSON_2[0]['wins'])
    print("derrotas: ", responseJSON_2[0]['losses'])
    
if __name__ == "__main__":
    main()
    
