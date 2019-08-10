from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
import uuid
from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify


class BaseProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                primary_key=True)
    slug = models.UUIDField(default=uuid.uuid4, blank=True, editable=False)
    # Add more user profile fields here. Make sure they are nullable
    # or with default values
    picture = models.ImageField('Profile picture',
                                upload_to='profile_pics/%Y-%m-%d/',
                                null=True,
                                blank=True)
    bio = models.CharField("Short Bio", max_length=200, blank=True, null=True)
    email_verified = models.BooleanField("Email verified", default=False)

    class Meta:
        abstract = True


class Tango_Location(models.Model):
    name = models.CharField(max_length=128)
    group_url = models.URLField(null=True)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Tango_Location, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Tango_Events(models.Model):
    category = models.ForeignKey(Tango_Location)
    message = models.CharField(max_length=928, blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    updated_time = models.DateTimeField()
    post_type = models.CharField(max_length=128, blank=True, null=True)
    post_name = models.CharField(max_length=998, blank=True, null=True)
    permalink_url = models.URLField(blank=True)
    picture = models.URLField(blank=True, null=True)
    post_id = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=9998, blank=True, null=True)
    post_from = models.CharField(max_length=998, blank=True)
    created_time = models.DateTimeField()
    place = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self, ):
        return self.category
    # class Meta:
        # ordering = ['-created_time']


class TangoCommunity(models.Model):
    name = models.CharField(max_length=128, unique=True)
#   url = models.URLField(blank=True)
#   slug = models.SlugField()

#    def save(self,*args, **kwargs):
#        self.slug = slugify(self.name)
#        super(TangoCommunity,self).save(*args, **kwargs)

    def __str__(self):
        return str(self.name)


class TangoCommunityInfo(models.Model):
    category = models.ForeignKey(TangoCommunity)
    message = models.CharField(max_length=928, blank=True, null=True)
    description = models.CharField(max_length=4928, blank=True, null=True)
    class_location = models.CharField(max_length=928, blank=True, null=True)
    class_timings = models.CharField(max_length=928, blank=True, null=True)
    class_location1 = models.CharField(max_length=928, blank=True, null=True)
    class_timings1 = models.CharField(max_length=928, blank=True, null=True)
    class_location2 = models.CharField(max_length=928, blank=True, null=True)
    class_timings2 = models.CharField(max_length=928, blank=True, null=True)
    class_location3 = models.CharField(max_length=928, blank=True, null=True)
    class_timings3 = models.CharField(max_length=928, blank=True, null=True)
    class_location_map = models.URLField(blank=True)
    class_location_map1 = models.URLField(blank=True)
    instructor_name = models.CharField(max_length=928, blank=True, null=True)
    fees = models.CharField(max_length=928, blank=True, null=True)
    admission_process = models.CharField(
        max_length=5928, blank=True, null=True)
    email = models.CharField(max_length=928, blank=True, null=True)
    email1 = models.EmailField(blank=True, null=True)
    contact_number = models.CharField(max_length=928, blank=True, null=True)
    fb_url = models.URLField(blank=True)
    fb_url1 = models.URLField(blank=True)
    website = models.URLField(blank=True, null=True)
    website1 = models.URLField(blank=True, null=True)
    milonga_venue = models.CharField(max_length=4928, blank=True, null=True)
    milonga_venue_map_link = models.URLField(blank=True)
    milonga_time = models.CharField(max_length=928, blank=True, null=True)
    practica_venue = models.CharField(max_length=4928, blank=True, null=True)
    practica_venue_map_link = models.URLField(blank=True)
    practica_time = models.CharField(max_length=928, blank=True, null=True)

    def __str__(self, ):
        return str(self.category)
    # class Meta:
        # ordering = ['-created_time']


class FBLocation(models.Model):
    Name = models.CharField(max_length=100)
    Group_Url = models.URLField(null=True)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.Name)
        super(FBLocation, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.Name)


class FBEvents(models.Model):
    Location = models.ForeignKey(FBLocation)
    Location_Name = models.CharField(max_length=500, null=True, blank=True)
    Attending_Count = models.IntegerField(default=0)
    Cover = models.URLField(blank=True, null=True)
    Event_Name = models.CharField(max_length=928, blank=True, null=True)
    Event_Link = models.URLField(blank=True, null=True)
    Start_Time = models.DateTimeField()
    Event_Id = models.CharField(max_length=200)
    Description = models.CharField(max_length=99998, blank=True, null=True)
    End_Time = models.DateTimeField()
    Place = models.CharField(max_length=9999, blank=True, null=True)
    Updated_Time = models.DateTimeField()

    def __str__(self, ):
        return str(self.Location)

    class Meta:
        ordering = ['-Start_Time']


@python_2_unicode_compatible
class Profile(BaseProfile):
    def __str__(self):
        return "{}'s profile". format(self.user)
