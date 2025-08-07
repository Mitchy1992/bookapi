
# 📚 Book API (Django + Docker + GitHub Actions)

Hello! This is my personal project — a simple RESTful API built with Django and Django REST Framework. It manages a collection of books and supports full CRUD operations. The project is containerised with Docker, uses PostgreSQL, and includes a CI/CD pipeline with GitHub Actions for building and deploying the app automatically.

[![CI/CD Pipeline](https://github.com/Mitchy1992/bookcatalog/actions/workflows/ci-cd.yaml/badge.svg)](https://github.com/Mitchy1992/bookcatalog/actions/workflows/ci-cd.yaml)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue)](https://github.com/Mitchy1992/bookcatalog/pkgs/container/book-catalog)
[![Kubernetes](https://img.shields.io/badge/Kubernetes-Ready-green)](./k8s/)

---

## 🔧 What I Used

* **Django 4.2**
* **Django REST Framework**
* **PostgreSQL**
* **Docker & Docker Hub**
* **Helm & Kubernetes**
* **GitHub Actions** for CI/CD
* **Python 3.9**

---

## 📦 Features

* Add, update, view and delete books via REST API
* PostgreSQL as the backend database
* Dockerised app with clean environment separation
* CI/CD pipeline to build, test and push Docker images
* Optional Kubernetes deployment with Helm

---

## 🚀 Getting Started

Here’s how I set up and ran this project locally and in CI/CD.

### 1. Clone the repo

```bash
git clone https://github.com/Mitchy1992/bookapi.git
cd bookapi
```

---

### 2. Run it locally using Docker

Make sure Docker is installed and running on your machine.

```bash
docker build -t mitch3192/bookapi:latest .
docker run -p 8000:8000 mitch3192/bookapi:latest
```

You can now access the API at: `http://localhost:8000/`

---

### 3. Environment variables

I used the `python-decouple` library to manage secrets. These are the environment variables required:

```
DEBUG=True
SECRET_KEY=your_django_secret
ALLOWED_HOSTS=*
DATABASE_URL=postgres://user:password@localhost:5432/dbname
```

You can either:

* Use a `.env` file (in local development)
* Or use Kubernetes Secrets and ConfigMaps in production

---

## ⚙️ Running Tests

I added a few simple tests. To run them:

```bash
python manage.py test
```

In CI/CD, the tests use PostgreSQL, so make sure the database is running or mocked during tests.

---

## 🐳 CI/CD Pipeline

I set up a GitHub Actions workflow that does the following:

* Installs dependencies
* Runs Django tests
* Builds a Docker image
* Pushes it to Docker Hub
* Optionally deploys to Kubernetes

Here's the GitHub Actions file: `.github/workflows/deploy.yaml`

You’ll need to set these secrets in your GitHub repo:

* `DOCKERHUB_USERNAME`
* `DOCKERHUB_TOKEN`
* (optional) `KUBECONFIG` (if deploying to K8s)

---

## 🛠 Kubernetes Deployment

I created a Helm chart (`bookapi-chart/`) that contains:

* Deployment
* Service
* Ingress
* ConfigMap/Secrets
* Horizontal Pod Autoscaler

To install it:

```bash
helm upgrade --install bookapi ./bookapi-chart --namespace default
```

---

## 📁 File Structure

```bash
bookapi/
│
├── bookapi/                  # Django app
├── bookapi-chart/            # Helm chart for K8s deployment
├── Dockerfile                # Docker image config
├── requirements.txt          # Python dependencies
├── .github/workflows/        # GitHub Actions config
└── README.md                 # You're reading it!

```

---
Absolutely — here’s an updated **section to include in your `README.md`** that shows how to use the Book API via **Postman** and **cURL**. This goes directly after the “📁 File Structure” section.

---

## 📡 How to Use the API

Once the server is running (locally or via Kubernetes), the API base URL is:

```
API HOME PAGE : http://localhost:8000/
API           : http://localhost:8000/api
BOOKS         : http://localhost:8000/api/books
```

You can interact with the API using either **Postman** or **cURL**.

---

### 🔸 1. Get All Books

**cURL:**

```bash
curl -X GET http://localhost:8000/api/books/
```

**Postman:**

* Method: `GET`
* URL: `http://localhost:8000/api/books/`
* No body needed

---

### 🔸 2. Get a Single Book (by ID)

**cURL:**

```bash
curl -X GET http://localhost:8000/api/books/1/
```

**Postman:**

* Method: `GET`
* URL: `http://localhost:8000/api/books/1/`

---

### 🔸 3. Create a New Book

**cURL:**

```bash
curl -X POST http://localhost:8000/api/books/ \
     -H "Content-Type: application/json" \
     -d '{"title": "1984", "author": "George Orwell", "isbn": "9780451524935"}'
```

**Postman:**

* Method: `POST`
* URL: `http://localhost:8000/api/books/`
* Body: raw JSON

```json
{
  "title": "1984",
  "author": "George Orwell",
  "isbn": "9780451524935"
}
```

---

### 🔸 4. Update a Book

**cURL:**

```bash
curl -X PUT http://localhost:8000/api/books/1/ \
     -H "Content-Type: application/json" \
     -d '{"title": "Animal Farm", "author": "George Orwell", "isbn": "9780451526342"}'
```

**Postman:**

* Method: `PUT`
* URL: `http://localhost:8000/api/books/1/`
* Body: raw JSON (same as above)

---

### 🔸 5. Delete a Book

**cURL:**

```bash
curl -X DELETE http://localhost:8000/api/books/1/
```

**Postman:**

* Method: `DELETE`
* URL: `http://localhost:8000/api/books/1/`

---

## 🌍 Future Improvements

* Add Swagger/OpenAPI documentation
* Set up integration tests with mocked DB
* Deploy using GitHub Container Registry
* Auto-scale based on CPU/memory in Kubernetes

---

## 🙋‍♂️ Author

Built with care by **Mitul Galav**

📧 Feel free to reach out: [mitulgalav@hotmail.com](mailto:mitulgalav@hotmail.com)

🐙 GitHub: [@Mitchy1992](https://github.com/Mitchy1992)
