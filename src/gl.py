from PyQt5.QtWidgets import QOpenGLWidget

from OpenGL import GL


class GLX:
    def initGL(self):
        GL = QOpenGLWidget(self)
        self.setCentralWidget(GL)
        GL.initializeGL = self.iGL
        GL.paintGL = self.paintGL

    def iGL(self):
        print('INIT')

    def paintGL(self):
        print("PAINT")

        GL.glClearColor(0.5, 0.5, 0.5, 1.0)
        GL.glClear(GL.GL_COLOR_BUFFER_BIT)
