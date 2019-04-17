import os
import arcade


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Bomber Pie"
MOVEMENT_SPEED = 2


class BomberPie(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Sprite lists
        self.all_sprites_list = None

        # Set up the player
        self.score = 0
        self.player = None

    def setup(self):
        self.all_sprites_list = arcade.SpriteList()

        self.score = 0
        self.player = arcade.AnimatedWalkingSprite()
        self.player.state = 4

        self.player.stand_right_textures = []
        self.player.stand_right_textures.append(arcade.load_texture('player.png', 53, 2, 16, 26))

        self.player.stand_left_textures = []
        self.player.stand_left_textures.append(arcade.load_texture('player.png', 158, 2, 16, 26))

        self.player.walk_up_textures = []
        self.player.walk_up_textures.append(arcade.load_texture('player.png', 2, 4, 15, 25))
        self.player.walk_up_textures.append(arcade.load_texture('player.png', 19, 4, 15, 25))
        self.player.walk_up_textures.append(arcade.load_texture('player.png', 36, 4, 15, 25))

        self.player.walk_down_textures = []
        self.player.walk_down_textures.append(arcade.load_texture('player.png', 107, 2, 15, 26))
        self.player.walk_down_textures.append(arcade.load_texture('player.png', 124, 2, 15, 26))
        self.player.walk_down_textures.append(arcade.load_texture('player.png', 141, 2, 15, 27))

        self.player.walk_left_textures = []
        self.player.walk_left_textures.append(arcade.load_texture('player.png', 158, 2, 16, 26))
        self.player.walk_left_textures.append(arcade.load_texture('player.png', 176, 4, 16, 24))
        self.player.walk_left_textures.append(arcade.load_texture('player.png', 194, 3, 16, 25))

        self.player.walk_right_textures = []
        self.player.walk_right_textures.append(arcade.load_texture('player.png', 53, 2, 16, 26))
        self.player.walk_right_textures.append(arcade.load_texture('player.png', 71, 3, 16, 25))
        self.player.walk_right_textures.append(arcade.load_texture('player.png', 89, 4, 16, 24))

        self.player.texture_change_distance = 20

        self.player.center_x = SCREEN_WIDTH // 2
        self.player.center_y = SCREEN_HEIGHT // 2

        self.all_sprites_list.append(self.player)

        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        arcade.start_render()

        self.all_sprites_list.draw()

        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.ESCAPE:
            self.close()
        elif key == arcade.key.UP or key == arcade.key.Z:
            self.player.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.player.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT or key == arcade.key.Q:
            self.player.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP or key == arcade.key.DOWN or key == arcade.key.Z or key == arcade.key.S:
            self.player.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT or key == arcade.key.Q or key == arcade.key.D:
            self.player.change_x = 0

    def update(self, delta_time):
        self.all_sprites_list.update()
        self.all_sprites_list.update_animation()


def main():
    window = BomberPie(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == '__main__':
    main()
