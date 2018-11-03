import random
import string

from django.utils.text import slugify


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_customer_id_generator(instance):

    customer_new_id = random_string_generator()

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(customer_id=customer_new_id).exists()
    if qs_exists:
        return unique_slug_generator(instance)
    return customer_new_id


def unique_order_id_generator(instance):
    """
    This is for a Django project with an order_id field
    """
    order_new_id = random_string_generator()

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(order_id=order_new_id).exists()
    if qs_exists:
        return unique_slug_generator(instance)
    return order_new_id


def unique_slug_generator(instance, filed="plan",new_slug=None):
    """
    This is for a Django project and it assumes your instance 
    has a model with a slug field and a title character (char) field.
    """
    if new_slug is not None:
        slug = new_slug
    else:
        # slug = slugify(instance.plan)
        slug = slugify(getattr(instance, filed))

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists() # this is why Product has slug filed!!
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
                    slug=slug,
                    randstr=random_string_generator(size=4)
                )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug