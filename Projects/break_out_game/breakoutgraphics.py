"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball
NUM_LIVES = 3          # Number of attempts


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, num_lives = NUM_LIVES, title='Breakout'):

        """
        Instance variables we need for setting up the game.
        """
        self.paddle_os = paddle_offset
        self.brick_os = brick_offset
        self.brick_s = brick_spacing
        self.click_flag = False
        self.total_bricks = brick_rows * brick_cols
        self.num_lives = num_lives
        self.score = 0

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(width=paddle_width, height=paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, x=(self.window.width-self.paddle.width)/2, y=self.window.height-paddle_offset)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.window.add(self.ball, x=(self.window.width-self.ball.width)/2, y=(self.window.height-self.ball.height)/2)

        # A label to check lives remaining
        self.lives_remaining = GLabel('Lives: ' + str(self.num_lives), x=0, y=window_height)
        self.lives_remaining.color = 'black'
        self.lives_remaining.font = '-20'
        self.window.add(self.lives_remaining)

        # Create a scoreboard
        self.scoreboard = GLabel('Score: ' + str(self.score))
        self.scoreboard.color = 'black'
        self.scoreboard.font = '-20'
        self.window.add(self.scoreboard, x=window_width-self.scoreboard.width-30, y=window_height)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Initialize our mouse listeners
        onmouseclicked(self.ball_drop)
        onmousemoved(self.paddle_move)

        # Draw bricks
        self.create_bricks(brick_rows, brick_cols, brick_width, brick_height, brick_spacing, brick_offset)

    """
    Instance method for creating rows of blocks with different colors.
    """
    def create_bricks(self, row_num, col_num, brick_w, brick_h, brick_s, brick_o):
        for i in range(col_num):
            for j in range(row_num):
                brick = GRect(width=brick_w, height=brick_h)
                brick.filled = True
                if j < 2:
                    brick.fill_color = 'red'
                elif j < 4:
                    brick.fill_color = 'orange'
                elif j < 6:
                    brick.fill_color = 'yellow'
                elif j < 8:
                    brick.fill_color = 'green'
                else:
                    brick.fill_color = 'blue'

                self.window.add(brick, x=i*brick_w+(i-1)*brick_s, y=brick_o+j*brick_h+(j-1)*brick_s)

    def paddle_move(self, mouse_move):
        self.window.add(self.paddle, x=mouse_move.x-self.paddle.width/2, y=self.window.height-self.brick_os)
        if mouse_move.x <= self.paddle.width/2:
            self.paddle.x = 0
        elif mouse_move.x >= self.window.width - self.paddle.width/2:
            self.paddle.x = self.window.width - self.paddle.width

    """
    Define the ball movement after a click
    """
    def ball_drop(self, mouse_click):
        if not self.click_flag:
            self.click_flag = True
            self.__dy = INITIAL_Y_SPEED
            self.__dx = random.randint(1, MAX_X_SPEED)
            if random.random() > 0.5:
                self.__dx = - self.__dx

    def reset_ball(self):
        self.window.add(self.ball, x=(self.window.width - self.ball.width) / 2,
                        y=(self.window.height - self.ball.height) / 2)

    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy
