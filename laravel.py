import sublime, sublime_plugin
import logging
import os

class GenerateControllerCommand(sublime_plugin.WindowCommand):
    def run(self):
        self.window.show_input_panel("Controller Name", "", self.on_done, None, None)

    def on_done(self, name):
        folder = self.window.folders()
        opened_folder = folder[0]
        command_string = "php " + opened_folder + "/artisan make:controller " + name
        os.system(command_string)

        self.window.open_file(opened_folder + "/app/Http/Controllers/" + name + ".php")

    def is_enabled(self):
        folder = self.window.folders()
        opened_folder = folder[0]
        return os.path.isfile(opened_folder + "/artisan")

class GenerateModelCommand(sublime_plugin.WindowCommand):
    def run(self):
        self.window.show_input_panel("Model Name", "", self.on_done, None, None)
        
    def on_done(self, name):
        folder = self.window.folders()
        opened_folder = folder[0]
        command_string = "php " + opened_folder + "/artisan make:model " + name
        os.system(command_string)

        self.window.open_file(opened_folder + "/app/" + name + ".php")

    def is_enabled(self):
        folder = self.window.folders()
        opened_folder = folder[0]
        return os.path.isfile(opened_folder + "/artisan")

class GenerateMigrationCommand(sublime_plugin.WindowCommand):
    def run(self):
        self.window.show_input_panel("Migration Name", "", self.on_done, None, None)
        
    def on_done(self, name):
        folder = self.window.folders()
        opened_folder = folder[0]
        command_string = "php " + opened_folder + "/artisan make:migration " + name
        os.system(command_string)

    def is_enabled(self):
        folder = self.window.folders()
        opened_folder = folder[0]
        return os.path.isfile(opened_folder + "/artisan")

class MigrateCommand(sublime_plugin.WindowCommand):
    def run(self):
        folder = self.window.folders()
        opened_folder = folder[0]
        command_string = "php " + opened_folder + "/artisan migrate"
        os.system(command_string)

    def is_enabled(self):
        folder = self.window.folders()
        opened_folder = folder[0]
        return os.path.isfile(opened_folder + "/artisan")

class MigrateRollbackCommand(sublime_plugin.WindowCommand):
    def run(self):
        folder = self.window.folders()
        opened_folder = folder[0]
        command_string = "php " + opened_folder + "/artisan migrate:rollback"
        os.system(command_string)

    def is_enabled(self):
        folder = self.window.folders()
        opened_folder = folder[0]
        return os.path.isfile(opened_folder + "/artisan")

class GenerateSeederCommand(sublime_plugin.WindowCommand):
    def run(self):
        self.window.show_input_panel("Seeder Name", "", self.on_done, None, None)
        
    def on_done(self, name):
        folder = self.window.folders()
        opened_folder = folder[0]
        command_string = "php " + opened_folder + "/artisan make:seeder " + name
        os.system(command_string)

    def is_enabled(self):
        folder = self.window.folders()
        opened_folder = folder[0]
        return os.path.isfile(opened_folder + "/artisan")

class GenerateRequestCommand(sublime_plugin.WindowCommand):
    def run(self):
        self.window.show_input_panel("Request Name", "", self.on_done, None, None)
        
    def on_done(self, name):
        folder = self.window.folders()
        opened_folder = folder[0]
        command_string = "php " + opened_folder + "/artisan make:request " + name
        os.system(command_string)

        self.window.open_file(opened_folder + "/app/Http/Requests/" + name + ".php")

    def is_enabled(self):
        folder = self.window.folders()
        opened_folder = folder[0]
        return os.path.isfile(opened_folder + "/artisan")

class SeedDatabaseCommand(sublime_plugin.WindowCommand):
    def run(self):
        folder = self.window.folders()
        opened_folder = folder[0]
        command_string = "php " + opened_folder + "/artisan db:seed"
        status = os.system(command_string)

        print status

    def is_enabled(self):
        folder = self.window.folders()
        opened_folder = folder[0]
        return os.path.isfile(opened_folder + "/artisan")

# context
class RouteCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.insert(edit, self.view.sel()[0].begin(), "Route::get('path', 'LaravelController@method')")
