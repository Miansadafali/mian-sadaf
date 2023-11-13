from .form import SubscriberForm

def subscribe_form(request):
    return {'subscriber_form': SubscriberForm()}