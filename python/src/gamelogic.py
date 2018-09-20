from shapely import geometry

class area():
    def __init__(self, level, fps):
        self.level=level
        self.fps=fps
        if level==1:
            self.frame=[(130,210),(130,390),(670,390),(670,210)]
            self.gridfactor=30
            self.sizeX=18
            self.sizeY=6
            self.o_speed=180/fps
            
            self.playingField=[(130,210),
                               (220,210),
                               (220,360),
                               (250,360),
                               (250,240),
                               (520,240),
                               (520,210),
                               (670,210),
                               (670,390),
                               (580,390),
                               (580,240),
                               (550,240),
                               (550,360),
                               (280,360),
                               (280,390),
                               (130,390)]
            
            self.startArea=[(130,210),
                            (220,210),
                            (220,390),
                            (130,390)]
            
            self.finishArea=[(580,210),
                             (670,210),
                             (670,390),
                             (580,390)]
            
            self.startingPos=(175,300)
            
            self.area_obj=geometry.polygon.Polygon(self.playingField)
            
            self.lightList=[]
            self.darkList=[]
            
            for i in range(self.sizeX):
                for j in range(self.sizeY):
                    rect=[(self.frame[0][0]+i*self.gridfactor,self.frame[0][1]+j*self.gridfactor),
                          (self.frame[0][0]+(i+1)*self.gridfactor,self.frame[0][1]+j*self.gridfactor),
                          (self.frame[0][0]+(i+1)*self.gridfactor,self.frame[0][1]+(j+1)*self.gridfactor),
                          (self.frame[0][0]+i*self.gridfactor,self.frame[0][1]+(j+1)*self.gridfactor)]
                    rect_obj=geometry.polygon.Polygon(rect)
                    if self.area_obj.contains(rect_obj):
                        if (i+j) % 2 == 0:
                            self.lightList.append(rect)
                        else:
                            self.darkList.append(rect)
        elif level==2:
            self.frame=[(130,210),(130,390),(670,390),(670,210)]
            self.gridfactor=30
            self.sizeX=18
            self.sizeY=6
            self.o_speed=180/fps
            
            self.playingField=[(130,270),
                               (130,330),
                               (220,330),
                               (220,390),
                               (580,390),
                               (580,330),
                               (670,330),
                               (670,270),
                               (580,270),
                               (580,210),
                               (220,210),
                               (220,270)]
            
            self.startArea=[(130,270),
                            (130,330),
                            (220,330),
                            (220,270)]
            
            self.finishArea=[(670,270),
                             (670,330),
                             (580,330),
                             (580,270)]
            
            self.startingPos=(175,300)
            
            self.area_obj=geometry.polygon.Polygon(self.playingField)
            
            self.lightList=[]
            self.darkList=[]
            
            for i in range(self.sizeX):
                for j in range(self.sizeY):
                    rect=[(self.frame[0][0]+i*self.gridfactor,self.frame[0][1]+j*self.gridfactor),
                          (self.frame[0][0]+(i+1)*self.gridfactor,self.frame[0][1]+j*self.gridfactor),
                          (self.frame[0][0]+(i+1)*self.gridfactor,self.frame[0][1]+(j+1)*self.gridfactor),
                          (self.frame[0][0]+i*self.gridfactor,self.frame[0][1]+(j+1)*self.gridfactor)]
                    rect_obj=geometry.polygon.Polygon(rect)
                    if self.area_obj.contains(rect_obj):
                        if (i+j) % 2 == 0:
                            self.lightList.append(rect)
                        else:
                            self.darkList.append(rect)
                            
        elif level==3:
            self.frame=[(340,210),(460,210),(460,360),(340,360)]
            self.gridfactor=30
            self.sizeX=4
            self.sizeY=5
            self.o_speed=60/fps
            
            self.playingField=[(340,210),
                               (370,210),
                               (370,240),
                               (460,240),
                               (460,360),
                               (340,360)]
            
            self.startArea=[(370,270),
                            (430,270),
                            (430,330),
                            (370,330)]
            
            self.finishArea=[(370,270),
                             (430,270),
                             (430,330),
                             (370,330)]
            
            self.startingPos=(400,300)
            
            self.area_obj=geometry.polygon.Polygon(self.playingField)
            
            self.lightList=[]
            self.darkList=[]
            
            for i in range(self.sizeX):
                for j in range(self.sizeY):
                    rect=[(self.frame[0][0]+i*self.gridfactor,self.frame[0][1]+j*self.gridfactor),
                          (self.frame[0][0]+(i+1)*self.gridfactor,self.frame[0][1]+j*self.gridfactor),
                          (self.frame[0][0]+(i+1)*self.gridfactor,self.frame[0][1]+(j+1)*self.gridfactor),
                          (self.frame[0][0]+i*self.gridfactor,self.frame[0][1]+(j+1)*self.gridfactor)]
                    rect_obj=geometry.polygon.Polygon(rect)
                    if self.area_obj.contains(rect_obj):
                        if (i+j) % 2 == 0:
                            self.lightList.append(rect)
                        else:
                            self.darkList.append(rect)
        self.obstacles=self.generateObstacles(self.o_speed, self.level)
        self.coins=self.generateCoins(self.level)
    
    def generateObstacles(self, o_speed, level):
        if level==1:
            return [obstacle(7,(265,255),[(1,0),(-1,0)],[270,270],o_speed),
                    obstacle(7,(535,285),[(-1,0),(1,0)],[270,270],o_speed),
                    obstacle(7,(265,315),[(1,0),(-1,0)],[270,270],o_speed),
                    obstacle(7,(535,345),[(-1,0),(1,0)],[270,270],o_speed)]
        elif level==2:
            return [obstacle(7,(235,375),[(0,-1),(0,1)],[150,150],o_speed),
                    obstacle(7,(265,225),[(0,1),(0,-1)],[150,150],o_speed),
                    obstacle(7,(295,375),[(0,-1),(0,1)],[150,150],o_speed),
                    obstacle(7,(325,225),[(0,1),(0,-1)],[150,150],o_speed),
                    obstacle(7,(355,375),[(0,-1),(0,1)],[150,150],o_speed),
                    obstacle(7,(385,225),[(0,1),(0,-1)],[150,150],o_speed),
                    obstacle(7,(415,375),[(0,-1),(0,1)],[150,150],o_speed),
                    obstacle(7,(445,225),[(0,1),(0,-1)],[150,150],o_speed),
                    obstacle(7,(475,375),[(0,-1),(0,1)],[150,150],o_speed),
                    obstacle(7,(505,225),[(0,1),(0,-1)],[150,150],o_speed),
                    obstacle(7,(535,375),[(0,-1),(0,1)],[150,150],o_speed),
                    obstacle(7,(565,225),[(0,1),(0,-1)],[150,150],o_speed),]
        elif level==3:
            return [obstacle(7,(355,255),[(1,0),(0,1),(-1,0),(0,-1)],[90,90,90,90],o_speed),
                    obstacle(7,(385,255),[(1,0),(0,1),(-1,0),(0,-1),(1,0)],[60,90,90,90,30],o_speed),
                    obstacle(7,(415,255),[(1,0),(0,1),(-1,0),(0,-1),(1,0)],[30,90,90,90,60],o_speed),
                    obstacle(7,(445,255),[(0,1),(-1,0),(0,-1),(1,0)],[90,90,90,90],o_speed),
                    obstacle(7,(445,285),[(0,1),(-1,0),(0,-1),(1,0),(0,1)],[60,90,90,90,30],o_speed),
                    obstacle(7,(445,345),[(-1,0),(0,-1),(1,0),(0,1)],[90,90,90,90],o_speed),
                    obstacle(7,(415,345),[(-1,0),(0,-1),(1,0),(0,1),(-1,0)],[60,90,90,90,30],o_speed),
                    obstacle(7,(385,345),[(-1,0),(0,-1),(1,0),(0,1),(-1,0)],[30,90,90,90,60],o_speed),
                    obstacle(7,(355,345),[(0,-1),(1,0),(0,1),(-1,0)],[90,90,90,90],o_speed),
                    obstacle(7,(355,315),[(0,-1),(1,0),(0,1),(-1,0),(0,-1)],[60,90,90,90,30],o_speed),
                    obstacle(7,(355,285),[(0,-1),(1,0),(0,1),(-1,0),(0,-1)],[30,90,90,90,60],o_speed)]
        return []
    
    def generateCoins(self, level):
        if level==2:
            return [coin((400,300),5)]
        if level==3:
            return [coin((355,225),5)]
        return []
        
    def update(self):
        for o in self.obstacles:
            o.update()
            
    def reset(self):
        self.__init__(self.level, self.fps)
                    
class obstacle():
    def __init__(self, rad, startpoint, directions, distances, speed):
        self.pos=startpoint
        self.rad=rad
        self.startpoint=startpoint
        self.directions=directions
        self.distances=distances
        self.travelled=0
        self.speed=speed
    
    def update(self):
        if self.travelled+self.speed<self.distances[0]:
            self.pos=(self.pos[0]+self.speed*self.directions[0][0],
                      self.pos[1]+self.speed*self.directions[0][1])
            self.travelled+=self.speed
        else:
            self.pos=(self.pos[0]+(self.distances[0]-self.travelled)*self.directions[0][0],
                      self.pos[1]+(self.distances[0]-self.travelled)*self.directions[0][1])
            rest=self.speed-(self.distances[0]-self.travelled)
            self.directions.append(self.directions[0])
            self.distances.append(self.distances[0])
            self.directions.pop(0)
            self.distances.pop(0)
            self.pos=(self.pos[0]+rest*self.directions[0][0],
                      self.pos[1]+rest*self.directions[0][1])
            self.travelled=rest
        
class player():
    def __init__(self, area):
        self.pos=area.startingPos
        self.area=[(self.pos[0]-9,self.pos[1]-9),
                   (self.pos[0]+9,self.pos[1]-9),
                   (self.pos[0]+9,self.pos[1]+9),
                   (self.pos[0]-9,self.pos[1]+9),]
        self.environment=area
        
    def update(self):
        new_area=[(self.pos[0]-9,self.pos[1]-9),
                  (self.pos[0]+9,self.pos[1]-9),
                  (self.pos[0]+9,self.pos[1]+9),
                  (self.pos[0]-9,self.pos[1]+9),]
        new_area_obj=geometry.polygon.Polygon(new_area)
        if self.environment.area_obj.contains(new_area_obj):
            self.area=new_area
        else:
            #reset position
            self.pos=(sum([a[0] for a in self.area])/4,
                      sum([a[1] for a in self.area])/4)
            
    def check_obstacle(self):
        for o in self.environment.obstacles:
            o_obj=geometry.point.Point(o.pos).buffer(o.rad)
            area_obj=geometry.polygon.Polygon(self.area)
            if o_obj.intersects(area_obj):
                return True
        return False
    
    def check_finished(self):
        area_obj=geometry.polygon.Polygon(self.area)
        farea_obj=geometry.polygon.Polygon(self.environment.finishArea)
        for c in self.environment.coins:
            c_obj=geometry.point.Point(c.pos).buffer(c.rad)
            area_obj=geometry.polygon.Polygon(self.area)
            if c_obj.intersects(area_obj):
                c.found=True
        if all([c.found for c in self.environment.coins]):
            if area_obj.intersects(farea_obj):
                return True
        return False
    
    def reset(self):
        self.__init__(self.environment)
        
class coin():
    def __init__(self, pos, rad):
        self.pos=pos
        self.rad=rad
        self.found=False