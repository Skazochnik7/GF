init -998 python:
  
# Класс - обертка для словаря ивентов
    class EventCollection(store.object):
        def __init__( self): # ELog:
            scenario=None
            points={}
            self.List=[] # Упорядоченный список ивентов.
            
# Можно вызвать eco("Name") и получить ивент "Name",
# Если вызвать с параметром None - получим саму коллекцию (полезно, если обращаться через лямбду)
        def __call__( self, sName=None):
            return self.GetCall(sName)

        def GetCall( self, sName=None):
            if sName==None:
                return self
           
            for e in self.List:
                if e.Name==sName:
                    return e

            return None


#        def InitStart( self ):
#            for e in self.List:
#                e.InitStart()

#        def InitTempVars(self):                
#            for e in self.List:
#                e.InitTempVars()

        def Where(self,points, scenario=""):
            self.scenario=scenario
# Необходимо делать копию, иначе скопируется просто ссылка на объект            
            self.points=points.copy()
            return self

# Внимание! Не проверяется на наличие в списке одноименных! Необходимо внимательно описывать секцию Init
        def AddStep( self, sFullName, weight=0, ready=None, done=None, defVals=None, constVals=None):
# Необходимо делать копию, иначе скопируется просто ссылка на объект            
            self.AddEvent(sFullName, weight, self.scenario, self.points.copy(), ready, done, defVals, constVals)


# Внимание! Не проверяется на наличие в списке одноименных! Необходимо внимательно описывать секцию Init
        def AddEvent( self, sFullName, weight=0, scenario=None, points={}, ready=None, done=None, defVals=None, constVals=None):
            prev=None
            prevInList=None

            if len(self.List)>0:
                prevInList=self.List[len(self.List)-1]

            if scenario!=None:
                for e in self.List:
                    if e.GetValue("scenario")==scenario:
                        prev=e

            self.List.append(RegEntry(Event(sFullName, weight, scenario, points, ready, done, defVals, constVals)))
# Нужно ставить не max(self.List), а self.List[len(self.List)-1] , max почему-то выдает предыдущее значение    ?!
            if prev!=None: prev.next=self.List[len(self.List)-1]
            self.List[len(self.List)-1].prev=prev
            self.List[len(self.List)-1].prevInList=prevInList
            
            return self.List[len(self.List)-1]



# Был ли завершен ивент (установлен флаг завершения)? Как параметр можно подать имя или альтернативное имя
        def Has( self, sName):
            return self.GetCall(sName).IsDone()


# Поскольку список ивентов создается в блоке инит, порядок следования ивентов жестко зафиксирован
# Если несколько ивентов могут запускаться в одной и той же точке, запустится тот, который был добавлен раньше (по движении по списку запускается первый ивент, который удовлетворяет условиям)
# Смысл сценария - связать события в одну нить. Если события в одном сенарии, последующее не может запуститься, пока не выполнено (IsDone) предыдущее.
        def GetSteps(self, point):
            __arr=[]
            for e in self.List:
                 if (point in e._points) and e.IsActive() and e._scenario!=None:
                    __arr.append(e)
#                        return e

            return __arr

        def IsStep(self, point):
            return self.GetSteps(point) != []

# Исполнить шаг (если есть готовый для исполнения)
        def RunStep(self, point):
            if self.IsStep(point):
                __arr = self.GetSteps(point)
                __arr1=[] # Есть вероятности исполнения, но может ни один не исполниться
                __arr2=[] # Хотя бы один исполнится обязательно 
                for e in __arr:
                    if (e._weight==0):
                        __arr2.append(e)
                    else: 
                        __arr1.append(e)

                r=1.0 # Вероятность отрицательного исхода
                m=0 # Сумма вероятностей положительных исходов (для нормирирования)
                for e in __arr1:
                    r=r*(100-e._weight)/100
                    m+=e._weight

                debug.SaveString(str(len(__arr1))+" "+str(len(__arr2))+" "+" "+str(r)+" "+str(m))

                v=Rand(10000) 
                debug.SaveString(str(v))
                if v>(1-r)*10000:
                    debug.SaveString(str((1-r)*10000))
                    if __arr2!=None:
                        __arr2[Rand(len(__arr2))-1].Run()
                else:
                    if __arr1!=[]:
                        v=Rand(m)
                        debug.SaveString(str(v))
                        for e in __arr1:
                            v-=e._weight
                            debug.SaveString(str(v))
                            if v<=0:
                                e.Run()
                                break
            return


                


        def GetTime(self, sStartFinishMode, scenario=None, points=None):
            self.__stamp=0
            for e in self.List:
                debug.SaveString(e.Name+": "+str(e._scenario)+" "+str(e._points))
                if scenario==None or scenario==e._scenario:
                    if points==None or points.intersection(e._points)!={}:
                        if e.GetValue(sStartFinishMode+"Time")>self.__stamp:
#                            debug.SaveString(e.Name+": "+str(e.GetValue(what+"Time")))
                            self.__stamp=e.GetValue(sStartFinishMode+"Time")
            return self.__stamp








