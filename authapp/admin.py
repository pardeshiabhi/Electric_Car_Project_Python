from django.contrib import admin

# Register your models here.
from .models import Contact,Carbooking,CarType,Selectcarbrand

from .models import Carrenting,rentingType,carbrand

from .models import Services,About,Team
#booking
admin.site.register(Contact)
admin.site.register(Selectcarbrand)
admin.site.register(CarType)
admin.site.register(Carbooking)


#renting
admin.site.register(Carrenting)
admin.site.register(rentingType)
admin.site.register(carbrand)

#services
admin.site.register(Services)

#about
admin.site.register(About)

#team
admin.site.register(Team)
