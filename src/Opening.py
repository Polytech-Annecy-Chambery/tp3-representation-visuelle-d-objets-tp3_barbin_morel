# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:47:50 2017

@author: lfoul
"""

import OpenGL.GL as gl

class Opening:
    # Constructor
    def __init__(self, parameters = {}) :  
        # Parameters
        # position: mandatory
        # width: mandatory
        # height: mandatory
        # thickness: mandatory
        # color: mandatory        

        # Sets the parameters
        self.parameters = parameters

        # Sets the default parameters 
        if 'position' not in self.parameters:
            raise Exception('Parameter "position" required.')       
        if 'width' not in self.parameters:
            raise Exception('Parameter "width" required.')
        if 'height' not in self.parameters:
            raise Exception('Parameter "height" required.')
        if 'thickness' not in self.parameters:
            raise Exception('Parameter "thickness" required.')    
        if 'color' not in self.parameters:
            raise Exception('Parameter "color" required.')  
            
        # Generates the opening from parameters
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
            # [0, 3, 2, 1],
            [3, 7, 6, 2],
            # [7, 6, 5, 4],
            [0, 4, 5, 1],
            [1, 2, 6, 5],
            [0, 3, 7, 4]
                ]   
        
    # Draws the faces                
    def draw(self):        
        # A compléter en remplaçant pass par votre code
        gl.glPushMatrix()
        gl.glTranslate(self.parameters['position'][0],self.parameters['position'][1],self.parameters['position'][2])
        # gl.glRotate(self.parameters['orientation'],0,0,1)
        
    
                
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
        
        gl.glBegin(gl.GL_QUADS)# Tracé d’un quadrilatère
        gl.glColor3fv(self.parameters['color']) # Couleur gris moyen
        for i in range (0, len(self.faces)):
            for j in range (0,4) :   
                gl.glVertex3fv(self.vertices[self.faces[i][j]])
        gl.glEnd()
        gl.glPopMatrix()