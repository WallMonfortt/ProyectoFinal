from email.policy import default
from pydoc import pager
from rest_framework import pagination


class CustomPagination(pagination.PageNumberPagination): 
    page_size = 2 # Cantidad de objetos por pagina
    page_size_query_param = 'page_size' # Parametro que se usa para cambiar la cantidad de objetos por pagina
    max_page_size = 50 # Maximo numero de objetos por pagina
    page_query_param = 'p' # Parametro que se usa para cambiar la pagina
