from consumir_api import request_get
from cards_template import cards
from html_template import html
from transformar_html import python_html

# Se obtiene la informacion de la API reformateada a JSON con la funcion "request_get"
results = request_get('https://aves.ninjas.cl/api/birds')

# Se iteran los elementos de la API separados
lista_aves_esp = [elemento['name']['spanish'] for elemento in results]
lista_aves_ing = [elemento['name']['english'] for elemento in results]
img_aves = [elemento['images']['full'] for elemento in results]

# Se arman las cards con la funcion "cards"
contenido = cards(lista_aves_esp, lista_aves_ing, img_aves)

# Se arma el html con la funcion "html_template"
template_html = html(contenido)

# Se crea archivo html "index" con funcion "python_html"
python_html(template_html)