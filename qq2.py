import base64
img='TnpFd01USTBORFkwTVRBd016UXpPRFE1LlhydjQ4US5OdEE3aXk0OU9KM1VvOWpoNjBHTFE0WFJRWVk='

x = base64.b64decode(img)
print(str(x))