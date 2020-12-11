# TanksMP
A Multiplayer Implementation of Tanks (Converted from Code-Project.org's single player tanks game)

MUST HAVE PYTHON3, AND PYGAME INSTALLED.

INSTRUCTIONS
  1. Install Python 3.9.1 from Python's website https://www.python.org/downloads/release/python-391/
  2. Ensure that python 3.9.1 is in PATH (go to environment variables to check)
  3. go to powershell/gitbash/etc. (this will be refered to as terminal for the rest of the instructions) and type 'pip install pygame'
  4. navigate to the folder that contains tank-game folder through terminal
  5. type 'python server.py' to run the server
  6. If you want to connect to something other than localhost, go into network.py and modify the 'HOST' variable at the top to whatever IP address you want to connect to;  The server must be running on the machine w/ this IP.
  7. type 'python tank.py' in terminal to run the client
  8. press 'play' to begin matchmaking; since it is unlikely anyone else is connecting, if you want to test this out just run tank.py again on the same machine and press play.  This will match you with yourself
