import usuario


def app ():

    menu()



def menu():
    
    eleccion = 0

    while eleccion != 9:
        print('\n')
        print('Bienvenido a la agenda de contactos: \n')
        print('Pulsa el numero de la accion que quieras realizar. \n')
        print('1. Si deseas crear un contacto. ')
        print('2. Si deseas listar todos los contactos. ')
        print('3. Si deseas buscar un contacto ')
        print('4. Si deseas editar un contacto. ')
        print('5. Si deseas borrar un contacto. ')
        print('9. para salir.')

        pregunta = int(input())


        if pregunta == 9:
            eleccion = 9
        elif pregunta == 1:
            crear_usuario()
            continue
        elif pregunta == 2:
            list_all()
            continue
        elif pregunta == 3:
            list_one()
            continue
        elif pregunta == 4:
            update_user()
            continue
        elif pregunta == 5:
            delete_user()
            continue


def crear_usuario():

    print('Agrega un nuevo usuario: \n')
    input_id = int(input('Ingresa el numero de identificacion: '))
    input_name = input('Ingresa el nombre del contacto: ')
    input_lastname = input('Ingresa el apellido del contacto: ')
    input_phone = input('Ingresa el telefono del contacto: ')

    user = usuario.User(input_id, input_name , input_lastname , input_phone)
    user.create_user()

    print('Contacto agregado. ')

def list_all():
    user= usuario.User()
    lista_usuarios = user.list_all()

    if len(lista_usuarios) == 0:
        print('Aun no has registrado ningun usuario. ')
    else:
        print('Usuarios registrados: ')
        
        for lista_usuario in lista_usuarios:
            print(f'Id: {lista_usuario[0]}. Nombre: {lista_usuario[1]}. Apellido: {lista_usuario[2]}. Telefono: {lista_usuario[3]}')
            
def list_one():
    user= usuario.User()

    print('Buscar usuario. \n')

    id_usuario = int(input('Ingresa el id del usuario a buscar: \n'))

    lista_usuarios = user.list_one(id_usuario) 
    if len(lista_usuarios) == 0:
        print('\n No hay un usuario con ese id, intenta nuevamente. ')
    else:
        print('\n Usuario registrado: ')
        
        for lista_usuario in lista_usuarios:
            print(f'Id: {lista_usuario[0]}. Nombre: {lista_usuario[1]}. Apellido: {lista_usuario[2]}. Telefono: {lista_usuario[3]}')

def update_user():
    search_user = usuario.User()

    print('Actualizar usuario \n')
    id_new = int(input('Ingresa el id de la persona que deseas editar: '))

    user_return = search_user.list_one(id_new)

    if len(user_return) > 0:

        nombre = input('Ingresa el nuevo nombre: ')
        apellido = input('Ingresa el nuevo apellido: ')
        tel = input('Ingresa el nuevo telefono: ')

        upd_user = usuario.User(id_new, nombre, apellido, tel)

        upd_user.update_user(id_new)
        print('Usuario actualizado')

    else:
        print('No hay usuarios con ese id')

def delete_user():
    user = usuario.User()

    print('Eliminar usuario \n')
    id_eliminado = int(input('Ingresa el id de la persona a eliminar: '))

    delete_user = user.del_user(id_eliminado)

    if delete_user == 200:
        print(f'El usuario con id {id_eliminado} fue eliminado')
    else:
        print('Ocurrio un error!!')

app()

