import eyed3
m=eyed3.load('Music/明年今日.mp3')
print([i for i in dir(m.info)])
print(m.tag.title)