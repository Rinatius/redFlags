from django.db import models


class IdModel(models.Model):
    id = models.CharField(primary_key=True, max_length=400)

    class Meta:
        abstract = True


class NameModel(models.Model):
    name = models.TextField(null=True)
    description = models.TextField(null=True)

    class Meta:
        abstract = True


class URLModel(models.Model):
    url = models.URLField(max_length=400)

    class Meta:
        abstract = True


class Entity(IdModel, NameModel, URLModel):
    class Meta:
        verbose_name_plural = "Entities"

    def __str__(self):
        return self.name


class Classifier(IdModel, NameModel):

    def __str__(self):
        return self.name


class Tender(IdModel, NameModel, URLModel):
    procuring_entity = models.ForeignKey(Entity, on_delete=models.CASCADE)
    classifier = models.ForeignKey(Classifier, null=True,
                                   on_delete=models.CASCADE)
    start_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Lot(IdModel, NameModel):
    tender = models.ForeignKey(Tender, on_delete=models.CASCADE)
    classifier = models.ForeignKey(Classifier, null=True,
                                   on_delete=models.CASCADE)
    price = models.FloatField()
    bidders = models.ManyToManyField(Entity, through="Bid")

    class Meta:
        ordering = ['tender__name']

    def __str__(self):
        return self.name


class Bid(IdModel):
    price = models.FloatField(null=True)
    status = models.CharField(blank=True, max_length=200)
    time = models.DateTimeField(null=True)
    won = models.BooleanField(null=True)
    lot = models.ForeignKey(Lot, on_delete=models.CASCADE)
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE)


class Irregularity(IdModel, NameModel):

    def __str__(self):
        return self.name


class Flag(IdModel, NameModel):
    irregularity = models.ForeignKey(
        Irregularity,
        on_delete=models.CASCADE,
    )
    tender = models.ForeignKey(
        Tender,
        on_delete=models.CASCADE,
        null=True,
        related_name='flags',
    )
    lot = models.ForeignKey(Lot, on_delete=models.CASCADE, null=True)
    data = models.JSONField(null=True)

    def __str__(self):
        return self.name
