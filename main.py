from nicegui import ui

# in-memory list to store contacts
contacts = []


def refresh_contacts() -> None:
    """Refresh the list of displayed contacts."""
    contact_list.clear()
    with contact_list:
        for contact in contacts:
            with ui.row().classes('items-center gap-4'):
                ui.label(f"{contact['name']} | {contact['email']} | {contact['phone']}")
                ui.button('Delete', on_click=lambda c=contact: delete_contact(c))


def add_contact() -> None:
    """Add a contact from the input fields."""
    if name.value and email.value and phone.value:
        contacts.append({'name': name.value, 'email': email.value, 'phone': phone.value})
        name.value = ''
        email.value = ''
        phone.value = ''
        refresh_contacts()


def delete_contact(contact: dict) -> None:
    """Delete the given contact and refresh display."""
    contacts.remove(contact)
    refresh_contacts()



with ui.row().classes('gap-4'):
    name = ui.input('Name')
    email = ui.input('Email')
    phone = ui.input('Phone')
    ui.button('Add', on_click=add_contact)

contact_list = ui.column()

ui.run()
