from utils import send_command
from geometry_msgs.msg import Twist  # Importing correct message type

COMMANDS = {
    "Move Forward": {
        "function": lambda speed, distance: send_command(
            "/cmd_vel",
            Twist,
            linear_x=float(speed),
            angular_z=0.0,
            duration=float(distance) / float(speed)
        ),
        "inputs": {"Speed": "speed", "Distance": "distance"},
        "topic": "/cmd_vel",
        "msg_type": Twist  # Explicitly defining message type
    },
    "Move Backward": {
        "function": lambda speed, distance: send_command(
            "/cmd_vel",
            Twist,
            linear_x=-float(speed),
            angular_z=0.0,
            duration=float(distance) / float(speed)
        ),
        "inputs": {"Speed": "speed", "Distance": "distance"},
        "topic": "/cmd_vel",
        "msg_type": Twist
    },
    "Rotate Left": {
        "function": lambda speed, angle: send_command(
            "/cmd_vel",
            Twist,
            linear_x=0.0,
            angular_z=float(speed),
            duration=float(angle) / float(speed)
        ),
        "inputs": {"Speed": "speed", "Angle": "angle"},
        "topic": "/cmd_vel",
        "msg_type": Twist
    },
    "Rotate Right": {
        "function": lambda speed, angle: send_command(
            "/cmd_vel",
            Twist,
            linear_x=0.0,
            angular_z=-float(speed),
            duration=float(angle) / float(speed)
        ),
        "inputs": {"Speed": "speed", "Angle": "angle"},
        "topic": "/cmd_vel",
        "msg_type": Twist
    },
    "Stop": {
        "function": lambda: send_command(
            "/cmd_vel",
            Twist,
            linear_x=0.0,
            angular_z=0.0
        ),
        "inputs": {},
        "topic": "/cmd_vel",
        "msg_type": Twist
    }
}

colour = "#FF5733"  # Orange color for UI
