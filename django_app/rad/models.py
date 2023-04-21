from django.db import models
from django.utils import timezone

class Traders(models.Model):
    trader_name = models.CharField(max_length=200)
    
    def __str__(self):
        return "%s"%(self.trader_name)
    
class Distros(models.Model):
    distro_location = models.CharField(max_length=200)
    socket_count = models.IntegerField(default=0)
    
    def __str__(self):
        return "%s @ %s"%(self.id,self.distro_location)

class TraderToDistro(models.Model):
    trader = models.ForeignKey(Traders, on_delete=models.CASCADE)
    distro = models.ForeignKey(Distros, on_delete=models.CASCADE)
    socket_number = models.IntegerField(default=0)
    start_time = models.DateField(default=timezone.now)

class DistroCurrentData(models.Model):
    distroID = models.IntegerField()
    socketNum = models.IntegerField()
    currentValue = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Distro %s, Socket %s, Current %sA @ %s"%(self.distroID,self.socketNum, self.currentValue, self.timestamp)

