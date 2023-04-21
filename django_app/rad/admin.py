from django.contrib import admin

from .models import Traders
from .models import Distros
from .models import TraderToDistro
from .models import DistroCurrentData

# Adds the different models to the admin site to allow direct edit of the data and deletion
admin.site.register(Traders)
admin.site.register(Distros)
admin.site.register(TraderToDistro)
admin.site.register(DistroCurrentData)
