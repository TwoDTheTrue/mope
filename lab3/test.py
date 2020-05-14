from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from random import randint
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.core.text import LabelBase
from math import sqrt, fabs
from numpy import linalg

Window.maximize()
LabelBase.register(name='Got',
                   fn_regular='BenguiatGothicC_Bold.ttf')

Window.clearcolor = (1, .58, .3, 1)


class Laba2App(App):


    def build(self):
        MainBoxL = BoxLayout()
        m = 4
        x1min = -25
        x1max = 5
        x2min = -15
        x2max = 35
        x3min = -5
        x3max = 60
        Ymax = 200 + round((x1max + x2max + x3max)/3)
        Ymin = 200 + round((x1min + x2min + x3min)/3)
        BoxL = BoxLayout(orientation = 'vertical')
        RightBoxL = BoxLayout(orientation='vertical',
                              spacing = 20,
                              padding = [10,10])
        GridL1 = GridLayout(
            cols = 3,
            padding = [10,0],
            spacing = 15,
            size_hint = [3/(m+3),1]
        )

        GridL1.add_widget(Label(
            text = "X1", font_size = 35, bold='True', outline_width=2, outline_color=[0,0,0]
        ))
        GridL1.add_widget(Label(
            text="X2", font_size = 35,bold='True', outline_width=2, outline_color=[0,0,0]
        ))
        GridL1.add_widget(Label(
            text="X3", font_size=35,bold='True', outline_width=2, outline_color=[0,0,0]
        ))
        GridL1.add_widget(Button(
            text=str(x1min), font_size = 25, background_color = [.6,.7,.9,1]
        ))
        GridL1.add_widget(Button(
            text=str(x2min), font_size = 25, background_color = [.6,.7,.9,1]
        ))
        GridL1.add_widget(Button(
            text=str(x3min), font_size = 25, background_color = [.6,.7,.9,1]
        ))
        GridL1.add_widget(Button(
            text=str(x1min), font_size = 25, background_color = [.6,.7,.9,1]
        ))
        GridL1.add_widget(Button(
            text=str(x2max), font_size = 25, background_color = [.6,.7,.9,1]
        ))
        GridL1.add_widget(Button(
            text=str(x3max), font_size=25, background_color=[.6, .7, .9, 1]
        ))
        GridL1.add_widget(Button(
            text=str(x1max), font_size=25, background_color=[.6, .7, .9, 1]
        ))
        GridL1.add_widget(Button(
            text=str(x2min), font_size=25, background_color=[.6, .7, .9, 1]
        ))
        GridL1.add_widget(Button(
            text=str(x3max), font_size=25, background_color=[.6, .7, .9, 1]
        ))
        GridL1.add_widget(Button(
            text=str(x1max), font_size=25, background_color=[.6, .7, .9, 1]
        ))
        GridL1.add_widget(Button(
            text=str(x2max), font_size=25, background_color=[.6, .7, .9, 1]
        ))
        GridL1.add_widget(Button(
            text=str(x3min), font_size=25, background_color=[.6, .7, .9, 1]
        ))


        GridL2 = GridLayout(
            rows = 5,
            cols = m,
            padding = [10,0],
            spacing = 15,
            size_hint = [m/(m+2),1]
        )

        for i in range(m):
            GridL2.add_widget(Label(
                text = "Y"+str(i+1), font_size = 35, bold='True', outline_width=2, outline_color=[0,0,0]
            ))
        BoxL1 = BoxLayout(
            padding=[15, 0, 15, 15],
            spacing=20
        )

        grid = GridLayout(cols=4,
                          size_hint_y=.6)

        gridGp = GridLayout(cols=2,
                            size_hint_y=.1)
        def coef(y_average, sum_s):
            mx1 = (2*(-1) + 2*1)/4
            mx2 = (2*(-1) + 2*1)/4
            mx3 = (2 * (-1) + 2 * 1) / 4
            my = sum(y_average)/4
            a1 = ((-1)*y_average[0] + (-1)*y_average[1] + 1*y_average[2] + 1*y_average[3])/4
            a2 = ((-1)*y_average[0] + 1*y_average[1] + (-1)*y_average[2] + 1*y_average[3])/4
            a3 = ((-1)*y_average[0] + 1*y_average[1] + 1*y_average[2] + (-1)*y_average[3])/4
            a11 = ((-1)**2 + 1**2)/2
            a22 = (1**2+(-1)**2)/2
            a33 = (1 ** 2 + (-1) ** 2) / 2
            a12 = ((-1)*(-1)+(-1)*1+1*(-1)+1*1)/4
            a13 = ((-1) * (-1) + (-1) * 1 + 1 * 1 + 1 * (-1)) / 4
            a23 = ((-1) * (-1) + 1 * 1 + (-1) * 1 + 1 * (-1)) / 4
            denominator =  linalg.det([[1,mx1,mx2,mx3],
                                      [mx1,a11,a12,a13],
                                      [mx2,a12,a22,a23],
                                      [mx3,a13,a23,a33]])
            b0 = linalg.det([[my,mx1,mx2,mx3],
                             [a1,a11,a12,a13],
                             [a2,a12,a22,a23],
                             [a3,a13,a23,a33]]) / denominator
            b1 = linalg.det([[1,my,mx2,mx3],
                             [mx1,a1,a12,a13],
                             [mx2,a2,a22,a23],
                             [mx3,a3,a23,a33]]) / denominator
            b2 = linalg.det([[1,mx1,my,mx3],
                             [mx1,a11,a1,a13],
                             [mx2,a12,a2,a23],
                             [mx3,a13,a3,a33]]) / denominator
            b3 = linalg.det([[1,mx1,mx2,my],
                             [mx1,a11,a12,a1],
                             [mx2, a12,a22,a2],
                             [mx3, a13,a23,a3]]) / denominator
            coefs = []
            coefs.append(b0)
            coefs.append(b1)
            coefs.append(b2)
            coefs.append(b3)

            grid.add_widget(Label(text = "b0 = {0:+.2f}".format(b0),
                                  font_size = 25))
            grid.add_widget(Label(text="b1 = {0:+.2f}".format(b1),
                                 font_size=25))
            grid.add_widget(Label(text="b2 = {0:+.2f}".format(b2),
                                 font_size=25))
            grid.add_widget(Label(text="b3 = {0:+.2f}".format(b3),
                                  font_size=25))
            deltaX1 = fabs(x1max- x1min)/2
            deltaX2 = fabs(x2max - x2min)/2
            deltaX3 = fabs(x3max - x3min) / 2
            x10 = (x1max + x1min)/2
            x20 = (x2max + x2min)/2
            x30 = (x3max + x3min)/2

            a0 = b0 - b1 * x10/deltaX1 - b2 * x20/deltaX2 - b3 * x30/deltaX3
            a1 = b1/deltaX1
            a2 = b2/deltaX2
            a3 = b3/deltaX3
            grid.add_widget(Label(text="a0 = {0:+.2f}".format(a0),
                                 font_size=25))
            grid.add_widget(Label(text="a1 = {0:+.2f}".format(a1),
                                 font_size=25))
            grid.add_widget(Label(text="a2 = {0:+.2f}".format(a2),
                                 font_size=25))
            grid.add_widget(Label(text="a3 = {0:+.2f}".format(a3),
                                  font_size=25))

            grid.add_widget(Label(text="y1 = {0:.2f}".format(y_average[0]),
                                  font_size=25))
            grid.add_widget(Label(text="y2 = {0:.2f}".format(y_average[1]),
                                  font_size=25))
            grid.add_widget(Label(text="y3 = {0:.2f}".format(y_average[2]),
                                  font_size=25))
            grid.add_widget(Label(text="y4 = {0:.2f}".format(y_average[3]),
                                  font_size=25))


            RightBoxL.add_widget(Label(text="b0 - b1 - b2 - b3 = {0:.2f}".format(b0 - b1 - b2 - b3),
                                       font_size=25, size_hint_y = 0.05))
            RightBoxL.add_widget(Label(text="a0 - 25a1 - 15a2 - 5a3 = {0:.2f}".format(a0 + x1min * a1 + x2min * a2 + x3min * a3),
                                       font_size=25, size_hint_y = 0.05))

            RightBoxL.add_widget(Label(text="b0 - b1 + b2 + b3 = {0:.2f}".format(b0 - b1 + b2 +b3),
                                       font_size=25, size_hint_y = 0.05))
            RightBoxL.add_widget(Label(text="a0 - 25a1 + 35a2 +60a3 = {0:.2f}".format(a0 + x1min * a1 + x2max * a2 + x3max*a3),
                                       font_size=25,size_hint_y = 0.05))

            RightBoxL.add_widget(Label(text="b0 + b1 - b2 + b3 = {0:.2f}".format(b0 + b1 - b2 + b3),
                                       font_size=25,size_hint_y = 0.05))
            RightBoxL.add_widget(Label(text="a0 - 5a1 - 15a2 + 60a3 = {0:.2f}".format(a0 + x1max * a1 + x2min * a2 + x3max*a3),
                                       font_size=25,size_hint_y = 0.05))

            RightBoxL.add_widget(Label(text="b0 + b1 + b2 - b3 = {0:.2f}".format(b0 + b1 + b2 - b3),
                                       font_size=25,size_hint_y = 0.05))
            RightBoxL.add_widget(Label(text="a0 - 5a1 + 35a2 - 5a3 = {0:.2f}".format(a0 + x1max * a1 + x2max * a2 + x3min * a3),
                      font_size=25,size_hint_y = 0.05))
            BoxL.add_widget(grid)
            BoxL.add_widget(Label(text="y = {0:+.2f} {1:+.2f}*X1н {2:+.2f}*X2н {3:+.2f}*X3н".format(b0, b1, b2, b3),
                                       font_size=25,size_hint_y = 0.15))
            BoxL.add_widget(Label(text="y = {0:+.2f}{1:+.2f}*X1{2:+.2f}*X2{3:+.2f}*X3".format(a0, a1, a2, a3),
                                  font_size=25, size_hint_y=0.15))
            student(m,y_average,sum_s, coefs)
        
        def calculate(m,y):
            y_average = []
            dispertion = []
            for q in range(4):
                y_average.append(sum(y[q])/m)
                dispertion_current = 0
                for h in range(m):
                    dispertion_current += (y[q][h]-y_average[q])**2
                dispertion.append(dispertion_current/m)
            Gp = max(dispertion)/sum(dispertion)
            Gt = 0.25
            if m==3:
                Gt = 0.6841
            elif m == 4:
                Gt = 0.6287
            elif m == 5:
                Gt = 0.5892
            elif m == 6:
                Gt = 0.5598
            elif m == 7:
                Gt = 0.5365
            elif m == 8:
                Gt = 0.5175
            elif m == 9:
                Gt = 0.5017
            elif m == 10:
                Gt = 0.4884
            else:
                start()
            if Gp < Gt:
                gridGp.add_widget(Label(text="Gp = {0:.2f}".format(Gp),
                                      font_size=25))
                gridGp.add_widget(Label(text="Gt = {0:.2f}".format(Gt),
                                        font_size=25))

                RightBoxL.add_widget(gridGp)
                coef(y_average,sum(dispertion))
            else:
                add_y(m,y)

        gridy = GridLayout(cols=2,
                           spacing=15,
                           padding=[10, 10])
        def student(m, y_average, sum_s,coefs):
            S2b = sum_s/4
            Sbeta = S2b/(4*m)
            SB = sqrt(Sbeta)
            Beta = []
            Beta.append(sum(y_average)/4)
            Beta.append((y_average[0]*(-1)+y_average[1]*(-1)+y_average[2]*1+y_average[3]*1)/4)
            Beta.append((y_average[0] * (-1) + y_average[1] * 1 + y_average[2] * (-1) + y_average[3] * 1) / 4)
            Beta.append((y_average[0] * (-1) + y_average[1] * 1 + y_average[2] * 1 + y_average[3] * (-1)) / 4)
            tx = []
            tx.append(Beta[0]/SB)
            tx.append(Beta[1]/SB)
            tx.append(Beta[2]/SB)
            tx.append(Beta[3]/SB)
            t = 1.960
            if m == 2:
                t = 2.776
            elif m == 3:
                t = 2.306
            elif m == 4:
                t = 2.179
            elif m == 5:
                t = 2.145
            elif m == 6:
                t = 2.086
            elif m == 7:
                t = 2.064
            elif m == 8:
                t = 2.048
            RightBoxL.add_widget(Label(text="t = {0:.2f}".format(t),
                                        font_size=25, size_hint_y = .2))
            gridt = GridLayout(cols = 4,spacing = 5,
                               size_hint_y = .3)
            eq = 'y = '
            eq_index = []
            eq += '{0:+.2f}'.format(coefs[0])
            gridt.add_widget(Label(text="t{0} = {1:.2f}".format(0, tx[0]),
                                   font_size=25))
            Xij = [[-1,-1,-1],
                   [-1, 1, 1],
                   [1, -1, 1],
                   [1, 1, -1]]

            for i in range(1,4):
                if tx[i] > t:
                    eq_index.append(i)
                    eq += "{0:+.2f}*X{1}н".format(coefs[i],i)
                gridt.add_widget(Label(text="t{0} = {1:.2f}".format(i,tx[i]),
                                        font_size=25))
            RightBoxL.add_widget(Label(text=eq, font_size=25, size_hint_y=.2))
            sum_st = []

            for i in range(4):
                current_sum = coefs[0]
                temp = '{0:+.2f}'.format(coefs[0])
                for j in range(len(eq_index)):
                    current_sum += coefs[eq_index[j]]*Xij[i][eq_index[j]-1]
                    temp += '{0:+.2f}'.format(coefs[eq_index[j]]*Xij[i][eq_index[j]-1])
                sum_st.append(current_sum)
                gridy.add_widget(Label(text="y{0} = {1} = {2:.2f}".format(i+1, temp, current_sum),
                                      font_size=25))

            RightBoxL.add_widget(gridt)
            RightBoxL.add_widget(gridy)
            fisher(m,len(eq_index)+1,sum_st,y_average, Sbeta)

        def fisher(m,d,sum_st,y_average,Sbeta):
            Sad = 0
            for i in range(4):
                Sad += (sum_st[i]-y_average[i])**2
            Sad *= m/(4-d)
            Fp = Sad/Sbeta
            Ftable = [[6.6,4.1,3.5,3.2,3.1,3.0],
                      [6.9,4.5,3.9,3.6,3.5,3.4],
                      [7.7,5.3,4.8,4.5,4.4,4.3]]
            Ft = Ftable[d-1][m-2]
            gridy.add_widget(Label(text="Fp = {0:.2f}".format(Fp),
                                        font_size=25))
            gridy.add_widget(Label(text="Ft = {0:.2f}".format(Ft),
                                   font_size=25))
            if Fp > Ft:
                RightBoxL.add_widget(Label(text = 'Рівняння регресії неадекватно оригіналу',font_size=25, size_hint_y = .3))


        flag = []
        def add_y(m,y):
            if m == 13:
                start()
            m += 1
            y[0].append(randint(Ymin, Ymax))
            y[1].append(randint(Ymin, Ymax))
            y[2].append(randint(Ymin, Ymax))
            y[3].append(randint(Ymin, Ymax))
            flag.append(GridLayout(
                cols=1,
                spacing=15,
            ))

            flag[len(flag)-1].add_widget(Label(
                text="Y" + str(m), font_size=35,bold='True', outline_width=2, outline_color=[0,0,0]
            ))
            flag[len(flag)-1].add_widget(Button(
                text=str(y[0][m - 1]), font_size=25, background_color=[.6, .7, .9, 1]
            ))
            flag[len(flag)-1].add_widget(Button(
                text=str(y[1][m - 1]), font_size=25, background_color=[.6, .7, .9, 1]
            ))
            flag[len(flag)-1].add_widget(Button(
                text=str(y[2][m - 1]), font_size=25, background_color=[.6, .7, .9, 1]
            ))
            flag[len(flag) - 1].add_widget(Button(
                text=str(y[3][m - 1]), font_size=25, background_color=[.6, .7, .9, 1]
            ))

            calculate(m,y)


        y = []
        def start():
            if len(y) > 0:
                y.clear()
            for j in range(4):
                y_row = []
                for k in range(m):
                    y_current = randint(Ymin,Ymax)
                    y_row.append(y_current)
                    GridL2.add_widget(Button(
                            text=str(y_current), font_size=25, background_color=[.6, .7, .9, 1]
                        ))
                y.append(y_row)
            BoxL.add_widget(BoxL1)
            calculate(m, y)

        start()
        BoxL1.add_widget(GridL1)
        BoxL1.add_widget(GridL2)



        if len(flag) > 0:
            GridL3 = GridLayout(
                spacing = 15,
                cols = len(flag),
                size_hint = [len(flag)/(m+2+len(flag)),1]
            )
            for d in range(len(flag)):
                GridL3.add_widget(flag[d])
            BoxL1.add_widget(GridL3)
        MainBoxL.add_widget(BoxL)
        MainBoxL.add_widget(RightBoxL)
        return MainBoxL
if __name__ == "__main__":
    Laba2App().run()