from PyQt5.QtWidgets import QOpenGLWidget

from OpenGL import GL


class GLX:
    def initGL(self):
        GL = QOpenGLWidget(self)
        self.setCentralWidget(GL)
        GL.initializeGL = self.iGL
        GL.paintGL = self.paintGL

    def iGL(self):
        GL.glClearColor(0.5, 0.5, 0.5, 1.0)

    def paintGL(self):
        GL.glClear(GL.GL_COLOR_BUFFER_BIT)

        GL.glBegin(GL.GL_TRIANGLES)
        GL.glColor(1, 0, 0)
        GL.glVertex2f(0, 0)
        GL.glColor(0, 1, 0)
        GL.glVertex2f(0, 1)
        GL.glColor(0, 0, 1)
        GL.glVertex2f(1, 0)
        GL.glEnd()
