from django.forms import ModelForm

from todo_app.models import Task, Comment

class TaskForm(ModelForm):
    ''' Pull the 'description' column from the Task  model into a form '''
    class Meta:
        model = Task
        fields = ['description']


class CommentForm(ModelForm):
    '''  Pull the 'body' column from the Task model into a form'''
    class Meta:
        model = Comment
        fields = ['body']
    
    # the form will get created with a task, we need to pull that task out and keep track of it

    def __init__(self, *args, **kwargs):
        task = kwargs.pop('task_object')
        super().__init__(*args, **kwargs)
        #  self.instance is the comment we are creating with htis form
        self.instance.task = task



# comment_form = CommmentForm(task_object=Task)

        