from django.db import models


class SpecialisationChoices(models.TextChoices):
    MEDICAL = "MEDICAL", "Медицинская реабилитация"
    PHYSICAL = "PHYSICAL", "Физическая реабилитация"
    PSYCHOLOGICAL = "PSYCHOLOGICAL", "Психологическая реабилитация"
    SOCIAL = "SOCIAL", "Социально-бытовая реабилитация"
    PROFESSIONAL = "PROFESSIONAL", "Профессиональная реабилитация"
