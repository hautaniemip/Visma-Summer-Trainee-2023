from parser import Parser
from URI import URI

class Client:
    def __init__(self):
        pass

    def run(self):
        while True:
            uri = input("Enter URI (leave empty to exit): ")

            if uri == "":
                break

            parsedURI = Parser.parseURI(uri)
            self.printURI(parsedURI)



    def printURI(self, parsedURI: URI):
        if parsedURI == None:
            return

        print("URI:")
        print(f"Path: {parsedURI.getPath()}")
        print("Parameters:")

        for param in parsedURI.getParams():
            print(f"- {param[0]}: {param[1]}")




if __name__ == "__main__":
    client = Client()
    client.run()
