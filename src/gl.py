from PyQt5.QtWidgets import QOpenGLWidget, QDesktopWidget
from OpenGL import GL
from numpy.random import rand

class GLX:
    def initGL(self):
        GL = QOpenGLWidget(self)
        self.setCentralWidget(GL)
        GL.initializeGL = self.iGL
        GL.paintGL = self.paintGL

        self.Triangle()
        self.Pos()

    def Triangle(self):
        self.Vs = rand(3, 2) * 2 - 1
        self.Cs = rand(3, 3)

    def Pos(self):
        R = QDesktopWidget().availableGeometry()
        S = R.size() / 3
        W = R.size() - S
        self.resize(S)
        self.move(*(rand(2) * [W.width(), W.height()]))

    def iGL(self):
        GL.glClearColor(0.5, 0.5, 0.5, 1.0)

    def paintGL(self):
        GL.glClear(GL.GL_COLOR_BUFFER_BIT)

        GL.glBegin(GL.GL_TRIANGLES)
        for v, c in zip(self.Vs, self.Cs):
            GL.glColor(*c)
            GL.glVertex2f(*v)
        GL.glEnd()
