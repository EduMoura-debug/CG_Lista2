from GLAPP import GLAPP
from OpenGL import GL
from array import array
import ctypes
import glm
import math

aurea = 1.61803398875
Phi = aurea

icoPositions = (( 0.000,  0.000,  1.000), ( 0.894,  0.000,  0.447), ( 0.276,  0.851,  0.447), (-0.724,  0.526,  0.447),
                (-0.724, -0.526,  0.447), ( 0.276, -0.851,  0.447), ( 0.724,  0.526, -0.447), (-0.276,  0.851, -0.447), 
                (-0.894,  0.000, -0.447), (-0.276, -0.851, -0.447), ( 0.724, -0.526, -0.447), ( 0.000,  0.000, -1.000))

faces = ((0,1,2), (0,2,3), (0,3,4), (0,2,3), 
        (0,3,4), (0,4,5), (0,5,1), (1,2,6),
        (0,5,1), (1,2,6), (2,3,7), (3,4,8),
        (4,5,9), (5,1,10), (6,7,2), (7,8,3),
        (8,9,4), (9,10,5), (10,6,1), (6,7,11),
        (7,8,11), (8,9,11), (9,10,11), (10,6,11))

cores = ((1.0, 0.0, 0.0),
        ( 0.8, 0.1, 0.1),
        ( 0.6, 0.2, 0.3),
        ( 0.4, 0.3, 0.5),
        ( 0.2, 0.4, 0.7),
        ( 0.5, 0.5, 1.0),
        ( 1.0, 0.6, 0.5),
        ( 0.7, 0.7, 0.2),
        ( 0.5, 0.8, 0.4),
        ( 0.3, 0.9, 0.6),
        ( 0.1, 1.0, 0.8),
        (0.0, 0.0, 1.0))
    
class ConstrucaoApp(GLAPP):

    def setup(self):
        # Window setup
        self.title("Construcao Icosaedro")
        self.size(800,800)

        # OpenGL Initialization
        GL.glClearColor(0.2, 0.2, 0.2, 0.0)
        GL.glEnable(GL.GL_DEPTH_TEST)
        GL.glEnable(GL.GL_MULTISAMPLE)

        # Pipeline (shaders)
        self.pipeline = self.loadPipeline("SimplePipeline")
        GL.glUseProgram(self.pipeline)
        self.a = 0
        self.icoArrayBufferId = None

    def drawIcosahedron(self):
        if self.icoArrayBufferId == None:

            position = array('f')
            cor = array('f')



            for f in faces:
                for v in f:
                    position.append(icoPositions[v][0])
                    position.append(icoPositions[v][1])
                    position.append(icoPositions[v][2])
                    cor.append(cores[v][0])
                    cor.append(cores[v][1])
                    cor.append(cores[v][2])

            self.icoArrayBufferId = GL.glGenVertexArrays(1)
            GL.glBindVertexArray(self.icoArrayBufferId)
            GL.glEnableVertexAttribArray(0)
            GL.glEnableVertexAttribArray(1)
                
            idVertexBuffer = GL.glGenBuffers(1)
            GL.glBindBuffer(GL.GL_ARRAY_BUFFER, idVertexBuffer)
            GL.glBufferData(GL.GL_ARRAY_BUFFER, len(position)*position.itemsize, ctypes.c_void_p(position.buffer_info()[0]), GL.GL_STATIC_DRAW)
            GL.glVertexAttribPointer(0,3,GL.GL_FLOAT,GL.GL_FALSE,0,ctypes.c_void_p(0))

            idColorBuffer = GL.glGenBuffers(1)
            GL.glBindBuffer(GL.GL_ARRAY_BUFFER, idColorBuffer)
            GL.glBufferData(GL.GL_ARRAY_BUFFER, len(cor)*cor.itemsize, ctypes.c_void_p(cor.buffer_info()[0]), GL.GL_STATIC_DRAW)
            GL.glVertexAttribPointer(1,3,GL.GL_FLOAT,GL.GL_FALSE,0,ctypes.c_void_p(0))

        GL.glBindVertexArray(self.icoArrayBufferId)
        projection = glm.perspective(math.pi/4,self.width/self.height,0.1,100)
        camera = glm.lookAt(glm.vec3(0,0,5),glm.vec3(0),glm.vec3(0,1,0))
        model = glm.rotate(self.a,glm.vec3(0,0,1)) * glm.rotate(self.a,glm.vec3(0,1,0)) * glm.rotate(self.a,glm.vec3(1,0,0)) 
        mvp = projection * camera * model
        GL.glUniformMatrix4fv(GL.glGetUniformLocation(self.pipeline, "MVP"),1,GL.GL_FALSE,glm.value_ptr(mvp))
        GL.glDrawArrays(GL.GL_TRIANGLES,0,240)
        self.a += 0.01

    def draw(self):
        GL.glClear(GL.GL_COLOR_BUFFER_BIT|GL.GL_DEPTH_BUFFER_BIT)
        self.drawIcosahedron()
        
ConstrucaoApp()
