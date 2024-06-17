import requests
# Sol·licita el nom de la ciutat
#ciutat=input("Indiqui el nom de la ciutat:")
# Cream un diccionari amb les dades de la petició
parametres={"access_key":"9d39e29bff4eb2841c644d72789c3bac",
   		 "symbols":"AENA.BMEX"}
# Fem la petició indicant l'url i els paràmetres
res=requests.get("http://api.marketstack.com/v1/eod",params=parametres)
# Si retorna el codi d'estat 200, ha anat bé i podem fer feina, si no sortim
if res.status_code == 200:
    # Convertim la resposta JSON en un diccionari
    dades = res.json()
    # Imprimir els valors del diccionari que volem
    for e in dades["data"]:
        print("El canvi de:", dades["data"][0]["exchange"])
        print("Ha obert a:", dades["data"][0]["open"],"€")
        print("Ha tancat a:", dades["data"][0]["close"],"€")
        print("Dia:", dades["data"][0]["date"])
else:
    print("No hi ha dades d'aquesta empresa.")
