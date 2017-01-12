class View:
    @staticmethod
    def data_base_menu():
        print 'Main menu\n========='
        print 'Choose your menu item:'
        print '1)Contacts'
        print '2)Settings'
        print '3)Exit'

    @staticmethod
    def first_menu():
        print '=========================\n[Main menu] -> [Contacts]\n========================='
        print '1)Create new contact'
        print '2)Show all contacts'
        print '3)Save'
        print '4)'
        print '5)'
        print '6)Back'

    @staticmethod
    def second_menu():
        print '=========================\n[Main menu] -> [Second Menu]\n========================='
        print '1)'
        print '2)'
        print '3)'
        print '4)'
        print '5)Exit'



    @staticmethod
    def error_message(message):
        print '[ERROR]:' + message + '\n'

    @staticmethod
    def success_message(message):
        print message + '\n'

    @staticmethod
    def sample(message):
        print "Sample Title"