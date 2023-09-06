import factory
from whitepapers.models import WhitePapers, Topic
from users.models import UserDownload, Country
from django.utils import timezone
from django.template.defaultfilters import slugify

class TopicF(factory.django.DjangoModelFactory):
    class Meta:
        model = Topic
    title = factory.Faker('word')
    description = factory.Faker('sentence', nb_words=10)

class WhitePapersF(factory.django.DjangoModelFactory):
    class Meta:
        model = WhitePapers
        
    title = factory.Faker('sentence', nb_words=4)
    description = factory.Faker('sentence', nb_words=50)
    about = factory.Faker('sentence', nb_words=120)
    detail = factory.Faker('sentence', nb_words=100)
    status = factory.Faker('random_element', elements=[
                           'Draft', 'Published', 'Archives'])
    created_at = factory.Faker('date_time', tzinfo=timezone.utc)
    updated_at = factory.Faker('date_time', tzinfo=timezone.utc)
    count_of_downloads = factory.Faker('random_int', min=0, max=1000)
    topic = factory.SubFactory(TopicF)
    author = factory.Faker('name')
    image = factory.django.ImageField()
    file = factory.django.FileField()
    
            
    @factory.post_generation
    def create_slug(instance, *args, **kwargs):
        instance.slug = slugify(instance.title)  
        instance.save()
    
    
class CountryF(factory.django.DjangoModelFactory):
    class Meta:
        model = Country
    name = factory.Faker('country')
    code = factory.Faker('country_code')

class UsersF(factory.django.DjangoModelFactory):
    class Meta:
        model = UserDownload
    name = factory.Faker('name')
    company = factory.Faker('company')
    position = factory.Faker('job')
    email = factory.Faker('email')
    phone = factory.Faker('phone_number')
    country = factory.SubFactory(CountryF)