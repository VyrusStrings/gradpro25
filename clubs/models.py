from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
class Club(models.Model):
    id = models.AutoField(primary_key=True)  # Add ID as primary key
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='club_images/', blank=True, null=True)
    quota = models.PositiveIntegerField(default=0)  # Add quota field
    leader = models.OneToOneField(
        "users.ClubLeader",
        on_delete=models.SET_NULL,
        null=True,  # Allow null in the database
        blank=True,  # Allow blank in forms
        related_name='led_club'
    )  # Optional relationship with ClubLeader
    members = models.ManyToManyField('users.ClubMember', blank=True, related_name='club_memberships')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ClubActivity(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    club = models.ForeignKey('clubs.Club', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    datetime = models.DateTimeField()
    participants = models.TextField()
    image = models.ImageField(upload_to='activity_images/', blank=True, null=True)
    needs = models.TextField(blank=True, null=True)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    transportation_request = models.BooleanField(default=False)
    supporting_documents = models.FileField(upload_to='activity_docs/', blank=True, null=True)
    created_by = models.ForeignKey('users.User', on_delete=models.CASCADE, null=True, blank=True)  # Updated for AUTH_USER_MODEL
    approval_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')  # ✅ Ensure this exists

    def __str__(self):
        return self.title




class Meeting(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='meetings')
    date_time = models.DateTimeField()
    agenda = models.TextField()

    def __str__(self):
        return f"Meeting with {self.club.name} on {self.date_time}"


class Announcement(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]

    club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='announcements')
    title = models.CharField(max_length=255)
    content = models.TextField()
    visible = models.BooleanField(default=True)  # Visibility toggle (default: visible to members)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({'Visible' if self.visible else 'Hidden'}, {self.status})"


class ClubDocument(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name="documents")
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to="club_documents/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.club.name})"