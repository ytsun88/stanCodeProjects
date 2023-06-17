"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
This is an extension of breakout.py
I add a scoreboard and a sign that shows remaining lives to the window
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10  # 100 frames per second
NUM_LIVES = 3  # Number of attempts


def main():
    graphics = BreakoutGraphics()
    lives = NUM_LIVES
    total_bricks = graphics.total_bricks
    score = graphics.score
    # Add the animation loop here!
    while True:
        pause(FRAME_RATE)
        if graphics.click_flag:
            if lives > 0:
                dx = graphics.get_dx()
                dy = graphics.get_dy()
                while True:
                    pause(FRAME_RATE)
                    if graphics.ball.y > graphics.window.height:
                        lives -= 1
                        if lives == 0:                                              # If there is no remaining live,
                            graphics.lives_remaining.text = 'Game Over'             # tell the player game is over
                            graphics.scoreboard.text = 'You lose...'                # and the player loses the game
                        else:
                            graphics.lives_remaining.text = 'Lives: ' + str(lives)  # Tell the player how many lives remaining
                        graphics.reset_ball()
                        graphics.click_flag = False
                        break
                    if total_bricks == 0:                           # Set victory condition
                        graphics.ball.move(0, 0)
                        graphics.scoreboard.text = 'You win!!'
                        break
                    graphics.ball.move(dx, dy)
                    if (graphics.ball.x <= 0 and dx < 0) or (
                            graphics.ball.x + graphics.ball.width >= graphics.window.width and dx > 0):
                        dx = - dx
                    if graphics.ball.y <= 0 and dy < 0:
                        dy = - dy

                    obj_lower_left = graphics.window.get_object_at(x=graphics.ball.x,
                                                                   y=graphics.ball.y + graphics.ball.height)
                    obj_lower_right = graphics.window.get_object_at(x=graphics.ball.x + graphics.ball.width,
                                                                    y=graphics.ball.y + graphics.ball.height)
                    obj_upper_left = graphics.window.get_object_at(x=graphics.ball.x,
                                                                   y=graphics.ball.y)
                    obj_upper_right = graphics.window.get_object_at(x=graphics.ball.x + graphics.ball.width,
                                                                    y=graphics.ball.y)

                    if (obj_lower_left is graphics.paddle or obj_lower_right is graphics.paddle) and dy > 0:
                        dy = - dy

                    elif (
                            obj_lower_left is graphics.paddle
                            and graphics.ball.y >= graphics.paddle.y - graphics.ball.height / 2 and dx < 0) or (
                            obj_upper_left is graphics.paddle
                            and graphics.ball.y <= graphics.paddle.y + graphics.paddle.height - graphics.ball.height / 2
                            and dx < 0) or (obj_lower_right is graphics.paddle
                                            and graphics.ball.y >= graphics.paddle.y - graphics.ball.height / 2 and dx > 0) or (
                            obj_upper_right is graphics.paddle
                            and graphics.ball.y <= graphics.paddle.y + graphics.paddle.height - graphics.ball.height / 2
                            and dx > 0):
                        dx = -dx

                    """
                    Define the area where the ball will remove object 
                    so that scoreboard and lives remaining sign won't be removed.
                    
                    Also, once a block is removed, the scoreboard will be refreshed and scores plus one.
                    """
                    if graphics.ball.y < graphics.paddle.y - graphics.ball.height:
                        if obj_upper_left is not None:
                            if graphics.ball.y > obj_upper_left.y + obj_upper_left.height - graphics.ball.height / 2 and dy < 0:
                                score += 1
                                graphics.window.remove(obj_upper_left)
                                total_bricks -= 1
                                graphics.scoreboard.text = 'Score: ' + str(score)
                                dy = - dy
                            elif graphics.ball.y <= obj_upper_left.y + obj_upper_left.height - graphics.ball.height / 2 and dx < 0:
                                score += 1
                                graphics.window.remove(obj_upper_left)
                                total_bricks -= 1
                                graphics.scoreboard.text = 'Score: ' + str(score)
                                dx = - dx
                        if obj_lower_left is not None:
                            if graphics.ball.y < obj_lower_left.y - graphics.ball.height / 2 and dy > 0:
                                graphics.window.remove(obj_lower_left)
                                total_bricks -= 1
                                score += 1
                                graphics.scoreboard.text = 'Score: ' + str(score)
                                dy = - dy
                            elif graphics.ball.y >= obj_lower_left.y - graphics.ball.height / 2 and dx < 0:
                                graphics.window.remove(obj_lower_left)
                                total_bricks -= 1
                                score += 1
                                graphics.scoreboard.text = 'Score: ' + str(score)
                                dx = - dx
                        if obj_upper_right is not None:
                            if graphics.ball.y > obj_upper_right.y + obj_upper_right.height - graphics.ball.height / 2 and dy < 0:
                                score += 1
                                graphics.window.remove(obj_upper_right)
                                total_bricks -= 1
                                graphics.scoreboard.text = 'Score: ' + str(score)
                                dy = - dy
                            elif graphics.ball.y <= obj_upper_right.y + obj_upper_right.height - graphics.ball.height / 2 and dx > 0:
                                score += 1
                                total_bricks -= 1
                                graphics.window.remove(obj_upper_right)
                                graphics.scoreboard.text = 'Score: ' + str(score)
                                dx = - dx
                        if obj_lower_right is not None:
                            if graphics.ball.y < obj_lower_right.y - graphics.ball.height / 2 and dy > 0:
                                graphics.window.remove(obj_lower_right)
                                total_bricks -= 1
                                score += 1
                                graphics.scoreboard.text = 'Score: ' + str(score)
                                dy = - dy
                            elif graphics.ball.y >= obj_lower_right.y - graphics.ball.height / 2 and dx > 0:
                                graphics.window.remove(obj_lower_right)
                                total_bricks -= 1
                                score += 1
                                graphics.scoreboard.text = 'Score: ' + str(score)
                                dx = - dx


if __name__ == '__main__':
    main()
