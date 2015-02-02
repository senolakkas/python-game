# -*- coding: utf-8 -*-

import sfml as sf


WIDTH = 640
HEIGHT = 480
TITLE = "Python SFML Class Example"


class Game:
    def __init__(self):
        self.window = sf.RenderWindow(
            sf.VideoMode(WIDTH, HEIGHT), TITLE)

        self.circle = sf.CircleShape(50)
        self.circle.origin = self.circle.radius, self.circle.radius

        try:
            bg_texture = sf.Texture.from_file(
                'assets/images/background.png')

            plane_texture = sf.Texture.from_file(
                'assets/images/planeRed1.png')
            s_buffer = sf.SoundBuffer.from_file(
                'assets/sounds/tone1.ogg')
            music = sf.Music.from_file(
                'assets/sounds/spaceTrash3.ogg')
            font = sf.Font.from_file(
                'assets/fonts/kenvector_future_thin.ttf')
        except IOError:
            print("HATA VERDİ!!")
            sys.exit(-1)



    def run(self):
        while self.window.is_open:
            for event in self.window.events:
                self.handle_events(event)
            self.update()
            self.render()


    def handle_events(self, event):
        if type(event) is sf.CloseEvent:
            self.window.close()

    def render(self):
        self.window.clear()
        self.window.draw(self.circle)
        self.window.display()

    def update(self):
        self.circle.position = \
            sf.Mouse.get_position(self.window)


if __name__ == "__main__":
    oyun = Game()
    oyun.run()