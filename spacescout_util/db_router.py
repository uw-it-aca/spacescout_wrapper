class LegacyRouter(object):
    """
    A router sending oauth to the right place 
    """
    def db_for_read(self, model, **hints):
        """
        """
        if model._meta.app_label == 'spacescout_admin':
            return 'admin'
        if model._meta.app_label == 'spacescout_web':
            return 'web'
        return 'server'

    def db_for_write(self, model, **hints):
        """
        """
        if model._meta.app_label == 'spacescout_admin':
            return 'admin'
        if model._meta.app_label == 'spacescout_web':
            return 'web'
        return 'server'

    def allow_relation(self, obj1, obj2, **hints):
        return True

    def allow_migrate(self, db, model):
        """
        """
        return None
