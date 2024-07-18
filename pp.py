class vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def get_pos(self) -> list:
        return [self.x, self.y]

    def __add__(self, other):
        r = vec2(self.x + other.x, self.y + other.y)
        return r
    def set_pos(self, x, y):
        self.x, self.y = x, y

class vec3:
    def __init__():
        pass

class tex:
    def __init__(self, img: list):
        self.img = img

class Sprite2D:
    def __init__(self):
        self.pos: vec2 = vec2(0, 0)
        self.size: vec2 = vec2(0, 0)
        self.rot: int = 0
        self.img: tex = tex([[0000],[0000],[0000],[0000]])

    def get_pos(self) -> list:
        return self.pos.get_pos()

    def set_pos(self, x, y) -> None:
        self.pos.set_pos(x, y)

class Window:
    def __init__(self):
        self.pos: vec2 = vec2(0, 0)
        self.viewrect: vec2 = vec2(0, 0)
        self.rot: int = 0
        self.skybox: tex = tex([[0000],[0000],[0000],[0000]])

file = open(input(), "r")
for line in file:
    exec(line)
