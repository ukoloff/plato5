from PyQt5.QtWidgets import QOpenGLWidget


class GL:
    def initGL(self):
        GL = QOpenGLWidget(self)
        self.setCentralWidget(GL)
        GL.paintGL = self.paintGL

    def paintGL(self):
        print("PAINT")
