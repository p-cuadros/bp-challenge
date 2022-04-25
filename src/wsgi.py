from __init__ import app as server
import controller_devops

if __name__ == "__main__":
    server.run( debug = True, port = 5000)