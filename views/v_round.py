from datetime import datetime


def get_round_number():
    number = input("Veuillez saisir le numéro du round :")
    return number


def get_round_date():
    date = datetime.today()
    return date.strftime("%d/%m/%y")


def get_round_start():
    start_time = datetime.now()
    return start_time.strftime("%H:%M:%S")


def get_round_end():
    end_time = datetime.now()
    return end_time.strftime("%H:%M:%S")
