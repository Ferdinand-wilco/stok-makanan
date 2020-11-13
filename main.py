from datetime import datetime

#punyasendiri
from models import ticket, user
import view
import system

system.tickets = system.load_ticket_data()
system.users = system.load_users_data()

while not system.error :
	view.main_menu()