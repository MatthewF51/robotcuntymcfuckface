def forward(distance, velocity):
    return f"Move Forward {distance} meters {velocity} m/s"


def backward(distance, velocity):
    return f"Move Backward {distance} meters {velocity} m/s"


def turn_left(degrees):
    return f"Turn Left {degrees} degrees"


def turn_right(degrees):
    return f"Turn Right {degrees} degrees"


COMMANDS = {
    "Forward": {
        "func": forward,
        "inputs": {"Distance (meters)": "distance"
        , "Velocity (m/s)": "velocity"},
    },
    "Backward": {
        "func": backward,
        "inputs": {"Distance (meters)": "distance"
        , "Velocity (m/s)": "velocity"},
    },
    "Turn Left": {
        "func": turn_left,
        "inputs": {"Degrees": "degrees"},
    },
    "Turn Right": {
        "func": turn_right,
        "inputs": {"Degrees": "degrees"},
    },
}

colour = "#FF5733"
