# Generate admin models here

from django.contrib import admin
from .models import GradingBasis, GradingBasisValue

class GradingBasisValueInline(admin.TabularInline):
    model = GradingBasisValue
    extra = 0

@admin.register(GradingBasis)
class GradingBasisAdmin(admin.ModelAdmin):
    inlines = [GradingBasisValueInline]
