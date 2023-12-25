
''''
• Create a phonebook module holding contact details like (simple class with just a constructor):
• id - UUID,
• first name – at least 2 characters, last name – at least 1 character,
• phone number (in xx-xxxxxxx or xxx-xxxxxxx format)
• city – 1 of a closed list of 10 cities you choose
• Expose few functions (use generators when appropriate):
• add(**args) -> uuid (returns the new generated contact id)
• find_by_lastname(ln) -> contact or None
• find_id(uuid) -> contact or None
• remove(uuid) -> contact or None (Removes this contact and moves it to the deleted phonebook)
• restore(uuid) -> bool (locate from deleted phonebook and adds back to phonebook)
• add_phone(uuid) -> bool (adds another phone to this contact)
• group_by(arg) -> Dictionary (arg can be city or lastname. Returns how many there are for each city/lastname)

'''

import uuid

class Contact:
    def __init__(self, first_name, last_name, phone_number, city):
        self.id = uuid.uuid4()
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.city = city

class Phonebook:
    def __init__(self):
        self.contacts = {}
        self.deleted_contacts = {}

    def add(self, **kwargs):
        if 'first_name' in kwargs and 'last_name' in kwargs and 'phone_number' in kwargs and 'city' in kwargs:
            if len(kwargs['first_name']) >= 2 and len(kwargs['last_name']) >= 1:
                contact = Contact(kwargs['first_name'], kwargs['last_name'], kwargs['phone_number'], kwargs['city'])
                self.contacts[contact.id] = contact
                return contact.id
            else:
                raise ValueError("First name should be at least 2 characters and last name should be at least 1 character.")
        else:
            raise ValueError("Please provide all required contact details.")

    def find_by_lastname(self, ln):
        for contact in self.contacts.values():
            if contact.last_name == ln:
                return contact
        return None

    def find_id(self, uuid):
        return self.contacts.get(uuid, None)

    def remove(self, uuid):
        contact = self.contacts.pop(uuid, None)
        if contact:
            self.deleted_contacts[contact.id] = contact
        return contact

    def restore(self, uuid):
        contact = self.deleted_contacts.pop(uuid, None)
        if contact:
            self.contacts[contact.id] = contact
            return True
        return False

    def add_phone(self, uuid, new_phone_number):
        contact = self.contacts.get(uuid, None)
        if contact:
            contact.phone_number = new_phone_number
            return True
        return False

    def group_by(self, arg):
        result = {}
        if arg == 'city':
            for contact in self.contacts.values():
                result[contact.city] = result.get(contact.city, 0) + 1
        elif arg == 'lastname':
            for contact in self.contacts.values():
                result[contact.last_name] = result.get(contact.last_name, 0) + 1
        return result
