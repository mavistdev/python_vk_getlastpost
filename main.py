import vk_api
from vk_api.audio import VkAudio

token = vk_api.VkApi(token = "")
vk = token.get_api()

# vk.messages.send(user_id = "", message = "TEXT", random_id = 0) # Вернет message ID
# print(vk.wall.post(message='vk_api')) # вернет post id
tools = vk_api.VkTools(token)

posts = vk.wall.get(owner_id='', count=1)
print(posts)
posts = posts['items']
posts_strings = [post['text'] for post in posts]

comments_strings = []
for i in range(0, 200):
	i = str(i)
	comments_strings.append(i)


with open('output.txt', 'w', encoding='utf-8') as f:
    for p, c in zip(posts_strings, comments_strings):
        f.write('[POST] ' + p + '\n')
