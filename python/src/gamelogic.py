from shapely import geometry

class area():
    def __init__(self, level):
        self.level=level
        if level==1:
            self.frame=[(100,210),(100,390),(700,390),(700,210)]
            self.gridfactor=30
            self.sizeX=20
            self.sizeY=6
            
            self.playingField=[(100,210),
                               (220,210),
                               (220,360),
                               (250,360),
                               (250,240),
                               (520,240),
                               (520,210),
                               (700,210),
                               (700,390),
                               (580,390),
                               (580,240),
                               (550,240),
                               (550,360),
                               (280,360),
                               (280,390),
                               (100,390)]
            
            self.startArea=[(100,210),
                            (220,210),
                            (220,390),
                            (100,390)]
            
            self.finishArea=[(580,210),
                             (700,210),
                             (700,390),
                             (580,390)]
            
            self.startingPos=(160,300)
            
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
                            
            self.obstacles=self.generateObstacles()
    
    def generateObstacles(self):
        return [obstacle(7,(265,255),(535,255),5),
                obstacle(7,(535,285),(265,285),5),
                obstacle(7,(265,315),(535,315),5),
                obstacle(7,(535,345),(265,345),5)]
        
    def update(self):
        for o in self.obstacles:
            o.update()
            
    def reset(self):
        self.__init__(self.level)
                    
class obstacle():
    def __init__(self, rad, startpoint, endpoint, speed):
        self.pos=startpoint
        self.rad=rad
        self.startpoint=startpoint
        self.endpoint=endpoint
        self.speed=speed#the distance between startpoint end endpoint must be a multiple of the speed
    
    def update(self):
        self.pos=(int((self.endpoint[0]-self.startpoint[0])/(abs(self.endpoint[0]-self.startpoint[0])+abs(self.endpoint[1]-self.startpoint[1]))*self.speed+self.pos[0]),
                  int((self.endpoint[1]-self.startpoint[1])/(abs(self.endpoint[0]-self.startpoint[0])+abs(self.endpoint[1]-self.startpoint[1]))*self.speed+self.pos[1]))
        if self.pos==self.endpoint:
            self.startpoint, self.endpoint=self.endpoint,self.startpoint
        
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
        if area_obj.intersects(farea_obj):
            return True
        return False
    
    def reset(self):
        self.__init__(self.environment)
        
        