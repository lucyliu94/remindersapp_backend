"""ReminderTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from app.Reminder import Reminder

class ReminderTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        Reminder.create({"title": "Supplements", "details": "Vitamin A, B, C, D, E"})
        Reminder.create({"title": "Feed the cat", "details": "1/3 cup of dry food"})
        Reminder.create({"title": "Send back amazon return packes", "details": "print label and return them all"})
        Reminder.create({"title": "Pay Rent", "details": "Vitamin A, B, C, D, E"})
        Reminder.create({"title": "Supplements", "details": "Vitamin A, B, C, D, E"})
        Reminder.create({"title": "Supplements", "details": "Vitamin A, B, C, D, E"})
        pass
