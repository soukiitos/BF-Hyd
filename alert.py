from pushbullet import Pushbullet

API_KEY = "o.JlZQP1qwPsEXx9QTi5DTBsqyceIMbgfj"

file = "message.txt"

with open(file, mode='r') as f:
    text = f.read()

pb = Pushbullet(API_KEY)
push = pb.push_note('Please Remember', text)
