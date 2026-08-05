def clean_name(name):
    return name.strip().title()


def clean_email(email):
    return email.strip().lower()


def clean_gender(gender):
    return gender.strip().lower()


def clean_customer(customer):
    return {
        "name": clean_name(customer["name"]),
        "email": clean_email(customer["email"]),
        "gender": clean_gender(customer["gender"]),
    }
