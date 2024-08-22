import numpy as np

class Car:
    def __init__(self, number, name, engine, wheel, wings, rightDistribution, frontDistribution, entreEixos, trackF, trackR, chassiWeight, weight, fuel, position):
        self.name = name
        self.number = number
        self.engine = engine
        self.wheel = wheel
        self.wings = wings
        self.rightDistribution = rightDistribution 
        self.frontDistribution = frontDistribution
        self.entreEixos = entreEixos
        self.trackF = trackF
        self.trackR = trackR
        self.chassiWeight = chassiWeight
        self.weight = weight
        self.fuel = fuel
        self.position = position        

        self.acceleration = Acceleration()
        self.skidPad = SkidPad()
        self.autoX = AutoX()
        self.efficiency = Efficiency(None,None,None,0)
        self.enduro = Enduro(None,0,0,0,0,0)

    def getCorrectedAccelTimes(self):
        correctedTimes = []
        runs = {}
        for number,run in enumerate(self.acceleration.runs):
            if run is not None:
                runs[number] = run
            else:
                runs[number] = None
        for index in runs.keys():
            if runs[index] is not None:
                correctedTimes.append(runs[index]+2*self.acceleration.cones[index])
            else:
                correctedTimes.append(None)
        return correctedTimes

    def getCorrectedSkidTimes(self):
        correctedTimes = []
        runs = {}
        for number,vector in enumerate(self.skidPad.runs):
            if vector is not None and None not in vector:
                runs[number] = np.mean(vector)
            else:
                runs[number] = None
        for index in runs.keys():
            if runs[index] is not None:
                correctedTimes.append(runs[index]+0.125*self.skidPad.cones[index])
            else:
                correctedTimes.append(None)
        return correctedTimes
    
    def getCorrectedAutoXTimes(self):
        correctedTimes = []
        runs = {}
        for number,run in enumerate(self.autoX.runs):
            if run is not None:
                runs[number] = run
            else:
                runs[number] = None
        for index in runs.keys():
            if runs[index] is not None:
                correctedTimes.append(runs[index]+2*self.autoX.cones[index]+20*self.autoX.offCourses[index])
            else:
                correctedTimes.append(None)
        return correctedTimes

    

    def getBestAccelTime(self):
        valid_vectors = [vector for vector in self.getCorrectedAccelTimes() if vector is not None]
        return min(valid_vectors)
    
    def getBestSkidPadTime(self):
        valid_vectors = [vector for vector in self.getCorrectedSkidTimes() if vector is not None]
        return min(valid_vectors)
    
    def getBestAutoXTime(self):
        valid_vectors = [vector for vector in self.getCorrectedAutoXTimes() if vector is not None]
        return min(valid_vectors)
    
    def getEnduroTotalTime(self):
        return self.enduro.total_time + 2*self.enduro.cones + 20 *self.enduro.off_courses + self.enduro.penalities
    
    def getDesignScores(self):
        return [self.design.suspension, self.design.frame, self.design.engine, self.design.transmission, self.design.brakes, self.design.electronics, self.design.management]

    def getCostScores(self):
        return [self.cost.report,self.cost.real_case,self.cost.manufacture,self.cost.cost,abs(self.cost.penalitiesProva)]


    def getTotalDesignScore(self):
            return sum(self.getDesignScores())
    
    def getPointsDistribution(self):
        return {
            "design":self.design.total_points/self.getFinalScore(),
            "cost":self.cost.points/self.getFinalScore(),
            "business":self.business.score/self.getFinalScore(),
            "acceleration":self.acceleration.score/self.getFinalScore(),
            "skidpad":self.skidPad.score/self.getFinalScore(),
            "autoX":self.autoX.score/self.getFinalScore(),
            "enduro":self.enduro.points/self.getFinalScore(),
            "efficiency":self.efficiency.score/self.getFinalScore()
        }
    def getAllPoints(self):
        return {
            "design":self.design.total_points,
            "cost":self.cost.points,
            "business":self.business.score,
            "acceleration":self.acceleration.score,
            "skidpad":self.skidPad.score,
            "autoX":self.autoX.score,
            "enduro":self.enduro.points,
            "efficiency":self.efficiency.score
        }


    def getFinalScore(self):
        return sum([self.design.total_points,self.cost.points,self.business.score,self.acceleration.score,self.skidPad.score,self.autoX.score,self.enduro.points,self.efficiency.score])
    
    def getDynamicScore(self):
        return sum([self.acceleration.score,self.skidPad.score,self.autoX.score,self.enduro.points,self.efficiency.score])

class Cost:
    def __init__(self,preco,relatorio,realCase,Manufatura,custo,penalidadeProva,penalidadeRelatorio,pontos):
        self.price = preco
        self.report = relatorio
        self.real_case = realCase
        self.manufacture = Manufatura
        self.cost = custo
        self.penalitiesProva = penalidadeProva
        self.penaltiesRelatorio = penalidadeRelatorio
        self.points = pontos

class Design:
    def __init__(self,suspension,frame,engine,transmission,brakes,electronics,management,penalties_test,penalties_report,total_points):
        self.suspension = suspension
        self.frame = frame
        self.engine = engine
        self.transmission = transmission
        self.brakes = brakes
        self.electronics = electronics
        self.management = management
        self.penalties_test = penalties_test
        self.penalties_report = penalties_report
        self.total_points = total_points


class Business:
    def __init__(self,penalties_test,penalties_report,score):
        self.score = score
        self.penalties_test = penalties_test
        self.penalties_report = penalties_report


class Acceleration:
    def __init__(self):
        self.runs = [None] * 4
        self.cones = [None] * 4
        self.score = 0

class SkidPad:
    def __init__(self):
        self.runs = [[None,None]] * 4
        self.cones = [None] * 4
        self.score = 0

class AutoX:
    def __init__(self):
        self.runs = [None] * 4
        self.cones = [None] * 4
        self.offCourses = [None]*4
        self.score = 0

class Efficiency:
    def __init__(self,avgTime,laps,consumed,points):
        self.avg_time = avgTime
        self.laps = laps
        self.consumed = consumed
        self.score = points

class Enduro:
    def __init__(self,totalTime,laps,cones,off_courses,pennalities,points):
        self.laps = laps
        self.total_time = totalTime
        self.cones = cones
        self.off_courses = off_courses
        self.penalities = pennalities
        self.points = points
        self.lap_times = []




