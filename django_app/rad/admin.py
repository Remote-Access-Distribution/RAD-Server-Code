from django.contrib import admin

from .models import Traders
from .models import Distros
from .models import TraderToDistro
from .models import DistroCurrentData

admin.site.register(Traders)
admin.site.register(Distros)
admin.site.register(TraderToDistro)
admin.site.register(DistroCurrentData)
