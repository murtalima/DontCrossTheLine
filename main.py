import time
import turtle
#Funcoes

def empate():
    turtle.color('green')
    style = ('Quantify', 30, 'italic')
    turtle.write('Empate!', font=style, align='center')
    turtle.hideturtle()
def vitoria_1():
    turtle.color('red')
    style = ('Quantify', 30, 'italic')
    turtle.write('Jogador 1 Venceu!', font=style, align='center')
    turtle.hideturtle()
def vitoria_2():
    turtle.color('blue')
    style = ('Quantify', 30, 'italic')
    turtle.write('Jogador 2 Venceu!', font=style, align='center')
    turtle.hideturtle()

def djogador1_cima():
    global direcao_jogador1
    if(direcao_jogador1!='s'):
        direcao_jogador1 = 'w'

def djogador1_baixo():
    global direcao_jogador1
    if (direcao_jogador1 != 'w'):
        direcao_jogador1 = 's'

def djogador1_direita():
    global direcao_jogador1
    if (direcao_jogador1 != 'a'):
        direcao_jogador1 = 'd'

def djogador1_esquerda():
    global direcao_jogador1
    if (direcao_jogador1 != 'd'):
        direcao_jogador1 = 'a'

def djogador2_cima():
    global direcao_jogador2
    if (direcao_jogador2 != 'Down'):
        direcao_jogador2 = 'Up'

def djogador2_baixo():
    global direcao_jogador2
    if (direcao_jogador2 != 'Up'):
        direcao_jogador2 = 'Down'

def djogador2_direita():
    global direcao_jogador2
    if (direcao_jogador2 != 'Left'):
        direcao_jogador2 = 'Right'

def djogador2_esquerda():
    global direcao_jogador2
    if (direcao_jogador2 != 'Right'):
        direcao_jogador2 = 'Left'
while(True):
    passo = 10
    wn = turtle.Screen()
    wn.title("Dont Cross The Line")
    wn.bgcolor("white")
    wn.setup(width=800, height=600)
    wn.tracer(0)

    # Jogador 1
    direcao_jogador1 = 'd'
    jogador1 = turtle.Turtle()
    jogador1.speed(0)
    jogador1.shape("square")
    jogador1.color("red")
    jogador1.shapesize(0.5,0.5)
    jogador1.penup()
    jogador1.goto(-350, 0)
    jogador1.pensize(11)
    jogador1.pendown()

    # Jogador 2
    global direcao_jogador2
    direcao_jogador2 = "Left"
    jogador2 = turtle.Turtle()
    jogador2.speed(0)
    jogador2.shape("square")
    jogador2.color("blue")
    jogador2.shapesize(0.5,0.5)
    jogador2.penup()
    jogador2.goto(350, 0)
    jogador2.pensize(11)
    jogador2.pendown()



    #Funcionalidade das teclas
    wn.listen()
    wn.onkeypress(djogador1_cima, "w")
    wn.onkeypress(djogador1_baixo, "s")
    wn.onkeypress(djogador1_direita, "d")
    wn.onkeypress(djogador1_esquerda, "a")
    wn.onkeypress(djogador2_cima, "Up")
    wn.onkeypress(djogador2_baixo, "Down")
    wn.onkeypress(djogador2_direita, "Right")
    wn.onkeypress(djogador2_esquerda, "Left")

    #main loop
    caminho_1=[]
    caminho_2=[]
    continuar = True
    while continuar:
        caminho_1.append([jogador1.xcor(),jogador1.ycor()])
        caminho_2.append([jogador2.xcor(), jogador2.ycor()])
        if(direcao_jogador1=="w"):
            y = jogador1.ycor()
            y+=passo
            jogador1.sety(y)
        elif (direcao_jogador1 == "s"):
            y = jogador1.ycor()
            y -= passo
            jogador1.sety(y)
        elif (direcao_jogador1 == "d"):
            x = jogador1.xcor()
            x += passo
            jogador1.setx(x)
        elif (direcao_jogador1 == "a"):
            x = jogador1.xcor()
            x -= passo
            jogador1.setx(x)

        if (direcao_jogador2 == "Up"):
            y = jogador2.ycor()
            y += passo
            jogador2.sety(y)
        elif (direcao_jogador2 == "Down"):
            y = jogador2.ycor()
            y -= passo
            jogador2.sety(y)
        elif (direcao_jogador2 == "Right"):
            x = jogador2.xcor()
            x += passo
            jogador2.setx(x)
        elif (direcao_jogador2 == "Left"):
            x = jogador2.xcor()
            x -= passo
            jogador2.setx(x)
        for etapas in caminho_1:
            if(jogador2.xcor()== etapas[0] and jogador2.ycor()== etapas[1]):
                vitoria_1()
                continuar = False
            if (jogador1.xcor() == etapas[0] and jogador1.ycor() == etapas[1]):
                vitoria_2()
                continuar = False
        for etapas in caminho_2:
            if(jogador1.xcor()== etapas[0] and jogador1.ycor()== etapas[1]):
                vitoria_2()
                continuar = False
            if (jogador2.xcor() == etapas[0] and jogador2.ycor() == etapas[1]):
                vitoria_1()
                continuar = False
        if(jogador1.ycor()>290 or jogador1.ycor() < -290 or jogador1.xcor()>390 or jogador1.xcor()<-390):
            vitoria_2()
            continuar = False
        if (jogador2.ycor() > 290 or jogador2.ycor() < -290 or jogador2.xcor() > 390 or jogador2.xcor() < -390):
            vitoria_1()
            continuar = False
        if(jogador1.xcor()== jogador2.xcor() and jogador1.ycor() == jogador2.ycor()):
            empate()
            continuar = False
        time.sleep(0.1)
        wn.update()
    time.sleep(3)
    wn.clear()









    #referencia https://www.youtube.com/watch?v=C6jJg9Zan7w