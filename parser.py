from URI import URI

class Parser:
    """
    A class for parsing URIs.
    Contains only static methods

    Methods
    -------
    parseURI(uri)
        parses the given URI
    """

    # __ALLOWED_PAHTS contain all paths that the parser supports
    __ALLOWED_PATHS = ["login", "confirm", "sign"]
    @staticmethod
    def parseURI(uri: str) -> URI:
        """
        Method used for parsing URI

        Arguments
        ---------
        uri: str
            a URI in string format using standard syntax

        Returns
        -------
        URI
            a parsed URI object
        """

        scheme = Parser.__parseScheme(uri)
        path = Parser.__parsePath(uri)
        params = Parser.__parseParams(uri)

        if scheme == None or path == None:
            print(f"Invalid URI: {uri}")
            return

        if scheme != "visma-identity":
            print(f"Scheme '{scheme}' is not allowed.")
            return

        if not path in Parser.__ALLOWED_PATHS:
            print(f"Path '{path}' is not allowed.")
            return

        if not Parser.__validateParams(path, params):
            print(f"Invalid parameters for path '{path}'.\nParameters: {params}")
            return

        return URI(scheme, path, params)

    @staticmethod
    def __parseScheme(uri: str) -> str:
        end = uri.find(":")

        if end == -1:
            return

        return uri[:end]

    @staticmethod
    def __parsePath(uri: str) -> str:
        start = uri.find("//")
        end = uri.find("?")

        if start == -1:
            return

        if end == -1:
            end = len(uri)

        return uri[start + 2:end]

    @staticmethod
    def __parseParams(uri: str) -> list:
        start = uri.find("?")
        params = []

        if start == -1:
            return params

        paramString = uri[start + 1:]

        for param in paramString.split("&"):
            [paramName, paramValue] = param.split("=")

            # Convert parameters with integer values to have actual integer value
            # Currently there is only one such parameter
            if paramName == "paymentnumber":
                paramValue = int(paramValue)

            params.append((paramName, paramValue))

        return params

    @staticmethod
    def __validateParams(path: str, params: list) -> bool:
        """
        Validates all parameters by calling the correct validating method based on path

        Arguments
        ---------
        path: str
            a path supported by parser
        params: list(tuple)
            a list of tuples for each parameter

        Returns
        -------
        bool
            return bool based on output of the coresponding validation method
            or False if path is not supported by parser
        """

        if path == "login":
            return Parser.__validateLoginParams(params)
        elif path == "confirm":
            return Parser.__validateConfirmParams(params)
        elif path == "sign":
            return Parser.__validateSignParams(params)

        return False

    @staticmethod
    def __validateLoginParams(params: list) -> bool:
        """
        Checks the amount of parameters and that they are correct for the path
        """

        isValid = True

        if len(params) != 1:
            isValid = False

        for param in params:
            #param[0] contains the name of the parameter
            if param[0] != "source":
                isValid = False

        return isValid


    @staticmethod
    def __validateConfirmParams(params: list) -> bool:
        """
        Checks the amount of parameters and that they are correct for the path
        """

        isValid = True

        if len(params) != 2:
            isValid = False

        for param in params:
            #param[0] contains the name of the parameter
            if param[0] != "source" and param[0] != "paymentnumber":
                isValid = False

        return isValid

    @staticmethod
    def __validateSignParams(params: list) -> bool:
        """
        Checks the amount of parameters and that they are correct for the path
        """

        isValid = True

        if len(params) != 2:
            isValid = False

        for param in params:
            #param[0] contains the name of the parameter
            if param[0] != "source" and param[0] != "documentid":
                isValid = False

        return isValid






if __name__ == "__main__":
    uri = Parser.parseURI("visma-identity://confirm?source=netvisor&paymentnumber=102226")
    print(uri.getScheme())
    print(uri.getPath())
    print(uri.getParams())
