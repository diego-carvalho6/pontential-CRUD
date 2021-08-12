from developers.models import Developer
from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework import status

# Create your tests here.


class DeveloperViewsTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        
        cls.nome = "diego"
        cls.sexo = "M"
        cls.idade = 22
        cls.hobby = "estudar"
        cls.datanascimento = "1999-09-06"
        
        cls.developer = Developer.objects.create(
            nome=cls.nome,
            sexo=cls.sexo,
            idade=cls.idade,
            hobby=cls.hobby,
            datanascimento=cls.datanascimento
        )

    def test_developers_get_can_execute(self):
        client = APIClient()
        
        response = client.get(
           '/developers', format="json"
        )
        response_result = response.json()
        
        self.assertEquals(type([]), type(response_result))
        self.assertEquals(response.status_code, status.HTTP_200_OK)
    
    def test_route_can_get_delopers_with_id(self):
        client = APIClient()
        
        response = client.get(
           '/developers/1', format="json"
        )
        response_result = response.json()
        
        self.assertEquals("diego", response_result["nome"])
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        
        response2 = client.get(
           '/developers/10', format="json"
        )
        
        response_result = response2.json()
        
        self.assertEquals("Not found.", response_result["detail"])
        self.assertEquals(response2.status_code, status.HTTP_404_NOT_FOUND)
    
    def test_route_can_get_developer_with_query(self):
        
        client = APIClient()
        
        response = client.get(
           '/developers?limit=10&search=diego', format="json"
        )
        response_result = response.json()
        
        self.assertEquals(1, len(response_result.get("results")))
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        

    def test_route_post_can_register_a_developer(self):
        client = APIClient()
        body = {"nome": "diego", "sexo": "M", "idade": 22, "hobby": "estudar", "datanascimento": "06/09/1999"}

        response = client.post(
           '/developers', body, format="json"
        )
        response_result = response.json()

        body["id"] = 2
        
        self.assertEquals(body, response_result)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        
        body_wrong = {"name: diego"}
        
        response2 = client.post(
           '/developers', body_wrong, format="json"
        )
        response_result = response.json()
        
        self.assertEquals(response2.status_code, status.HTTP_400_BAD_REQUEST)
        
    def test_route_put_can_update_developer(self):
        
        client = APIClient()
        body = {"nome": "junior", "sexo": "M", "idade": 22, "hobby": "estudar", "datanascimento": "06/09/1999"}

        response = client.put(
           '/developers/1', body, format="json"
        )
        response_result = response.json()
        
        self.assertEquals("junior", response_result["nome"])
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        

        body = {"name": "junior"}

        response = client.put(
           '/developers/1', body, format="json"
        )
        response_result = response.json()
        
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        
    def test_route_can_delete_a_developer(self):
        client = APIClient()

        response = client.delete(
           '/developers/1', format="json"
        )

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
        

        response2 = client.get(
           '/developers/1', format="json"
        )

        self.assertEquals(response2.status_code, status.HTTP_404_NOT_FOUND)
        
