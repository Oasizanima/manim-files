from manimlib.imports import *


class PClass:
    def __init__(self, name, attr, words, w2):
        self.name = name
        self.attr = attr
        self.words = words
        self.w2 = w2


class LSP(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE
        },
    }

    def construct(self):
        a = {}
        a[0] = PClass("猫三郎", "lsp", "1+1=2!", "0.jpg")
        a[1] = PClass("小杰", "lsp", "你是要挑战我的剑法吗", "1.png")
        a[2] = PClass("绿洲", "超纯洁", "我爱你们", "2.jpg")
        a[3] = PClass("小小板", "lsp", "键盘被我吃了我只能发表情.jpg", "3.png")
        a[4] = PClass("Excalibur", "lsp", "我是本群的提醒手冲小助手~", "4.jpg")
        a[5] = PClass("污喵汪", "lsp", "猫三郎呢出来下锅", "5.jpg")
        a[6] = PClass("SwetyCore", "lsp", "我爱绿洲~", "6.jpg")
        a[7] = PClass("吵闹", "lsp", "哼！哼！啊啊啊啊啊啊啊啊啊！", "7.png")
        a[8] = PClass("卡卡", "lsp", "爬！", "8.jpg")

        t1 = TextMobject("LSP图形类库v1.0", background_stroke_width=0)
        t1.set_color_by_gradient(YELLOW_B, YELLOW_E, BLUE_E, BLUE_B)
        self.play(Write(t1))
        self.play(t1.shift, LEFT * 4 + UP * 3)
        self.wait()
        self.play(FadeOut(t1))

        for i in range(9):
            self.profile(a[i], [-3, 2, 0])

    def profile(self, x, pos):
        na = TextMobject(x.name + "(" + x.attr + ")：", color=BLACK)
        na.next_to(pos, RIGHT + DOWN)
        self.play(Write(na))
        w = TextMobject(x.words, color=BLACK).next_to(na, DOWN)
        if x.words != "NONE":
            w.shift(RIGHT)
            self.play(ShowCreation(w))
        pic = ImageMobject(x.w2, height=2)
        if x.w2 != "NONE":
            pic.next_to(w, DOWN)
            self.play(FadeInFromLarge(pic))
        self.wait()
        v = VGroup(na, w)
        self.play(FadeOut(v))
        self.play(FadeOut(pic))
