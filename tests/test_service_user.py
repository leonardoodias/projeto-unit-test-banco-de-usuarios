from src.service.service_user import ServiceUser

class TestServiceUser:
    def test_add_user_success(self):
        # Setup
        name = "Leonardo"
        job = "Engineer"
        expected_result = "User added"
        service = ServiceUser()

        # Chamada
        result = service.add_user(name=name, job=job)

        # Avaliação
        assert result == expected_result

    def test_add_invalid_user(self):
        # Setup
        name = None
        job = "Eng"
        expected_result = "Invalid User"
        service = ServiceUser()

        # Chamada
        result = service.add_user(name=name, job=job)

        # Avaliação
        assert result == expected_result

    def test_add_existing_user(self):
        # Setup
        name = "Leonardo"
        job = "Engineer"
        expected_result = "User already exists"
        service = ServiceUser()

        # Adicionando usuário
        service.add_user(name, job)

        # Chamada
        result = service.add_user(name, job)

        # Avaliação
        assert result == expected_result

    def test_update_user_success(self):
        # Setup
        name = "Leonardo"
        job = "Engineer"
        new_job = "Tech Manager"
        expected_result = "Job was updated"
        service = ServiceUser()

        # Adicionando usuário
        service.add_user(name, job)

        # Chamada
        result = service.update_user(name, new_job)

        # Avaliação
        assert result == expected_result

    def test_update_nonexistent_user(self):
        # Setup
        name = "Gabriel"
        job = "Quality Engineer"
        expected_result = "User Name is not found"
        service = ServiceUser()

        # Chamada
        result = service.update_user(name, job)

        # Avaliação
        assert result == expected_result

    def test_list_names_for_job(self):
        # Setup
        service = ServiceUser()
        service.add_user("Leonardo", "Tech Manager")
        service.add_user("Felipe", "Tech Manager")
        service.add_user("Dias", "Quality Engineer")
        expected_result_job1 = ["Leonardo", "Felipe"]
        expected_result_job2 = ["Dias"]
        expected_result_job3 = []

        # Chamada
        result_job1 = service.list_name_for_job("Tech Manager")
        result_job2 = service.list_name_for_job("Quality Engineer")
        result_job3 = service.list_name_for_job("Manager")

        # Avaliação
        assert result_job1 == expected_result_job1
        assert result_job2 == expected_result_job2
        assert result_job3 == expected_result_job3

    def test_delete_user(self):
        # Setup
        name = "John"
        job = "Developer"
        expected_result = "User was removed"
        service = ServiceUser()
        service.add_user(name, job)

        # Chamada
        result = service.delete_user(name)

        # Avaliação
        assert result == expected_result

    def test_delete_nonexistent_user(self):
        # Setup
        name = "John"
        expected_result = "User name is not found"
        service = ServiceUser()

        # Chamada
        result = service.delete_user(name)

        # Avaliação
        assert result == expected_result

    def test_check_user_existing_user(self):
        # Setup
        name = "Leonardo"
        job = "Engineer"
        service = ServiceUser()
        service.add_user(name, job)

        # Chamada
        result = service.check_user(name)

        # Avaliação
        assert result.name == name
        assert result.job == job

    def test_check_user_nonexistent_user(self):
        # Setup
        name = "Gabriel"
        service = ServiceUser()

        # Chamada
        result = service.check_user(name)

        # Avaliação
        assert result is None

    def test_list_names_for_job_nonexistent_job(self):
        # Setup
        service = ServiceUser()
        service.add_user("Leonardo", "Tech Manager")
        service.add_user("Felipe", "Tech Manager")

        # Chamada
        result = service.list_name_for_job("Manager")

        # Avaliação
        assert result == []
