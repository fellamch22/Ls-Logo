DEFAULT_COLOR = " "


# Operation Codes: constants used to identify the various types of instructions
OP_ASSIGN = 1
OP_FORWARD = 2
OP_ROTATE = 3
OP_PEN_DOWN = 4
OP_PEN_UP = 5
OP_COLOR = 6
OP_INCR = 7
OP_GOTO = 8
OP_GOTONZ = 9


# Character representation of directions (used, e.g., to draw the turtle on the canvas)
DIRECTION_STRINGS = {
    0: "\u2192",  # →
    45: "\u2197",  # ↗
    90: "\u2191",  # ↑
    135: "\u2196",  # ↖
    180: "\u2190",  # ←
    225: "\u2199",  # ↙
    270: "\u2193",  # ↓
    315: "\u2198",  # ↘
}


def init_canvas(lines, columns, color=DEFAULT_COLOR):
    """create a new canvas of size lines * columns, filled with color

    """
    assert lines > 0
    assert columns > 0
    return [[color] * columns for i in range(lines)]


def init_state(lines, columns, program=None):
    """Return a new evaluation state (corresponding to the initial state of the
    interpreter), as a dictionary

    """
    canvas = init_canvas(lines, columns, DEFAULT_COLOR)

    return {
        "canvas": canvas,  # canvas content, as a list of rows (= lists of characters)
        "width": columns,  # canvas width
        "height": lines,  # canvas height
        "position": (0, 0),  # turtle's position on the canvas (LINExCOLUMN coordinate)
        "direction": 0,  # direction the turtle is facing
        "drawing": False,  # whether the pen is down or not
        "color": DEFAULT_COLOR,  # current "color" used to draw
        "environment": {"width":columns,"height":lines},  # variables: a mapping str -> int
        "pc": 10,  # program counter: next instruction to execute. Set to None when done
        "program": program,
        # program being executed: a mapping int -> Tuple[int, List[Union[int, str]]],
        # where the first tuple element is the instruction opcode and the second element
        # is a list of its arguments (each of which are either an integer or a variable
        # name)
    }
