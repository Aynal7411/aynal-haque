import requests

from django.conf import settings

from .utils import get_client_ip


def create_client_contact(form, request):
    """
    Save contact and send it to n8n.
    """

    contact = form.save(commit=False)

    contact.ip_address = get_client_ip(request)

    contact.save()

    payload = {
        "id": str(contact.id),
        "title": contact.title,
        "name": contact.name,
        "email": contact.email,
        "phone": contact.phone,
        "message": contact.message,
        "urgent": contact.urgent,
        "status": contact.status,
        "source": contact.source,
        "sent_at": contact.sent_at.isoformat(),
    }

    try:

        requests.post(
            settings.https://milonthis.app.n8n.cloud/webhook/contact-form,
            json=payload,
            timeout=10,
        )

    except requests.RequestException:

        pass

    return contact