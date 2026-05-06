from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from core.models import Post

class Command(BaseCommand):
    help = 'Create sample blog posts in English and Bangla'

    def handle(self, *args, **options):
        # Get or create a default user
        user, created = User.objects.get_or_create(
            username='admin',
            defaults={'email': 'admin@example.com'}
        )
        if created:
            user.set_password('admin123')
            user.save()

        # Sample English posts
        english_posts = [
            {
                'title': 'Getting Started with Django: A Complete Guide',
                'content': '''Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. In this comprehensive guide, we'll explore the fundamentals of Django development.

## Why Choose Django?

Django follows the "batteries included" philosophy, providing everything you need to build web applications out of the box. Here are some key advantages:

- **Rapid Development**: Django's ORM and admin interface speed up development significantly
- **Security**: Built-in protection against common security vulnerabilities
- **Scalability**: Used by companies like Instagram, Pinterest, and Mozilla
- **Community**: Large, active community with extensive documentation

## Setting Up Your First Django Project

Let's start by installing Django and creating your first project:

```bash
pip install django
django-admin startproject myproject
cd myproject
python manage.py runserver
```

## Key Django Concepts

### Models
Models define your data structure and relationships:

```python
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
```

### Views
Views handle the logic for processing requests and returning responses.

### Templates
Django's template system allows you to separate presentation from logic.

## Conclusion

Django is an excellent choice for web development projects of any size. Its comprehensive feature set and active community make it a reliable framework for both beginners and experienced developers.''',
                'language': 'en'
            },
            {
                'title': 'Modern Web Development Trends in 2024',
                'content': '''The web development landscape is constantly evolving. Here are the key trends shaping modern web development in 2024.

## Progressive Web Apps (PWAs)

PWAs combine the best of web and mobile applications, offering:
- Offline functionality
- Push notifications
- App-like user experience
- Cross-platform compatibility

## Server-Side Rendering and Static Site Generation

Modern frameworks like Next.js and Nuxt.js are pushing the boundaries of performance with advanced rendering techniques.

## AI-Powered Development

Artificial intelligence is transforming how we write code, with tools that can:
- Generate boilerplate code
- Suggest optimizations
- Debug issues automatically
- Convert designs to code

## WebAssembly

WebAssembly allows running high-performance code written in languages like C++, Rust, and Go directly in the browser.

## Edge Computing

Moving computation closer to users for faster response times and reduced latency.

The future of web development is exciting, with new technologies making it easier to build faster, more reliable, and feature-rich applications.''',
                'language': 'en'
            }
        ]

        # Sample Bangla posts
        bangla_posts = [
            {
                'title': 'ডjango দিয়ে শুরু করা: সম্পূর্ণ গাইড',
                'content': '''ডjango একটি উচ্চ-স্তরের Python ওয়েব ফ্রেমওয়ার্ক যা দ্রুত উন্নয়ন এবং পরিষ্কার, ব্যবহারিক ডিজাইনকে উৎসাহিত করে। এই বিস্তৃত গাইডে, আমরা ডjango উন্নয়নের মূল বিষয়গুলো অন্বেষণ করব।

## কেন ডjango বেছে নেবেন?

ডjango "ব্যাটারি অন্তর্ভুক্ত" দর্শন অনুসরণ করে, যা ওয়েব অ্যাপ্লিকেশন তৈরির জন্য প্রয়োজনীয় সবকিছু আউট অফ দ্য বক্স প্রদান করে। এখানে কিছু মূল সুবিধা:

- **দ্রুত উন্নয়ন**: ডjango এর ORM এবং অ্যাডমিন ইন্টারফেস উন্নয়নকে উল্লেখযোগ্যভাবে ত্বরান্বিত করে
- **নিরাপত্তা**: সাধারণ নিরাপত্তা দুর্বলতার বিরুদ্ধে অন্তর্নির্মিত সুরক্ষা
- **স্কেলেবিলিটি**: Instagram, Pinterest, এবং Mozilla এর মতো কোম্পানি দ্বারা ব্যবহৃত
- **কমিউনিটি**: বিস্তৃত ডকুমেন্টেশন সহ বড়, সক্রিয় কমিউনিটি

## আপনার প্রথম ডjango প্রজেক্ট সেটআপ করা

ডjango ইনস্টল করে এবং আপনার প্রথম প্রজেক্ট তৈরি করে শুরু করা যাক:

```bash
pip install django
django-admin startproject myproject
cd myproject
python manage.py runserver
```

## মূল ডjango ধারণা

### মডেল
মডেল আপনার ডেটা স্ট্রাকচার এবং সম্পর্ক নির্ধারণ করে।

### ভিউ
ভিউ রিকোয়েস্ট প্রসেস করার লজিক এবং রেসপন্স রিটার্ন করার জন্য হ্যান্ডেল করে।

### টেমপ্লেট
ডjango এর টেমপ্লেট সিস্টেম আপনাকে প্রেজেন্টেশনকে লজিক থেকে আলাদা করতে দেয়।

## উপসংহার

ডjango যেকোনো আকারের ওয়েব উন্নয়ন প্রজেক্টের জন্য একটি চমৎকার পছন্দ। এর বিস্তৃত ফিচার সেট এবং সক্রিয় কমিউনিটি এটাকে শিক্ষানবিস এবং অভিজ্ঞ ডেভেলপারদের জন্য একটি নির্ভরযোগ্য ফ্রেমওয়ার্ক করে তোলে।''',
                'language': 'bn'
            },
            {
                'title': '২০২৪ সালে আধুনিক ওয়েব উন্নয়নের প্রবণতা',
                'content': '''ওয়েব উন্নয়নের ল্যান্ডস্কেপ ক্রমাগত পরিবর্তিত হচ্ছে। এখানে ২০২৪ সালে আধুনিক ওয়েব উন্নয়নকে আকৃতি দেয় এমন মূল প্রবণতা।

## প্রগ্রেসিভ ওয়েব অ্যাপস (PWAs)

PWAs ওয়েব এবং মোবাইল অ্যাপ্লিকেশনের সেরা দিকগুলোকে একত্রিত করে, যা অফার করে:
- অফলাইন কার্যকারিতা
- পুশ নোটিফিকেশন
- অ্যাপ-লাইক ইউজার এক্সপেরিয়েন্স
- ক্রস-প্ল্যাটফর্ম কম্প্যাটিবিলিটি

## সার্ভার-সাইড রেন্ডারিং এবং স্ট্যাটিক সাইট জেনারেশন

Next.js এবং Nuxt.js এর মতো আধুনিক ফ্রেমওয়ার্ক উন্নত রেন্ডারিং টেকনিক দিয়ে পারফরম্যান্সের সীমানা ঠেলে দিচ্ছে।

## AI-চালিত উন্নয়ন

আর্টিফিশিয়াল ইন্টেলিজেন্স কোড লেখার পদ্ধতিকে পরিবর্তন করছে, যেমন টুলস যা:
- বয়লারপ্লেট কোড জেনারেট করতে পারে
- অপটিমাইজেশন সাজেস্ট করতে পারে
- স্বয়ংক্রিয়ভাবে ইস্যু ডিবাগ করতে পারে
- ডিজাইনকে কোডে কনভার্ট করতে পারে

## WebAssembly

WebAssembly C++, Rust, এবং Go এর মতো ভাষায় লিখিত হাই-পারফরম্যান্স কোডকে সরাসরি ব্রাউজারে রান করতে দেয়।

## এজ কম্পিউটিং

দ্রুত রেসপন্স টাইম এবং কম লেটেন্সির জন্য কম্পিউটেশনকে ইউজারদের কাছে নিয়ে আসা।

ওয়েব উন্নয়নের ভবিষ্যত উত্তেজনাপূর্ণ, নতুন প্রযুক্তি দিয়ে আরও দ্রুত, নির্ভরযোগ্য এবং ফিচার-সমৃদ্ধ অ্যাপ্লিকেশন তৈরি করা সহজ করে তুলছে।''',
                'language': 'bn'
            }
        ]

        # Create posts
        for post_data in english_posts + bangla_posts:
            Post.objects.get_or_create(
                title=post_data['title'],
                defaults={
                    'content': post_data['content'],
                    'author': user,
                    'language': post_data['language']
                }
            )

        self.stdout.write(
            self.style.SUCCESS(f'Successfully created sample posts in English and Bangla')
        )