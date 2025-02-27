import glfw
from OpenGL.GL import *
import numpy as np

shapes = []

def read_file(filename):
    with open(filename, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            parts = line.strip().split()
            if len(parts) < 2:
                continue
            num_vertices = int(parts[0])
            draw_mode = parts[1]
            vertices = []
            for _ in range(num_vertices):
                vertex_line = file.readline()
                x, y = map(float, vertex_line.strip().split())
                vertices.append((x, y))
            shapes.append((draw_mode, vertices))

def draw_shapes():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0) 

    for shape in shapes:
        draw_mode, vertices = shape
        if draw_mode == 'l':
            glBegin(GL_LINE_STRIP)
        elif draw_mode == 'f':
            glBegin(GL_POLYGON)
        else:
            continue

        for x, y in vertices:
            glVertex2f(x, y)
        glEnd()

def main():
    if not glfw.init():
        raise Exception("GLFW initialization failed")

    # Create a windowed mode window and its OpenGL context
    window = glfw.create_window(1000, 800, "Lab 2 Assignment: Snoopy", None, None)
    if not window:
        glfw.terminate()
        raise Exception("GLFW window creation failed")

    glfw.make_context_current(window)

    # Setting up the viewport and orthographic projection
    glViewport(0, 0, 1000, 800)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, 50, 0, 50, -1, 1)  # Map the window coordinates to the range [0, 50] in both x and y axes
    glMatrixMode(GL_MODELVIEW)

    read_file("snoopy.txt")

    # Main loop
    while not glfw.window_should_close(window):
        draw_shapes()
        
        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()