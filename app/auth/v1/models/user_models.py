class UserModel:
    '''
    Class for user authentication
    '''
    user = {}

    def __init__(self,email,password,confirm_password,task,tasktimer,taskbreak):
        '''
        Initialising the user model
        '''
        self.id = len(  UserModel.user) + 1
        self.email = email
        self.password = password
        self.confirm_confirm = confirm_password
        self.task = task
        self.tasktimer = tasktimer
        self.taskbreak = taskbreak

    def save_user(self):
        '''
        Method to register a user instance and update the data struchture

        '''    
        user_record = dict(
            id = self.id,
            email = self.email,
            password = self.password,
            confirm_password = self.confirm_password,
            task =self.task,
            tasttimer = self.tasktimer,
            taskbreak =self.taskbreak
            
        )
        self.users.update({
            self.id: user_record
        })