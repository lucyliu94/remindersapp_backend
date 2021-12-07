""" A ReminderController Module """

from masonite.controllers import Controller
from app.Reminder import Reminder
from masonite.request import Request


class ReminderController(Controller):
    """Class Docstring Description
    """
    def __init__(self, request: Request):
        self.request = request

    def show(self):
        """Show a single resource listing
        ex. Model.find('id')
            Get().route("/show", ReminderController)
        """
        id = self.request.param("id")
        return Reminder.find(id)
        pass

    def index(self):
        """Show several resource listings
        ex. Model.all()
            Get().route("/index", ReminderController)
        """
        return Reminder.all()

    pass

    def create(self):
        """Show form to create new resource listings
         ex. Get().route("/create", ReminderController)
        """
        title = self.request.input("title")
        details = self.request.input("details")
        reminder = Reminder.create({"title": title, "details": details})
        return reminder
        pass


    def update(self):
        """Edit an existing resource listing
        ex. Post target to update new Model
            Post().route("/update", ReminderController)
        """
        title = self.request.input("title")
        details = self.request.input("details")
        id = self.request.param("id")
        Reminder.where("id", id).update({"title": title, "details": details})
        return Reminder.where("id",id).get()
        pass

    def destroy(self):
        """Delete an existing resource listing
        ex. Delete().route("/destroy", ReminderController)
        """
        id = self.request.param("id")
        reminder = Reminder.where("id", id).get()
        Reminder.where("id", id).delete()
        return reminder 

        pass