import json
from django.core.management.base import BaseCommand
from quiz.models import Question

class Command(BaseCommand):
    help = 'Populate the database with questions from a JSON file'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str, help='The path to the JSON file containing questions')

    def handle(self, *args, **kwargs):
        json_file = kwargs['json_file']
        
        try:
            with open(json_file, 'r') as file:
                questions_data = json.load(file)
                for question in questions_data:
                    Question.objects.create(
                        question_text=question['question_text'],
                        option_a=question['option_a'],
                        option_b=question['option_b'],
                        option_c=question['option_c'],
                        option_d=question['option_d'],
                        correct_answer=question['correct_answer']
                    )
                self.stdout.write(self.style.SUCCESS('Successfully populated questions from JSON file.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {str(e)}'))