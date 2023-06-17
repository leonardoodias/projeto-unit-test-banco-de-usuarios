from src.models.store import Store
from src.models.user import User

class ServiceUser:
    def __init__(self):
        self.store = Store()

    def check_user(self, name):
        for user in self.store.bd:
            if user.name == name:
                return user
        return None

    def add_user(self, name, job):
        if name is not None and job is not None:
            if isinstance(name, str) and isinstance(job, str):
                if self.check_user(name) is None:
                    user = User(name, job)
                    self.store.bd.append(user)
                    return "User added"
                else:
                    return "User already exists"
            else:
                return "Invalid User"
        else:
            return "Invalid User"

    def update_user(self, name, new_job):
        user = self.check_user(name)
        if user is not None:
            user.job = new_job
            return "Job was updated"
        else:
            return "User Name is not found"

    def list_name_for_job(self, job):
        names = []
        for user in self.store.bd:
            if user.job == job:
                names.append(user.name)
        return names

    def delete_user(self, name):
        user = self.check_user(name)
        if user is not None:
            self.store.bd.remove(user)
            return "User was removed"
        else:
            return "User name is not found"
