from src.models.store import Store
from src.models.user import User
from src.service.service_user import ServiceUser

store = Store()

print("#Primeiro Teste")
name_1 = "Fabricio"
job_1 = "Eng"

user = User(name=name_1, job=job_1)
#print(user, name)
#print(user, job)

service = ServiceUser()
resultado = service.add_user(name=name_1, job=job_1)
print("Nome:", service.store.bd[0].name)
print("Job:", service.store.bd[0].job)
print("Resultado:", resultado)

print("#Segundo Teste")
name_1 = None
job_1 = "Eng"

service = ServiceUser()
resultado = service.add_user(name=name_1, job=job_1)
print(service.store.bd)
print("Resultado:", resultado)


print("#Terceiro Teste")
service = ServiceUser()
service.add_user("Katia", "Testadora")
print(user.name, service.store.bd)