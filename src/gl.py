from PyQt5.QtWidgets import QOpenGLWidget, QDesktopWidget
from PyQt5.QtCore import QTimer
from OpenGL import GL
from numpy.random import rand

#
# See: https://habr.com/ru/post/310790/
#
class GLX:
    def initGL(self):
        GL = QOpenGLWidget(self)
        self.gl = GL
        self.setCentralWidget(GL)
        GL.initializeGL = self.iGL
        GL.paintGL = self.paintGL

        self.Triangle()
        self.Pos()
        self.Timer()

    def Triangle(self):
        self.Vs = rand(3, 2) * 2 - 1
        self.Cs = rand(3, 3)

    def Pos(self):
        R = QDesktopWidget().availableGeometry()
        S = R.size() / 3
        W = R.size() - S
        self.resize(S)
        self.move(*(rand(2) * [W.width(), W.height()]))

    def Timer(self):
        timer = QTimer()
        timer.timeout.connect(self.tick)
        timer.start(rand(1)[0] * 2000 + 1000)
        self.timer = timer

    def tick(self):
        self.Triangle()
        self.gl.update()

    def iGL(self):
        GL.glClearColor(0.5, 0.5, 0.5, 1.0)

    def paintGL(self):
        GL.glClear(GL.GL_COLOR_BUFFER_BIT)

        GL.glBegin(GL.GL_TRIANGLES)
        for v, c in zip(self.Vs, self.Cs):
            GL.glColor(*c)
            GL.glVertex2f(*v)
        GL.glEnd()
