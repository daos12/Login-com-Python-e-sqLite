#Importando as bibliotecas
import DataBaser
import Functions
import re #Verifica o email
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from Functions import verificaEmail

#Criando janela inicial
jan = Tk()
jan.title("DAOs System - Acess Panel")
jan.geometry("600x300")
jan.configure(background="white")
jan.resizable(width=False, height=False) #Bloqueando a alteração das dimensões da janela 
jan.attributes("-alpha", 0.9) #Nivel de transparencia da janela
jan.iconbitmap(default="img/LogoIcon.ico") #Adiciona o icone 

#=== Carregamento das imagens ====================================================================
logo = PhotoImage(file="img/logo.png")

#=== Funções =====================================================================================
def Register():
    LoginButton.place(x=5000) #Removendo o botão login
    RegisterButton.place(x=5000) #Removendo o botão registro
    
    #Inserindo Widgets de Cadastro
    NomeLabel = Label(RightFrame, text="Name: ", font=("Century Gothic",20), bg="MIDNIGHTBLUE", fg="White")
    NomeLabel.place(x=25, y=25)
    
    NomeEntry = ttk.Entry(RightFrame, width=30)
    NomeEntry.place(x=175, y=40)
    
    EmailLabel = Label(RightFrame, text="Email: ", font=("Century Gothic",20), bg="MIDNIGHTBLUE", fg="White")
    EmailLabel.place(x=25, y=70)
    
    EmailEntry = ttk.Entry(RightFrame, width=30)
    EmailEntry.place(x=175, y=80)
    
    def ReturnToLogin():
        NomeLabel.place(x=5000)
        NomeEntry.place(x=5000)
        EmailLabel.place(x=5000)
        EmailEntry.place(x=5000)
        ReturnButton1.place(x=5000)
        LoginButton.place(x=110,y=225)
        
    
    ReturnButton1 = ttk.Button(RightFrame, text="Return", width=20, command=ReturnToLogin)
    ReturnButton1.place(x=110,y=225)
    
    def RegisterToDataBase():
        name        = NomeEntry.get()
        email       = EmailEntry.get()
        user        = UserEntry.get()
        password    = passEntry.get()
        
        if verificaEmail(email):
            print("O e-mail é válido.")
            if(name == "" or email == "" or user == "" or password == ""):
                messagebox.showerror(title="Register Error", message="Preencha Todos os Campos")
            else:
                DataBaser.cursor.execute("""
                INSERT INTO Users(name, email, user, password) VALUES(?,?,?,?)
                """, (name, email, user, password))
                DataBaser.conn.commit() #Para salvar as alterações
                messagebox.showinfo(title="Register Info", message="Account Created")
        else:
            print("O e-mail é inválido.")
        

    RegisterButton1 = ttk.Button(RightFrame, text="Register", width=20, command=RegisterToDataBase)
    RegisterButton1.place(x=110,y=260)


def Login():
    user        = UserEntry.get()
    password    = passEntry.get()
    
    DataBaser.cursor.execute("""
    SELECT * FROM Users
    WHERE (user = ? AND password = ?)
    """,(user,password))
    print("Selecionado")
    
    verifyLogin = DataBaser.cursor.fetchone() #Vai realizar a verificação do login
    
    # Demostrar como e realizado o tratamento de erros para os alunos com os exemplos de if e try a seguir
    
    # if(user in verifyLogin and password in verifyLogin):
    #     messagebox.showinfo(title="Login Info", message="Access confirmed, welcome!")
    # else:
    #     messagebox.showinfo(title="Login Info",message="Access Denied!")
    
    try:
        if(user in verifyLogin and password in verifyLogin):
            messagebox.showinfo(title="Login Info", message="Access confirmed, welcome!")
    except:
        messagebox.showinfo(title="Login Info",message="Access Denied!")

#=== Widgets =====================================================================================
LeftFrame = Frame(jan, width=200, height=300, bg="MIDNIGHTBLUE",relief="raise") #Dividindo a janela em duas
LeftFrame.pack(side=LEFT) #Localização do quadrado

RightFrame = Frame(jan, width=395, height=300, bg="MIDNIGHTBLUE",relief="raise") #Dividindo a janela em duas
RightFrame.pack(side=RIGHT) #Localização do quadrado

LogoLabel = Label(LeftFrame, image=logo, bg="MIDNIGHTBLUE")
LogoLabel.place(x=50,y=100)

UserLabel = Label(RightFrame,text="Username: ", font=("Century Gothic",20), bg="MIDNIGHTBLUE", fg="White")
UserLabel.place(x=25, y=110)

UserEntry = ttk.Entry(RightFrame, width=30)
UserEntry.place(x=175,y=120)

PassLabel = Label(RightFrame,text="Password: ", font=("Century Gothic",20), bg="MIDNIGHTBLUE", fg="White")
PassLabel.place(x=25, y=150)

passEntry = ttk.Entry(RightFrame, width=30, show="•")
passEntry.place(x=175,y=160)


#=== Botões =====================================================================================
LoginButton = ttk.Button(RightFrame, text="Login", width=20, command=Login)
LoginButton.place(x=110,y=225)

RegisterButton = ttk.Button(RightFrame, text="Register", width=20, command=Register)
RegisterButton.place(x=110,y=260)

jan.mainloop() #Finalizando as configurações da janela