# 22bq1a4737
affordmed repo
# 22bq1a4737
affordmed repo



This is a url shortner app that is builded on its own middlwware logging

To Test the app you can use curl operations

run django server


```cd urlshortner```
```python manage.py runserver```
then test with curl

```curl POST http://127.0.0.1:8000/shorten/
Content-Type: application/json

{
  "url": "https://www.google.com"
}
```
This should return a shortened url
