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

def requestCurrentMatchInfo(region, ID, APIkey):
    URL = "https://" + region + ".api.riotgames.com/lol/spectator/v4/active-games/by-summoner/" + ID + "?api_key=" + APIkey
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

def currentMatchInfo(region, ID, APIkey):
   responseMatchInfo = requestCurrentMatchInfo(region, ID, APIkey)
   
   print(responseMatchInfo)
   print("Modo de jogo: ", responseMatchInfo['gameType'])
   print("Jogador 1: ", responseMatchInfo['participants'][0]['summonerName'])
   print("Jogador 2: ", responseMatchInfo['participants'][1]['summonerName'])
   print("Jogador 3: ", responseMatchInfo['participants'][2]['summonerName'])
   print("Jogador 4: ", responseMatchInfo['participants'][3]['summonerName'])
   print("Jogador 5: ", responseMatchInfo['participants'][4]['summonerName'])
   print("Jogador 6: ", responseMatchInfo['participants'][5]['summonerName'])
   print("Jogador 7: ", responseMatchInfo['participants'][6]['summonerName'])
   print("Jogador 8: ", responseMatchInfo['participants'][7]['summonerName'])
   print("Jogador 9: ", responseMatchInfo['participants'][8]['summonerName'])
   print("Jogador 10: ", responseMatchInfo['participants'][9]['summonerName'])
   return currentMatchInfo



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
    print(" \n")
    print("Deseja ver informações seu Match Ativo? (Requer que você esteja inGame) [1]\n")
    answer = input("Deseja ver seus Status da Ranked? [2]\n")

   
    #se o usuário não quiser, imprimir mensagem de despedida   
    if answer == '0':
     print("Finalizando programa")
    #caso o usuário desejar, imprimir informações sobre seu Rank/Game ativo chamando a função currentMatchInfo/selectedRankedStatus
    elif answer == '1':
      currentMatchInfo(region, ID, APIkey)
    elif answer == '2':
      selectedRankedStatus(region, ID, APIkey)
    #caso o número não corresponda a nenhum dos casos, imprimir mensagem de despedida
    else:
      print("Finalizando programa")

    
if __name__ == "__main__":
    main()
