# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:47:50 2017

@author: lfoul
"""
import OpenGL.GL as gl

class Section:
    # Constructor
    def __init__(self, parameters = {}) :  
        # Parameters
        # position: position of the wall 
        # width: width of the wall - mandatory
        # height: height of the wall - mandatory
        # thickness: thickness of the wall
        # color: color of the wall        

        # Sets the parameters
        self.parameters = parameters
        
        # Sets the default parameters
        if 'position' not in self.parameters:
            self.parameters['position'] = [0, 0, 0]        
        if 'width' not in self.parameters:
            raise Exception('Parameter "width" required.')   
        if 'height' not in self.parameters:
            raise Exception('Parameter "height" required.')   
        if 'orientation' not in self.parameters:
            self.parameters['orientation'] = 0              
        if 'thickness' not in self.parameters:
            self.parameters['thickness'] = 0.2    
        if 'color' not in self.parameters:
            self.parameters['color'] = [0.5, 0.5, 0.5]       
        if 'edges' not in self.parameters:
            self.parameters['edges'] = False             
            
        # Objects list
        self.objects = []

        # Generates the wall from parameters
        self.generate()   
        
    # Getter
    def getParameter(self, parameterKey):
        return self.parameters[parameterKey]
    
    # Setter
    def setParameter(self, parameterKey, parameterValue):
        self.parameters[parameterKey] = parameterValue
        return self     

    # Defines the vertices and faces 
    def generate(self):
        self.vertices = [ 
            [0, 0, 0 ], 
            [0, 0, self.parameters['height']], 
            [self.parameters['width'], 0, self.parameters['height']],
            [self.parameters['width'], 0, 0],
            [0, self.parameters['thickness'], 0 ], 
            [0, self.parameters['thickness'], self.parameters['height']], 
            [self.parameters['width'], self.parameters['thickness'], self.parameters['height']],
            [self.parameters['width'], self.parameters['thickness'], 0]   
                ]
        self.faces = [
            [0, 3, 2, 1],
            [3, 7, 6, 2],
            [7, 6, 5, 4],
            [0, 4, 5, 1],
            [1, 2, 6, 5],
            [0, 3, 7, 4]
                ]   

    # Checks if the opening can be created for the object x
    def canCreateOpening(self, x):
        # A compléter en remplaçant pass par votre code
        if not(self.parameters['width']+self.parameters['position'][0]>=(x.parameters['width']+x.parameters['position'][0])):
            return False
        if not(self.parameters['height']+self.parameters['position'][2]>=(x.parameters['height']+x.parameters['position'][2])):
            return False
        if not(self.parameters['position'][0]<=x.parameters['position'][0]):
            return False
        if not(self.parameters['position'][2]<=x.parameters['position'][2]):
            return False
        return True
        
    # Creates the new sections for the object x
    def createNewSections(self, x):
        # A compléter en remplaçant pass par votre code
        liste = []
       
        if self.canCreateOpening(x)==True:
            
            if x.parameters['position'][0]>self.parameters['position'][0]:
                mur1 = Section({'position':self.parameters['position'],'orientation':self.parameters['orientation'],'color':self.parameters['color'],'width':x.parameters['position'][0],'height':self.parameters['height'],'thickness':self.parameters['thickness']})
                liste.append(mur1)
    
            if x.parameters['position'][2]>self.parameters['position'][2]:
                mur2 = Section({'position':[x.parameters['position'][0],0,0],'orientation':self.parameters['orientation'],'color':self.parameters['color'],'width':x.parameters['width'],'height':x.parameters['position'][2],'thickness':self.parameters['thickness']})
                liste.append(mur2)
                
            if x.parameters['position'][2]+x.parameters['height']<self.parameters['height']+self.parameters['position'][2]:
                mur3 = Section({'position':[x.parameters['position'][0],0,x.parameters['position'][2]+x.parameters['height']],'orientation':self.parameters['orientation'],'color':self.parameters['color'],'width':x.parameters['width'],'height':self.parameters['height']-(x.parameters['position'][2]+x.parameters['height']),'thickness':self.parameters['thickness']})
                liste.append(mur3)
                
            if x.parameters['position'][0]+x.parameters['width']<self.parameters['width']+self.parameters['position'][0]:
                mur4 = Section({'position':[x.parameters['position'][0]+x.parameters['width'],0,0], 'orientation':self.parameters['orientation'],'color':self.parameters['color'], 'width':(self.parameters['width']-(x.parameters['position'][0]+x.parameters['width'])), 'height':self.parameters['height'],'thickness':self.parameters['thickness']})
                liste.append(mur4)
        
        return (liste)
    # Draws the edges
    def drawEdges(self):
        # A compléter en remplaçant pass par votre code
        
        
        if self.parameters['edges']:
            
            gl.glBegin(gl.GL_LINES)
            
            
            newColor =[]
            for i in range (0, len(self.parameters['color'])):
                newColor.append(self.parameters['color'][i]*0.8)
                
            gl.glColor3fv(newColor)
            gl.glVertex3fv(self.vertices[0])
            gl.glVertex3fv(self.vertices[3])  
            gl.glColor3fv(newColor)
            gl.glVertex3fv(self.vertices[0])
            gl.glVertex3fv(self.vertices[1])
            gl.glColor3fv(newColor)
            gl.glVertex3fv(self.vertices[1])
            gl.glVertex3fv(self.vertices[5])
            gl.glColor3fv(newColor)
            gl.glVertex3fv(self.vertices[5])
            gl.glVertex3fv(self.vertices[6]) 
            gl.glColor3fv(newColor)
            gl.glVertex3fv(self.vertices[5])
            gl.glVertex3fv(self.vertices[4])
            gl.glColor3fv(newColor)
            gl.glVertex3fv(self.vertices[0])
            gl.glVertex3fv(self.vertices[4]) 
            gl.glColor3fv(newColor)
            gl.glVertex3fv(self.vertices[4])
            gl.glVertex3fv(self.vertices[7]) 
            gl.glColor3fv(newColor)
            gl.glVertex3fv(self.vertices[6])
            gl.glVertex3fv(self.vertices[7]) 
            gl.glColor3fv(newColor)
            gl.glVertex3fv(self.vertices[1])
            gl.glVertex3fv(self.vertices[2]) 
            gl.glColor3fv(newColor)
            gl.glVertex3fv(self.vertices[2])
            gl.glVertex3fv(self.vertices[3]) 
            gl.glColor3fv(newColor)
            gl.glVertex3fv(self.vertices[2])
            gl.glVertex3fv(self.vertices[6]) 
            gl.glColor3fv(newColor)
            gl.glVertex3fv(self.vertices[3])
            gl.glVertex3fv(self.vertices[7]) 
            
            gl.glEnd()   

    
    # Draws the faces
    def draw(self):
        # A compléter en remplaçant pass par votre code
        gl.glPushMatrix()
        gl.glTranslate(self.parameters['position'][0],self.parameters['position'][1],self.parameters['position'][2])
        gl.glRotate(self.parameters['orientation'],0,0,1)
        
        if self.parameters['edges']:
            self.drawEdges()
        
        gl.glBegin(gl.GL_QUADS)# Tracé d’un quadrilatère
        gl.glColor3fv(self.parameters['color']) # Couleur gris moyen
        for i in range (0, len(self.faces)):
            for j in range (0,4) :   
                gl.glVertex3fv(self.vertices[self.faces[i][j]])
        gl.glEnd()
        gl.glPopMatrix()