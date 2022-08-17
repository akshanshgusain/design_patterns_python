class GPSNavigator:
    def __init__(self, manual_router: str = "221b, Baker Street, London  to Scotland Yard, 8-10 Broadway, London"):
        self.route: str = manual_router

    def get_router(self) -> str:
        return self.route
