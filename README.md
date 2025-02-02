# BharatFD - Multilingual FAQ Management System 

Welcome to the **BharatFD** project! This is a Django-based FAQ Management System that supports multilingual content, efficient Redis caching, and a REST API for managing FAQs. The application is designed to allow easy handling of FAQs in different languages, offering translations on-the-fly and ensuring optimal performance with caching.

## Features

- **Multilingual FAQ Management**: Store and manage FAQs in multiple languages, including support for English, Hindi, and Bengali.
- **WYSIWYG Editor Support**: Rich text support for the FAQ answers using the Django CKEditor.
- **Dynamic Translations**: Automatic translation of FAQ content during object creation, with a fallback to English if translation is unavailable.
- **REST API**: Fetch FAQs based on a selected language using a dynamic `?lang=` query parameter.
- **Redis Caching**: Use Redis to cache translations for fast retrieval & efficient performance.
- **Admin Panel**: User-friendly Django admin interface to manage FAQs.
- **Unit Testing**: Unit tests to ensure the application works as expected.

## Demo Video 📽️

Check out the demo video to see the application in action:

[![Watch the demo](https://res.cloudinary.com/dhroesok2/video/upload/v1738497173/Project_Recording_g3pkir.jpg)](https://res.cloudinary.com/dhroesok2/video/upload/v1738497173/Project_Recording_g3pkir.mkv)

## Prerequisites

Ensure you have the following installed:

- Python 3.x
- Django
- Redis (for caching)
- Google Translate API or `googletrans` for language translation
- Django CKEditor for rich text support

## Installation

### Clone the Repository 🍀

Start by cloning the repository to your local machine:

```bash
git clone https://github.com/VamikaSheel/BharatFD.git
cd BharatFD
