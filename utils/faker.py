from faker import Faker

fake = Faker()

def get_login_faker(num_casos=5):
    casos = []
    usuarios_validos = ["standard_user"]
    passwords_validos = ["secret_sauce"]

    for _ in range(num_casos):

        if fake.boolean(chance_of_getting_true=30):
            # Datos válidos
            username = fake.random.choice(usuarios_validos)
            password = fake.random.choice(passwords_validos)
            expected_result = True

        else:
            # Datos inválidos
            username = fake.user_name()
            password = fake.password(length=10)
            expected_result = False

        casos.append((username, password, expected_result))

    return casos
