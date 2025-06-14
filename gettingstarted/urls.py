"""
URL configuration for gettingstarted project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
"""
from django.urls import path

# Forma más limpia de importar: Traemos cada función que necesitamos directamente
from hello.views import webhook, index, db 

urlpatterns = [
    # El webhook para WhatsApp
    path("webhook", webhook, name="webhook"),
    
    # Las rutas originales del proyecto de ejemplo
    path("", index, name="index"),
    path("db", db, name="db"),
]
