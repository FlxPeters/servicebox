from django.contrib.auth.models import User

if not User.objects.filter(username="admin"):
    u = User.objects.create_superuser("admin", "admin@example.com", "admin")
