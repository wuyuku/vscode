from dingtalkchatbot.chatbot import DingtalkChatbot
import time

#  WebHook地址 机器人1号
webhook = 'https://oapi.dingtalk.com/robot/send?access_token=cb4da5437cb50fcb670d27186193efeddbe6032295b10f82b67128a7a43ce07f'
# 初始化机器人小丁
xiaoding = DingtalkChatbot(webhook)
# Text消息@所有人
xiaoding.send_text(msg='傻子是夸奖？第一次听说', is_at_all=True)
time.sleep(10)

# 机器人2号
webhook = 'https://oapi.dingtalk.com/robot/send?access_token=b56ec8d3881b3ec1b346795f0a94f948c2d759915eadc26dddafe886a79d12be'
# 初始化机器人小丁
xiaoding = DingtalkChatbot(webhook)
# Text消息@所有人
xiaoding.send_text(msg='3号4号你们别闹了', is_at_all=True)
time.sleep(10)



# 机器人3号
webhook = 'https://oapi.dingtalk.com/robot/send?access_token=dda02047993a5043fe7173738ab8fbff699e7406b50d1aaacf3f206549e8a196'
# 初始化机器人小丁
xiaoding = DingtalkChatbot(webhook)
# Text消息@所有人
xiaoding.send_text(msg='4号你想死吗', is_at_all=True)
time.sleep(10)

# 机器人4号
webhook = 'https://oapi.dingtalk.com/robot/send?access_token=f11007a157713951d609f493a11919a657e6d0f19a5191200fa09283e4d09449'
# 初始化机器人小丁
xiaoding = DingtalkChatbot(webhook)
# Text消息@所有人
xiaoding.send_text(msg='来打我啊', is_at_all=True)
