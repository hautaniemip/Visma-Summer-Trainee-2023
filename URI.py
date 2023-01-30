class URI:
    """
    A class that represents a simplified structure of URI
    """

    scheme: str
    path: str
    params: dict

    def __init__(self, scheme: str, path: str, params: dict):
        self.scheme = scheme
        self.path = path
        self.params = params

    def getScheme(self) -> str:
        return self.scheme

    def getPath(self) -> str:
        return self.path

    def getParams(self) -> dict:
        return self.params
