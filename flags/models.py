from django.db import models


class IdModel(models.Model):
    id = models.CharField(primary_key=True, max_length=400)

    class Meta:
        abstract = True


class NameModel(models.Model):
    name = models.TextField(blank=True)
    description = models.TextField(blank=True)

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

    def __str__(self):
        return self.name


class Lot(IdModel, NameModel):
    tender = models.ForeignKey(Tender, on_delete=models.CASCADE)
    classifier = models.ForeignKey(Classifier, null=True,
                                   on_delete=models.CASCADE)
    price = models.FloatField()
    bidders = models.ManyToManyField(Entity, through="Bid")

    def __str__(self):
        return self.name


class Bid(IdModel):
    price = models.FloatField()
    status = models.CharField(blank=True, max_length=200)
    time = models.DateTimeField(null=True)
    won = models.BooleanField(null=True)
    lot = models.ForeignKey(Lot, on_delete=models.CASCADE)
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Irregularity(IdModel, NameModel):

    def __str__(self):
        return self.name


class Flag(IdModel, NameModel):
    irregularity = models.ForeignKey(Irregularity, on_delete=models.CASCADE)
    tender = models.ForeignKey(Tender, on_delete=models.CASCADE)
    lot = models.ForeignKey(Lot, on_delete=models.CASCADE, null=True)
    data = models.JSONField(null=True)

    def __str__(self):
        return self.name
