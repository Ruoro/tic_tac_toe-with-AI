class InvalidGameState (Exception):
    """Raised when Gamestate is invalid"""


class InvalidMove(Exception):
    """Raised when the move is invalid."""

class UnknownGameScore(Exception):
    """Raised when the game score is unknown."""