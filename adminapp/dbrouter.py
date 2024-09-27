class MultiDBRouter:
    """
    A router to control all database operations on models in the
    'adminapp' and 'userapp' applications, directing them to the appropriate database.
    """

    def db_for_read(self, model, **hints):
        """
        Attempts to read from the appropriate database based on the model's app label.
        """
        if model._meta.app_label == 'adminapp':
            return 'default'  # Use the 'default' database for adminapp reads
        elif model._meta.app_label == 'userapp':
            return 'referencedb1'  # Use the 'referencedb1' database for userapp reads
        return None  # Default behavior

    def db_for_write(self, model, **hints):
        """
        Attempts to write to the appropriate database based on the model's app label.
        """
        if model._meta.app_label == 'adminapp':
            return 'default'  # Use the 'default' database for adminapp writes
        elif model._meta.app_label == 'userapp':
            return 'referencedb1'  # Use the 'referencedb1' database for userapp writes
        return None  # Default behavior

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in 'adminapp' or 'userapp' is involved.
        """
        if obj1._meta.app_label in ['adminapp', 'userapp'] or obj2._meta.app_label in ['adminapp', 'userapp']:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Allow migrations for specific apps to their respective databases.
        """
        if app_label == 'adminapp':
            return db == 'default'
        elif app_label == 'userapp':
            return db == 'referencedb1'
        return None
