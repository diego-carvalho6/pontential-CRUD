# Potential Crud

Potential Crud is a system developed with the objective to save the data of the developers

When using this API, it should be possible to create a developer and manage your data.

# How to install and run

to start the app, first you need to make some steps

1- clone the repo below:

> https://gitlab.com/zacarias_link/pontential-crud

2- enter the virtual environment with the commands:

```
# Enter in the folder
$ cd pontential-crud/

# Make a container
$ docker build -t python3 .

# Start the server
$ docker-compose up -d

the server will run in http://127.0.0.1:8000/
```

3- make the migrations for your database and table be created

> `$ docker-compose exec web python manage.py migrate`

# HTTP status

200 -> This request was successful.

201 -> Request was successful and that a new resource was created.

204 -> Request was successful and that resource was deleted.

400 -> Server is unable to process the request due to a user error, either by syntax or any other reason

404 -> The server cannot find the requested resource.

# Developer

table to the Developer

## Schemas

### User

|      key       | type |        description        |
| :------------: | :--: | :-----------------------: |
|       id       | int  |    id of the Developer    |
|     idade      | int  |   age of the Developer    |
|      nome      | str  |   name of the Developer   |
|     hobby      | str  |    the Developer hobby    |
| datanascimento | str  | birthday of the developer |
|      sexo      | str  |  gender of the developer  |

## `Endpoints and methods:`

## Register new Developer

-> URL and method:

> POST: `http://127.0.0.1:8000/developers`

**Body request example:**

Request example: `POST http://127.0.0.1:8000/developers`

```JSON
    {
     	    "nome": "diego",
			"idade": 22,
			"hobby": "estudar",
			"datanascimento": "06/09/1999",
			"sexo": "M"
     }
```

**Response example:**

Response: `status 201 - Created`

```JSON
{
  "id": 1,
  "nome": "diego",
  "idade": 22,
  "hobby": "estudar",
  "sexo": "M",
  "datanascimento": "06/09/1999"
}
```

## Get Developers

-> URL and method:

> GET: `http://127.0.0.1:8000/developers`

**Body request example:**

Request with no body example: `GET http://127.0.0.1:8000/developers`

**Response example:**

Response: `status 200 - OK`

```JSON
[
  {
    "id": 1,
    "nome": "diego",
    "idade": 22,
    "hobby": "estudar",
    "sexo": "M",
    "datanascimento": "06/09/1999"
  },
  {
    "id": 2,
    "nome": "junior",
    "idade": 24,
    "hobby": "musica",
    "sexo": "M",
    "datanascimento": "02/03/1975"
  }
]
```

Request to get **ONE** developer example: `GET http://127.0.0.1:8000/developers/2`

**Response example:**

Response: `status 200 - OK`

```JSON
  {
    "id": 2,
    "nome": "junior",
    "idade": 24,
    "hobby": "musica",
    "sexo": "M",
    "datanascimento": "02/03/1975"
  }
```

Request with paginate example: `GET http://127.0.0.1:8000/developers?limit=1&offset=1`

**Query params:**

```JSON
{
    "limit": "Required",
    "offset": "No required"
}
```

**Response example:**

Response: `status 200 - OK`

```JSON
{
  "count": 2,
  "next": "http://127.0.0.1:8000/developers?limit=1&offset=1",
  "previous": null,
  "results": [
    {
      "id": 1,
      "nome": "diego",
      "idade": 22,
      "hobby": "estudar",
      "sexo": "M",
      "datanascimento": "06/09/1999"
    }
  ]
}
```

Request with paginate and filter example: `GET http://127.0.0.1:8000/developers?limit=1&search=diego`

**Query params:**

```JSON
{
    "limit": "Required",
    "offset": "No required",
    "search": "required"
}
```

**Response example:**

Response: `status 200 - OK`

```JSON
{
  "count": 1,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "nome": "diego",
      "idade": 22,
      "hobby": "estudar",
      "sexo": "M",
      "datanascimento": "06/09/1999"
    }
  ]
}
```

## Update Developers

-> URL and method:

> PUT: `http://127.0.0.1:8000/developers/<int:developer_id>`

**Body request example:**

Request example: `GET http://127.0.0.1:8000/developers/1`

```JSON
      {
     	"nome": "junior",
		"idade": 25,
		"hobby": "musica",
		"datanascimento": "02/03/1975",
		"sexo": "M"
     }
```

**Response example:**

Response: `status 200 - OK`

```JSON
{
  "id": 2,
  "nome": "junior",
  "idade": 25,
  "hobby": "musica",
  "sexo": "M",
  "datanascimento": "02/03/1975"
}
```

## Delete Developers

-> URL and method:

> PUT: `http://127.0.0.1:8000/developers/<int:developer_id>`

**Body request example:**

Request with no body example: `GET http://127.0.0.1:8000/developers/1`

**Response example:**

Response: `status 204 - No Content`
