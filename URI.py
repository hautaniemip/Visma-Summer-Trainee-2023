class URI:
    """
    A class that presents a simplified structure of URI
    """

    scheme: str
    path: str
    params: list

    def __init__(self, scheme: str, path: str, params: list):
        self.scheme = scheme
        self.path = path
        self.params = params

    def getScheme(self) -> str:
        return self.scheme

    def getPath(self) -> str:
        return self.path

    def getParams(self) -> list:
        return self.params
