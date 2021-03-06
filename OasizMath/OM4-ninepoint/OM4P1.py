from manimlib.imports import *


class OM4P1(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE
        },
    }

    def construct(self):
        A = Dot([-1.07, 4.35, 0], color=RED_E,radius=0.06)
        B = Dot([-3.49, -1.68, 0], color=RED_E,radius=0.06)
        C = Dot([6.16, -2.89, 0], color=RED_E,radius=0.06)
        HA = Dot([-1.86, -1.88, 0], color=RED_E,radius=0.06)
        HB = Dot([0.73, 2.54, 0], color=RED_E,radius=0.06)
        HC = Dot([-2.57, 0.62, 0], color=RED_E,radius=0.06)
        H = Dot([-1.59, 0.22, 0], color=RED_E,radius=0.06)
        GA = Dot([1.33, -2.28, 0], color=RED_E,radius=0.06)
        GB = Dot([2.54, 0.73, 0], color=RED_E,radius=0.06)
        GC = Dot([-2.28, 1.33, 0], color=RED_E,radius=0.06)
        G = Dot([0.53, -0.07, 0], color=RED_E,radius=0.06)
        O = Dot([1.59, -0.22, 0], color=RED_E,radius=0.06)
        gg = VGroup(A, B, C, HA, HB, HC, H, GA, GB, GC, G, O)
        gg.shift(LEFT + DOWN * 0.5)
        tr1 = self.Triangle(A, B, C)
        self.play(ShowCreation(tr1))
        self.wait()
        t1 = TextMobject("对于任意三角形，其垂心H，重心G，外心O共线，且HG=2GO", color=BLACK).scale(0.7).next_to([-6, -3, 0])
        t2 = TextMobject("这条线我们称作欧拉线", color=BLACK).scale(0.7).next_to([-6, -3, 0])
        self.play(Write(t1))
        self.wait()
        self.play(Uncreate(t1))
        self.wait()
        AHA = self.fl(A, HA)
        BHB = self.fl(B, HB)
        CHC = self.fl(C, HC)
        thg = VGroup(AHA, BHB, CHC)
        AGA = self.fl(A, GA)
        BGB = self.fl(B, GB)
        CGC = self.fl(C, GC)
        tgg = VGroup(AGA, BGB, CGC)
        GAO = self.fl(GA, O)
        GBO = self.fl(GB, O)
        GCO = self.fl(GC, O)
        ogg = VGroup(GAO, GBO, GCO)
        lineg=VGroup(thg,tgg,ogg)
        dotg=VGroup(H,G,O)
        HO=Line(H.get_center(),O.get_center(),color=GREEN_E)
        txh=TextMobject("H",color=BLACK).scale(0.7).next_to(H,LEFT*1.5+DOWN*0.1)
        txg=TextMobject("G",color=BLACK).scale(0.7).next_to(G,DOWN*0.3+LEFT*0.3)
        txo=TextMobject("O",color=BLACK).scale(0.7).next_to(O,RIGHT)
        tg=VGroup(txh,txg,txo)
        self.play(ShowCreation(thg),rate_func=linear,run_time=2)
        self.play(ShowCreation(H))
        self.play(Write(txh))
        self.wait()
        self.play(ShowCreation(tgg),rate_func=linear,run_time=2)
        self.play(ShowCreation(G))
        self.play(Write(txg))
        self.wait()
        self.play(ShowCreation(ogg),rate_func=linear,run_time=2)
        self.play(ShowCreation(O))
        self.play(Write(txo))
        self.wait()
        self.play(lineg.set_color,BLUE_B)
        self.play(dotg.set_color,RED_E)
        self.play(ShowCreation(HO))
        self.wait()
        t3=TextMobject("HG=2GO",color=BLACK).scale(0.7).shift(UP)
        self.play(ReplacementTransform(tg,t3))
        self.play(Write(t2))
        self.wait(2)
        self.play(Uncreate(t2))
        self.play(FadeOut(t3))

    def Triangle(self, X, Y, Z):
        return Polygon(X.get_center(), Y.get_center(), Z.get_center(),color=GREEN_B)

    def fl(self, X, Y):
        return Line(X.get_center(), Y.get_center(),color=BLUE_E,stroke_width=3)