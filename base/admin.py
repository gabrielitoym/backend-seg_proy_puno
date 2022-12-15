from django.contrib import admin

# Register your models here.

from .models import Note
admin.site.register(Note)


from .models import Empleado
admin.site.register(Empleado)

from .models import Proyecto
admin.site.register(Proyecto)

from .models import Sector
admin.site.register(Sector)

from .models import Estado_Inversion
admin.site.register(Estado_Inversion)

from .models import Tipo
admin.site.register(Tipo)

from .models import ciudad
admin.site.register(ciudad)

from .models import UEI
admin.site.register(UEI)

from .models import Modalidad_Ejecucion
admin.site.register(Modalidad_Ejecucion)

from .models import Beneficiario
admin.site.register(Beneficiario)