"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 20       # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    lives = NUM_LIVES
    # Add animation loop here!
    while True:
        pause(FRAME_RATE)
        vx = graphics.get_vx()
        vy = graphics.get_vy()
        graphics.ball.move(vx, vy)
        graphics.bounce_on_wall()
        graphics.remove_the_bricks()
        graphics.bounce_on_paddle()
        if graphics.ball.y + graphics.ball.height > graphics.window.height:
            lives -= 1
            if lives > 0:
                graphics.set_ball_position()
            else:
                graphics.window.add(graphics.get_lose_label())  # extension
                break
        elif graphics.count_bricks == graphics.get_all_bricks():
            graphics.window.add(graphics.get_win_label())   # extension
            break


if __name__ == '__main__':
    main()
