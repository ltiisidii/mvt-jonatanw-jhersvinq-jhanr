# Carga de familiares

Para cargar familia correr desde la terminal:

```
python manage.py shell

from appfamiliares.models import Familiar

familiar = Familiar(nombre="Pedro", apellido="Perez", relacion="Padre", edad="58", domicilio="Calle falsa 1234 - Ciudad Falsa")
familiar = Familiar(nombre="Rosa", apellido="Perez", relacion="Madre", edad="55", domicilio="Calle falsa 1234 - Ciudad Falsa")
familiar = Familiar(nombre="Lorena", apellido="Perez", relacion="Hija", edad="31", domicilio="Calle falsa 1234 - Ciudad Falsa")

familiar.save()

```
por ejemplo 

```
python manage.py shell

from appfamiliares.models import Familiar

familiar = Familiar(nombre="Pedro", apellido="Perez", relacion="Padre", edad="58", domicilio="Calle falsa 1234 - Ciudad Falsa")
familiar.save()
familiar = Familiar(nombre="Rosa", apellido="Perez", relacion="Madre", edad="55", domicilio="Calle falsa 1234 - Ciudad Falsa")
familiar.save()
familiar = Familiar(nombre="Lorena", apellido="Perez", relacion="Hija", edad="31", domicilio="Calle falsa 1234 - Ciudad Falsa")
familiar.save()

exit()
```

