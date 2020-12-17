from config.wsgi import *
from core.arp.models import *

data = ['Leche y derivados', 'Carnes, pescado y huevos', 'Patatas', 'Legumbres', 'frutos secos', 'Zanahorias', 'Verduras y Hortalizar', 'Frutas' 'Cereales y derivados, azúcar y dulces', 'Grasas, aceites y mantequilla']

for i in data:
    cat = Category(name=i)
    cat.save()
    print('Guardando registro No {}'.format(cat.id))

