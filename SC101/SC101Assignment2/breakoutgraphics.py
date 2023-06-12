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


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)
        self._click = True
        self._ball_position_default = (window_width - ball_radius * 2)/2

        # Create a paddle
        self._paddle = GRect(paddle_width, paddle_height,
                             x=(self.window.width - paddle_offset)/2, y=self.window.height - paddle_offset)
        self._paddle.filled = True
        self.window.add(self._paddle)
        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius * 2, ball_radius * 2)
        self.ball.filled = True
        # Default initial velocity for the ball
        self._dx = 0
        self._dy = 0
        self.set_ball_position()
        self._all_bricks = 0
        self.count_bricks = 0
        # Initialize our mouse listeners
        onmousemoved(self.paddle_move)
        onmouseclicked(self.click)
        # Draw bricks
        self.make_brick(brick_width, brick_height, brick_spacing, brick_cols, brick_rows,
                        brick_offset,)
        # Labels
        self._you_win = GLabel('You Win', window_width/2, window_height/2)
        self._you_lose = GLabel('You Lose QAQ', window_width / 2, window_height / 2)
        # self._score_label = GLabel('Score: ' + str(self.count_bricks), 100, 20)
        # self.window.add(self._score_label)

    def make_brick(self, width, height, spacing, cols, rows, offset):
        count = 0
        for i in range(cols):
            x = 0
            x += (width + spacing) * count
            count += 1
            y = offset
            for j in range(rows):
                y += height + spacing
                bricks = GRect(width, height)
                bricks.filled = True
                bricks.fill_color = 'red'
                if j >= 2:
                    bricks.fill_color = 'blue'
                if j >= 4:
                    bricks.fill_color = 'orange'
                if j >= 6:
                    bricks.fill_color = 'yellow'
                if j >= 8:
                    bricks.fill_color = 'green'
                self.window.add(bricks, x, y)
                self._all_bricks += 1
        return self._all_bricks

    def paddle_move(self, event):
        self._paddle.x = event.x - self._paddle.width / 2
        if self._paddle.x > self.window.width - self._paddle.width:
            self._paddle.x = self.window.width - self._paddle.width
        if self._paddle.x < 0:
            self._paddle.x = 0

    def set_ball_position(self):
        self.ball.x = (self.window.width - self.ball.width)/2
        self.ball.y = (self.window.height - self.ball.height)/2
        self.window.add(self.ball)

    def set_ball_velocity(self):
        self._dx = random.randint(1, MAX_X_SPEED)
        self._dy = INITIAL_Y_SPEED
        if random.random() > 0.5:
            self._dx = - self._dx

    def click(self, event):
        if self.ball.x == self._ball_position_default:
            if self._click:
                self._click = False
                self.set_ball_velocity()

    def bounce_on_paddle(self):  # 1. (x, y+2r) 2. (x+2r, y+2r)
        left_bottom = self.window.get_object_at(self.ball.x, self.ball.y + self.ball.height)
        right_bottom = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y + self.ball.height)
        if self.ball.y > self.window.height / 2:
            if left_bottom or right_bottom is not None:
                self._dy = - self._dy

    def bounce_on_wall(self):
        if self.ball.x <= 0 or self.ball.x + self.ball.width >= self.window.width:
            self._dx = -self._dx
        if self.ball.y <= 0:
            self._dy = -self._dy

    def remove_the_bricks(self):
        left_top = self.window.get_object_at(self.ball.x, self.ball.y)
        right_top = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y)
        left_bottom = self.window.get_object_at(self.ball.x, self.ball.y + self.ball.height)
        right_bottom = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y + self.ball.height)
        # label = self._score_label  # extension  不知道怎麼解決計分版碰撞後會消失的問題？
        # self._score_label.text = 'Score: ' + str(self.count_bricks)
        if self.ball.y + self.ball.height < self.window.height / 2:
            if left_top or left_bottom or right_top or right_bottom is not None:
                if left_top:
                    self.window.remove(left_top)
                elif right_top:
                    self.window.remove(right_top)
                elif left_bottom:
                    self.window.remove(left_bottom)
                elif right_bottom:
                    self.window.remove(right_bottom)
                self.count_bricks += 1
                self._dy = - self._dy

    def get_vx(self):
        return self._dx

    def get_vy(self):
        return self._dy

    def get_all_bricks(self):
        return self._all_bricks

    def get_win_label(self):
        return self._you_win

    def get_lose_label(self):
        return self._you_lose

    # def get_score_label(self):  # extension
    #     return self._score_label




