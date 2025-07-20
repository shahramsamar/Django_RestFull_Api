# Django Restful API

A Django project implementing RESTful APIs using Django REST Framework (DRF). This repository provides a foundation for building scalable and robust APIs for any Django application.

## Features

- **RESTful API Endpoints**: Create, retrieve, update, and delete operations.
- **ModelViewSet** for simplifying CRUD operations.
- **Serializers** for data validation and transformation.
- **Browsable API** for easy testing and interaction.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/shahramsamar/Django_RestFull_Api.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Django_RestFull_Api
   ```

3. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Apply database migrations:
   ```bash
   python manage.py migrate
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Usage

1. Access the application at `http://127.0.0.1:8000/`.

2. Use the provided API endpoints to interact with the application. Examples:
   - `GET /api/items/`: Retrieve a list of items.
   - `POST /api/items/`: Create a new item.
   - `PUT /api/items/<id>/`: Update an existing item.
   - `DELETE /api/items/<id>/`: Delete an item.

## Example Code

### Example Model
```python
from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
```

### Example Serializer
```python
from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
```

### Example ViewSet
```python
from rest_framework import viewsets
from .models import Item
from .serializers import ItemSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
```

### Example URL Configuration
```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet

router = DefaultRouter()
router.register(r'items', ItemViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
```

## Requirements

- Python 3.7+
- Django 3.2+
- Django REST Framework 3.12+

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes with clear messages.
4. Push your branch and create a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

- **Author**: Shahramsamar
- **Email**: [shahramsamar2010@gmail.com](mailto:shahramsamar.dev@gmail.com)
- **GitHub**: [Shahramsamar](https://github.com/shahramsamar)

 ![Alt](https://repobeats.axiom.co/api/embed/eabe6508a91fa38b4ace0060919094363916f544.svg "Repobeats analytics image")

