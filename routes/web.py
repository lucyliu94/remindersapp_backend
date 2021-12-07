"""Web Routes."""

from masonite.routes import Get, Post, Put, Delete, RouteGroup

ROUTES = [
    Get("/", "WelcomeController@show").name("welcome"),
    
    RouteGroup([
    Get("/", "ReminderController@index").name("index"),
    Get("/@id", "ReminderController@show").name("show"),
    Post("/", "ReminderController@create").name("create"),
    Put("/@id", "ReminderController@update").name("update"),
    Delete("/@id", "ReminderController@destroy").name("destroy")
        
    ], prefix="/reminders", name="reminders")
    
]
