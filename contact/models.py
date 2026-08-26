from django.db import models


class Profile(models.Model):
    """Singleton model — only one row; edit via Django admin to upload photo."""
    photo = models.ImageField(upload_to='profile/', blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'My Profile Photo'
        verbose_name_plural = 'My Profile Photo'

    def __str__(self):
        return 'Profile Photo'

    @classmethod
    def get_photo_url(cls):
        obj = cls.objects.first()
        if obj and obj.photo:
            return obj.photo.url
        return None


class ContactMessage(models.Model):
    name       = models.CharField(max_length=150)
    email      = models.EmailField()
    subject    = models.CharField(max_length=250, blank=True)
    message    = models.TextField()
    is_read    = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Contact Message'
        verbose_name_plural = 'Contact Messages'

    def __str__(self):
        return f"{self.name} ({self.email}) - {self.created_at.strftime('%Y-%m-%d %H:%M')}"
