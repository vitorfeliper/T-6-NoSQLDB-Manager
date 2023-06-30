from Modules.DBM_Module import DataBaseManager, MarcaDAO, ModeloDAO, CarroDAO
from tkinter import Tk, Label, Entry, Button, Listbox, END, Toplevel

# Cria a janela principal
mainWindow = Tk()
mainWindow.geometry("640x480")  # Define a resolução inicial da janela
dbm = DataBaseManager()

# Inicializa as instâncias do DAO para cada coleção
marca_dao = None
modelo_dao = None
carro_dao = None

# Função para criar os DAOs com base nas coleções selecionadas
def create_daos():
    db_name = ct_db_Name.get()
    db_host = ct_db_Host.get()
    db_port = int(ct_db_Port.get())

    db_coll1 = CollName1.get()
    db_coll2 = CollName2.get()
    db_coll3 = CollName3.get()

    db = dbm.CreateDB(db_name, db_host, db_port)

    global marca_dao, modelo_dao, carro_dao
    marca_dao = MarcaDAO(db)
    modelo_dao = ModeloDAO(db)
    carro_dao = CarroDAO(db)

    print("DAOs criados com sucesso.")

# Função para adicionar uma marca
def add_marca():
    nome_marca = ct_marca_nome.get()
    marca = {'nome': nome_marca}
    marca_id = marca_dao.add(marca)
    print('Marca adicionada:', marca_id)

# Função para adicionar um modelo
def add_modelo():
    nome_modelo = ct_modelo_nome.get()
    id_marca = ct_modelo_marca_id.get()
    modelo = {'nome': nome_modelo, 'id_marca': id_marca}
    modelo_id = modelo_dao.add(modelo)
    print('Modelo adicionado:', modelo_id)

# Função para adicionar um carro
def add_carro():
    nome_carro = ct_carro_nome.get()
    id_modelo = ct_carro_modelo_id.get()
    carro = {'nome': nome_carro, 'id_modelo': id_modelo}
    carro_id = carro_dao.add(carro)
    print('Carro adicionado:', carro_id)

# Função para exibir todas as marcas
def show_marcas():
    marcas = marca_dao.getAll()
    lb_marcas.delete(0, END)
    for marca in marcas:
        lb_marcas.insert(END, marca['_id'])

# Função para exibir todos os modelos
def show_modelos():
    modelos = modelo_dao.getAll()
    lb_modelos.delete(0, END)
    for modelo in modelos:
        lb_modelos.insert(END, modelo['_id'])

# Função para exibir todos os carros
def show_carros():
    carros = carro_dao.getAll()
    lb_carros.delete(0, END)
    for carro in carros:
        lb_carros.insert(END, carro['_id'])

# Função para excluir uma marca
def delete_marca():
    marca_id = lb_marcas.get(lb_marcas.curselection())
    marca_dao.delete(marca_id)
    print('Marca excluída:', marca_id)

# Função para atualizar uma marca
def update_marca():
    marca_id = lb_marcas.get(lb_marcas.curselection())
    marca = marca_dao.get(marca_id)

    update_window = Toplevel(mainWindow)
    update_window.title("Atualizar Marca")
    update_window.geometry("300x200")

    # Campo de texto para o novo nome da marca
    lbl_novo_nome = Label(update_window, text="Novo nome:")
    lbl_novo_nome.pack()
    ct_novo_nome = Entry(update_window)
    ct_novo_nome.pack()

    # Preenche o campo de texto com o nome atual da marca
    ct_novo_nome.insert(0, marca['nome'])

    # Função para confirmar a atualização da marca
    def confirm_update():
        novo_nome = ct_novo_nome.get()
        marca_dao.update(marca_id, {'nome': novo_nome})
        update_window.destroy()
        print('Marca atualizada:', marca_id)

    # Botão para confirmar a atualização
    btn_confirm = Button(update_window, text="Confirmar", command=confirm_update)
    btn_confirm.pack()

#==================== BANCO ========================================
# Cria os rótulos para os campos de texto
L_db_Name = Label(mainWindow, text="Nome do Banco:")
L_db_Name.grid(row=0, column=0)
L_db_Host = Label(mainWindow, text="Host:")
L_db_Host.grid(row=1, column=0)
L_db_Port = Label(mainWindow, text="Porta:")
L_db_Port.grid(row=2, column=0)

# Cria os campos de texto
ct_db_Name = Entry(mainWindow)
ct_db_Name.grid(row=0, column=1)
ct_db_Host = Entry(mainWindow)
ct_db_Host.grid(row=1, column=1)
ct_db_Port = Entry(mainWindow)
ct_db_Port.grid(row=2, column=1)
#==================== BANCO ========================================

#==================== COLLECTIONS ========================================
# Cria os rótulos para os campos de texto das coleções
CollName1 = Label(mainWindow, text="Collection Extra")
CollName1.grid(row=3, column=0)
CollName2 = Label(mainWindow, text="Collection Extra")
CollName2.grid(row=4, column=0)
CollName3 = Label(mainWindow, text="Collection Extra")
CollName3.grid(row=5, column=0)

# Cria os campos de texto das coleções
ct_coll1 = Entry(mainWindow)
ct_coll1.grid(row=3, column=1)
ct_coll2 = Entry(mainWindow)
ct_coll2.grid(row=4, column=1)
ct_coll3 = Entry(mainWindow)
ct_coll3.grid(row=5, column=1)
#==================== COLLECTIONS ========================================

# Cria o botão para conectar ao banco de dados
btn_connect = Button(mainWindow, text="Criar Banco de Dados", command=create_daos)
btn_connect.grid(row=22, columnspan=4)

#==================== CRUDS ========================================
# Cria os rótulos para os campos de texto dos CRUDs
L_marca_nome = Label(mainWindow, text="Nome da Marca:")
L_marca_nome.grid(row=7, column=0)
L_modelo_nome = Label(mainWindow, text="Nome do Modelo:")
L_modelo_nome.grid(row=8, column=0)
L_modelo_marca_id = Label(mainWindow, text="ID da Marca:")
L_modelo_marca_id.grid(row=9, column=0)
L_carro_nome = Label(mainWindow, text="Nome do Carro:")
L_carro_nome.grid(row=10, column=0)
L_carro_modelo_id = Label(mainWindow, text="ID do Modelo:")
L_carro_modelo_id.grid(row=11, column=0)

# Cria os campos de texto dos CRUDs
ct_marca_nome = Entry(mainWindow)
ct_marca_nome.grid(row=7, column=1)
ct_modelo_nome = Entry(mainWindow)
ct_modelo_nome.grid(row=8, column=1)
ct_modelo_marca_id = Entry(mainWindow)
ct_modelo_marca_id.grid(row=9, column=1)
ct_carro_nome = Entry(mainWindow)
ct_carro_nome.grid(row=10, column=1)
ct_carro_modelo_id = Entry(mainWindow)
ct_carro_modelo_id.grid(row=11, column=1)

# Cria os botões para adicionar registros
btn_add_marca = Button(mainWindow, text="Adicionar Marca", command=add_marca)
btn_add_marca.grid(row=12, column=0)
btn_add_modelo = Button(mainWindow, text="Adicionar Modelo", command=add_modelo)
btn_add_modelo.grid(row=12, column=1)
btn_add_carro = Button(mainWindow, text="Adicionar Carro", command=add_carro)
btn_add_carro.grid(row=12, column=2)

# Cria as listboxes para exibir os registros
lb_marcas = Listbox(mainWindow)
lb_marcas.grid(row=13, column=0, rowspan=3)
lb_modelos = Listbox(mainWindow)
lb_modelos.grid(row=13, column=1, rowspan=3)
lb_carros = Listbox(mainWindow)
lb_carros.grid(row=13, column=2, rowspan=3)

# Cria os botões para exibir os registros
btn_show_marcas = Button(mainWindow, text="Mostrar Marcas", command=show_marcas)
btn_show_marcas.grid(row=16, column=0)
btn_show_modelos = Button(mainWindow, text="Mostrar Modelos", command=show_modelos)
btn_show_modelos.grid(row=16, column=1)
btn_show_carros = Button(mainWindow, text="Mostrar Carros", command=show_carros)
btn_show_carros.grid(row=16, column=2)

# Cria os botões para excluir e atualizar marcas
btn_delete_marca = Button(mainWindow, text="Excluir Marca", command=delete_marca)
btn_delete_marca.grid(row=17, column=0)
btn_update_marca = Button(mainWindow, text="Atualizar Marca", command=update_marca)
btn_update_marca.grid(row=17, column=1)
#==================== CRUDS ========================================

# Executa a janela principal
mainWindow.mainloop()
