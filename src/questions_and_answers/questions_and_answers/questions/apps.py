from django.apps import AppConfig


class QuestionsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'questions_and_answers.questions'

    def ready(self):
        import questions_and_answers.questions.signals
