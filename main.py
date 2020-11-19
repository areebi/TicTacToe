import arcade


def draw_x(x, y):
    arcade.draw_line((SCREEN_WIDTH / 3) * x + (SCREEN_WIDTH / 12), (SCREEN_HEIGHT / 3) * (2 - y) + (SCREEN_HEIGHT / 12),
                     (SCREEN_WIDTH / 3) * x + (SCREEN_WIDTH / 4), (SCREEN_HEIGHT / 3) * (2 - y) + (SCREEN_HEIGHT / 4),
                     arcade.color.LIME_GREEN, MARKER_WIDTH)
    arcade.draw_line((SCREEN_WIDTH / 3) * x + (SCREEN_WIDTH / 4), (SCREEN_HEIGHT / 3) * (2 - y) + (SCREEN_HEIGHT / 12),
                     (SCREEN_WIDTH / 3) * x + (SCREEN_WIDTH / 12), (SCREEN_HEIGHT / 3) * (2 - y) + (SCREEN_HEIGHT / 4),
                     arcade.color.LIME_GREEN, MARKER_WIDTH)


def draw_o(x, y):
    arcade.draw_circle_outline(SCREEN_WIDTH / 3 * x + SCREEN_WIDTH / 6, SCREEN_HEIGHT / 3 * (2 - y) + SCREEN_HEIGHT / 6,
                               SCREEN_HEIGHT / 8, arcade.color.LIME_GREEN, MARKER_WIDTH)


def draw_win(win):
    arcade.draw_line(SCREEN_WIDTH / 3 * win[0][0] + SCREEN_WIDTH / 6,
                     SCREEN_HEIGHT / 3 * (2 - win[0][1]) + SCREEN_HEIGHT / 6,
                     SCREEN_WIDTH / 3 * win[2][0] + SCREEN_WIDTH / 6,
                     SCREEN_HEIGHT / 3 * (2 - win[2][1]) + SCREEN_HEIGHT / 6, arcade.color.WHITE, WIN_WIDTH)


SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_MARGIN = 10
LINE_WIDTH = 10
MARKER_WIDTH = 25
WIN_WIDTH = 12.5
TITLE_FONT = 72
TITLE_Y = 400
OPTION_FONT = 36
OPTION_HEIGHT = 90
OPTION1_Y = 225
OPTION2_Y = 95
SCREEN_TITLE = "Tic Tac Toe"
LIST_WINS = [[[0, 0], [0, 1], [0, 2]],
             [[1, 0], [1, 1], [1, 2]],
             [[2, 0], [2, 1], [2, 2]],
             [[0, 0], [1, 0], [2, 0]],
             [[0, 1], [1, 1], [2, 1]],
             [[0, 2], [1, 2], [2, 2]],
             [[0, 0], [1, 1], [2, 2]],
             [[0, 2], [1, 1], [2, 0]]]


class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.BLACK)

        self.gameMode = 0
        self.list_x = []
        self.list_o = []
        self.list_x_translate = []
        self.list_o_translate = []
        self.is_x_turn = True

    def on_draw(self):
        arcade.start_render()

        if self.gameMode == 0:
            self.mode_selection()
        elif self.gameMode == 1:
            self.one_player()
        elif self.gameMode == 2:
            self.two_player()
        else:
            self.two_player()

    def mode_selection(self):
        arcade.draw_text("TIC TAC TOE", SCREEN_MARGIN, TITLE_Y, arcade.color.LIME_GREEN, TITLE_FONT,
                         SCREEN_WIDTH - 2 * SCREEN_MARGIN, "center")
        arcade.draw_rectangle_outline(SCREEN_WIDTH / 2, OPTION1_Y + 25, 2 * SCREEN_WIDTH / 3, OPTION_HEIGHT,
                                      arcade.color.LIME_GREEN, LINE_WIDTH)
        arcade.draw_text("One Player", SCREEN_MARGIN, OPTION1_Y, arcade.color.LIME_GREEN, OPTION_FONT,
                         SCREEN_WIDTH - 2 * SCREEN_MARGIN, "center")
        arcade.draw_rectangle_outline(SCREEN_WIDTH / 2, OPTION2_Y + 25, 2 * SCREEN_WIDTH / 3, OPTION_HEIGHT,
                                      arcade.color.LIME_GREEN, LINE_WIDTH)
        arcade.draw_text("Two Player", SCREEN_MARGIN, OPTION2_Y, arcade.color.LIME_GREEN, OPTION_FONT,
                         SCREEN_WIDTH - 2 * SCREEN_MARGIN, "center")
        arcade.draw_rectangle_outline(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT,
                                      arcade.color.LIME_GREEN, 10)

    def one_player(self):
        arcade.draw_line(SCREEN_MARGIN, SCREEN_HEIGHT / 3, SCREEN_WIDTH - SCREEN_MARGIN, SCREEN_HEIGHT / 3,
                         arcade.color.LIME_GREEN, LINE_WIDTH)
        arcade.draw_line(SCREEN_MARGIN, 2 * SCREEN_HEIGHT / 3, SCREEN_WIDTH - SCREEN_MARGIN, 2 * SCREEN_HEIGHT / 3,
                         arcade.color.LIME_GREEN, LINE_WIDTH)
        arcade.draw_line(SCREEN_WIDTH / 3, SCREEN_MARGIN, SCREEN_WIDTH / 3, SCREEN_HEIGHT - SCREEN_MARGIN,
                         arcade.color.LIME_GREEN, LINE_WIDTH)
        arcade.draw_line(2 * SCREEN_WIDTH / 3, SCREEN_MARGIN, 2 * SCREEN_WIDTH / 3, SCREEN_HEIGHT - SCREEN_MARGIN,
                         arcade.color.LIME_GREEN, LINE_WIDTH)
        for element in self.list_x:
            draw_x(element[0], element[1])
        for element in self.list_o:
            draw_o(element[0], element[1])
        for win in LIST_WINS:
            if all(item in self.list_x for item in win):
                del self.list_o[-1]
                draw_win(win)
                self.gameMode = 3
            elif all(item in self.list_o for item in win):
                draw_win(win)
                self.gameMode = 3
        if len(self.list_x) == 5:
            self.gameMode = 3

    def two_player(self):
        arcade.draw_line(SCREEN_MARGIN, SCREEN_HEIGHT / 3, SCREEN_WIDTH - SCREEN_MARGIN, SCREEN_HEIGHT / 3,
                         arcade.color.LIME_GREEN, LINE_WIDTH)
        arcade.draw_line(SCREEN_MARGIN, 2 * SCREEN_HEIGHT / 3, SCREEN_WIDTH - SCREEN_MARGIN, 2 * SCREEN_HEIGHT / 3,
                         arcade.color.LIME_GREEN, LINE_WIDTH)
        arcade.draw_line(SCREEN_WIDTH / 3, SCREEN_MARGIN, SCREEN_WIDTH / 3, SCREEN_HEIGHT - SCREEN_MARGIN,
                         arcade.color.LIME_GREEN, LINE_WIDTH)
        arcade.draw_line(2 * SCREEN_WIDTH / 3, SCREEN_MARGIN, 2 * SCREEN_WIDTH / 3, SCREEN_HEIGHT - SCREEN_MARGIN,
                         arcade.color.LIME_GREEN, LINE_WIDTH)
        for element in self.list_x:
            draw_x(element[0], element[1])
        for element in self.list_o:
            draw_o(element[0], element[1])
        for win in LIST_WINS:
            if all(item in self.list_x for item in win):
                draw_win(win)
                self.gameMode = 3
            elif all(item in self.list_o for item in win):
                draw_win(win)
                self.gameMode = 3
        if len(self.list_x) == 5:
            self.gameMode = 3

    def on_mouse_press(self, x, y, button, modifiers):
        if self.gameMode == 0:
            if 95 <= x <= 505 and 70 <= y < 170:
                self.gameMode = 2
                return
            elif 95 <= x <= 505 and 200 <= y < 300:
                self.gameMode = 1
                return

        if self.gameMode == 1:
            xClick = int(x / 200)
            yClick = 2 - int(y / 200)
            if [xClick, yClick] not in self.list_x and [xClick, yClick] not in self.list_o:
                self.list_x.append([xClick, yClick])
            if len(self.list_x) == len(self.list_o) + 1:
                # First Move
                if len(self.list_x) == 1:
                    if [1, 1] not in self.list_x:
                        self.list_o.append([1, 1])
                        return
                    else:
                        self.list_o.append([0, 0])
                        return
                # General AI
                # If O has winning move, take. If X has winning move, prevent it.
                xBlock = []
                for win in LIST_WINS:
                    xMatch = 0
                    oMatch = 0
                    notFound = []
                    for element in win:
                        if element in self.list_o:
                            oMatch += 1
                        elif element in self.list_x:
                            xMatch += 1
                        else:
                            notFound.append(element)
                    if oMatch == 2 and notFound:
                        self.list_o.append(notFound[0])
                        return
                    elif xMatch == 2 and notFound:
                        xBlock = notFound[0]
                if xBlock:
                    self.list_o.append(xBlock)
                    return

                # Second Move If No Win
                if len(self.list_x) == 2:
                    if self.list_x[0] in [[0, 0], [0, 1], [1, 1]]:
                        self.list_x_translate = self.list_x
                        self.list_o_translate = self.list_o
                    if self.list_x[0] == [2, 0] or self.list_x[0] == [2, 1]:
                        for each in self.list_x:
                            self.list_x_translate.append([2 - each[0], each[1]])
                        for each in self.list_o:
                            self.list_o_translate.append([2 - each[0], each[1]])
                    if self.list_x[0] == [2, 2] or self.list_x[0] == [1, 2]:
                        for each in self.list_x:
                            self.list_x_translate.append([2 - each[1], 2 - each[0]])
                        for each in self.list_o:
                            self.list_o_translate.append([2 - each[1], 2 - each[0]])
                    if self.list_x[0] == [0, 2]:
                        for each in self.list_x:
                            self.list_x_translate.append([each[0], 2 - each[1]])
                        for each in self.list_o:
                            self.list_o_translate.append([each[0], 2 - each[1]])
                    if self.list_x[0] == [1, 0]:
                        for each in self.list_x:
                            self.list_x_translate.append([each[1], each[0]])
                        for each in self.list_o:
                            self.list_o_translate.append([each[1], each[0]])

                    if [0, 0] not in self.list_o_translate and [0, 0] not in self.list_x_translate:
                        if self.list_x_translate[1][1] > self.list_x_translate[1][0]:
                            self.list_o_translate.append([0, 2])
                        else:
                            self.list_o_translate.append([0, 0])
                    elif [0, 0] in self.list_o_translate:
                        self.list_o_translate.append([2, 0])
                    else:
                        if self.list_x_translate[1][1] > self.list_x_translate[1][0]:
                            self.list_o_translate.append([2, 1])
                        else:
                            self.list_o_translate.append([1, 2])

                    if self.list_x[0] == [2, 0] or self.list_x[0] == [2, 1]:
                        self.list_o.append([2 - self.list_o_translate[1][0], self.list_o_translate[1][1]])
                    if self.list_x[0] == [2, 2] or self.list_x[0] == [1, 2]:
                        self.list_o.append([2 - self.list_o_translate[1][1], 2 - self.list_o_translate[1][0]])
                    if self.list_x[0] == [0, 2]:
                        self.list_o.append([self.list_o_translate[1][0], 2 - self.list_o_translate[1][1]])
                    if self.list_x[0] == [1, 0]:
                        self.list_o.append([self.list_o_translate[1][1], self.list_o_translate[1][0]])
                    return

                # If none of above, fill first empty space
                for i in range(3):
                    for j in range(3):
                        if [i, j] not in self.list_o and [i, j] not in self.list_x:
                            self.list_o.append([i, j])
                            return

        if self.gameMode == 2:
            xClick = int(x / 200)
            yClick = 2 - int(y / 200)
            if [xClick, yClick] not in self.list_x and [xClick, yClick] not in self.list_o:
                if self.is_x_turn:
                    self.list_x.append([xClick, yClick])
                else:
                    self.list_o.append([xClick, yClick])
                self.is_x_turn = not self.is_x_turn

        if self.gameMode == 3:
            self.gameMode = 0
            self.list_x = []
            self.list_o = []
            self.list_x_translate = []
            self.list_o_translate = []
            self.is_x_turn = True


def main():
    MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


main()
