class Settings():
    """ 存储《外星人入侵》的所有设置的类 """
    def __init__(self):
        """ 初始化游戏的设置 """
        #  屏幕设置
        self.screen_width = 800
        self.screen_height = 1000
        # 背景颜色
        self.bg_color = (230, 230, 230)
        # 飞船的移动速度
        self.ship_speed_factor = 1.5

        # 子弹设置
        self.bullet_speed_factor = 1 #速度
        self.bullet_width = 3 #宽
        self.bullet_height = 15 #高
        self.bullet_color = 60, 60, 60 #颜色
        self.bullets_allowed=6

        # 外星人设置
        self.alien_speed_factor =1
