init -999 python:

# Класс - работа со временем
    class Time(store.object):
        def __init__( self): # ELog:
            self.__stamp=10000
            return

        def __call__( self):
            return self.stamp


        def Day(self, stamp=None):
            if (stamp==None):
                stamp=self.stamp
            return stamp//10000

        def Hour(self, stamp=None):
            if (stamp==None):
                stamp=self.stamp
            return (stamp-self.Day(stamp)*10000)//100

        def Minute(self, stamp=None):
            if (stamp==None):
                stamp=self.stamp
            return stamp-self.Day(stamp)*10000-self.Hour(stamp)*100

        def AddTime(self, delta):
            self.__min=self.__stamp=(self.Day()*24+self.Hour()*60+self.Minute())+(self.Day(delta)*24+self.Hour(delta)*60+self.Minute(delta))
            self.__hour=self.__min//60
            self.stamp=(self.__hour//24)*10000+(self.__hour-(self.__hour//24)*24)*100+(self.__min-(self.__hour*60))



        def IsPassed(self, oldstamp, interval, intervalType="h"):
            self.__min=(self.Day(self.stamp)-self.Day(oldstamp))*24*60+(self.Hour(self.stamp)-self.Hour(oldstamp))*60+(self.Minute(self.stamp)-self.Minute(oldstamp))
            if intervalType=="m":
                return self.__min>=interval
            elif intervalType=="h":
                return self.__min/60>=interval
            elif intervalType=="d":
                return self.__min/(24*60)>=interval
            return None

        def IsAllFinishedAgo(self, interval, intervalType="h", scenario=None, points=None ):
            return self.IsPassed(this.GetTime("finish2",scenario, points), interval, intervalType)

        def IsAllStartedAgo(self, interval, intervalType="h", scenario=None, points=None ):
            return self.IsPassed(this.GetTime("start2",scenario, points), interval, intervalType)

        
        @property
        def stamp(self): # Можно было бы в минуты переводить, но тогда визуально читается хуже при отладке
            return self.__stamp


