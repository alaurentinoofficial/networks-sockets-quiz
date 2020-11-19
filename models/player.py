class Player():
    ip: str
    port: int
    point: float

    def __init__(self, ip: str, port: int, point: float = 0.0):
        self.ip = ip
        self.port = port
        self.point = point
    
    def __str__(self):
        return f"Player(ip={self.ip}, port={self.port}, points={self.point})"
    
    def __repr__(self):
        return f"Player(ip={self.ip}, port={self.port}, points={self.point})"

    @property
    def address(self):
        return f"{self.ip}:{self.port}"

    def __eq__(self, other):
        if isinstance(other, Player):
            return self.address == other.address
        elif type(other) is str:
            return self.address == other
        else:
            return False