import requests


#exemplo de requestId: https://<region>.api.riotgames.com/lol/summoner/v4/summoners/by-name/<summonerName>?api_key=<APIkey>
def requestPlayerId(region, summonerName, APIkey):
    #partindo das informações dadas, buscar arquivo em JSON
    URL = "https://" + region + ".api.riotgames.com/lol/summoner/v4/summoners/by-name/" + summonerName + "?api_key=" + APIkey

    response = requests.get(URL)

    return  response.json()

#exemplo de requestInfo: https://<region>.api.riotgames.com/lol/league/v4/entries/by-summoner/<ID>?api_key=<APIkey>
def requestPlayerInfo(region, ID, APIkey):
    #partindo das informações dadas, buscar arquivo em JSON
    URL = "https://" + region + ".api.riotgames.com/lol/league/v4/entries/by-summoner/" + ID + "?api_key=" + APIkey

    response = requests.get(URL)

    return response.json()

#retornando informações sobre o inGame do player
def selectedRankedStatus(region, ID, APIkey):
  #partindo das informações dadas, buscar: Nome, tier, ranked, pontos, vitórias e derrotas.
  responseRanked = requestPlayerInfo(region, ID, APIkey)
  
  print("Nickname: ", responseRanked[0]['summonerName'])
  print("Elo: ", responseRanked[0]['tier'])
  print("tier: ", responseRanked[0]['rank'])
  print("pontos: ",  responseRanked[0]['leaguePoints'])
  print("vitórias: ", responseRanked[0]['wins'])
  print("derrotas: ", responseRanked[0]['losses'])

  #retornando valor da função 
  return selectedRankedStatus

#função main
def main():
    #expor regiões disponíveis ao acesso
    print("[BR1/NA1/EUW1/EUNE/LAN/LAS/KR/OCE/TR/RU/PBE]")

    #definindo região, nome e API key do usuário
    region = input("Insira sua região: ")
    summonerName = input("Insira seu Nickname: ")
    APIkey = input('Insira sua API key: ')

    #partindo das informações dadas, então o programa executa a função requestPlayerId, aqui definida também como responseJSON
    responseJSON = requestPlayerId(region, summonerName, APIkey)
    
    #definir o ID da conta informada partindo da informação de requestPlayerId
    ID = responseJSON['id']
    ID = (ID)

    #perguntar se o usuário deseja ver seus status
    answer = input("Deseja ver seus Status inGame? [Insira 0 or 1]\n")

    #caso o jogador desejar ver seus status, então ir para a função selectedRankedStatus
    if answer == '1':
      selectedRankedStatus(region, ID, APIkey)  
    #senão, imprimir mensagem de despedida
    else:
      print("Finalizando programa") 



    
if __name__ == "__main__":
    main()
