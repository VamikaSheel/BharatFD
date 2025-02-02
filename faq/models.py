from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator


class FAQ(models.Model):
    LANGUAGES = [('en', 'English'), ('hi', 'Hindi'), ('bn', 'Bengali'),] 
    question_en = models.TextField()
    answer_en = RichTextField()

    question_hi = models.TextField(blank=True, null=True)
    answer_hi = RichTextField(blank=True, null=True)

    question_bn = models.TextField(blank=True, null=True)
    answer_bn = RichTextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        translator = Translator()
        if not self.question_hi:
            self.question_hi = translator.translate(self.question_en, src="en", dest="hi").text
        if not self.question_bn:
            self.question_bn = translator.translate(self.question_en, src="en", dest="bn").text

        if not self.answer_hi:
            self.answer_hi = translator.translate(self.answer_en, src="en", dest="hi").text
        if not self.answer_bn:
            self.answer_bn = translator.translate(self.answer_en, src="en", dest="bn").text

        super().save(*args, **kwargs)
    
    def get_translated(self, lang):
        """ Return translated FAQ based on language """
        if lang not in ['hi', 'bn']:
            return {"question": self.question_en, "answer": self.answer_en}

        return {
            "question": getattr(self, f"question_{lang}", self.question_en),
            "answer": getattr(self, f"answer_{lang}", self.answer_en),
        }
    
    def __str__(self): 
        return self.question_en