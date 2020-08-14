from manimlib.imports import *


class OM3P1(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE
        },
    }

    def construct(self):
        A = Dot([-3.99, 0, 0], color=RED_E)
        B = Dot([-1.31, 0, 0], color=RED_E)

        AB=Line(A.get_center(),B.get_center(),color=BLUE_E)
        c=Circle(radius=0.5,color=GREEN_D,fill_color=GREEN_D,fill_opacity=0.5)
        abg=VGroup(AB,A,B)
        self.play(ShowCreation(abg))
        self.play(ShowCreation(c))
        t1=TextMobject("如何用直尺在不碰触圆的情况下将线段延长到另一端？", color=BLACK).scale(0.7).next_to([-6, -2, 0])
        t2=TextMobject("把纸折过来？\\\\把尺子掰弯？\\\\往左延伸，因为只要不停下来，道路就会无限延伸？\\\\在纸上造一个虫洞？\\\\把圆揭下来？", color=BLACK).scale(0.6).shift(RIGHT*3+UP*2.5)
        t3=TextMobject("为了解决这个问题，我们需要借助完全四边形", color=BLACK).scale(0.7).next_to([-6, -2, 0])
        self.play(Write(t1))
        self.wait(2)
        self.play(Write(t2),run_time=2)
        self.wait(2)
        self.play(t2.shift,LEFT*50,run_time=0.5)
        self.wait()
        self.play(ReplacementTransform(t1,t3))
        self.wait(2)