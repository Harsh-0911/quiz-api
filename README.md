
# **Quiz API** 

## **Problem Statement**

###  1. Design a DB and an API server in Django that has the following functionality:
    1. Admin should be able to create and schedule quizzes
    2. Each quiz can have 1 or more questions and the question types can be MCQ (2-4 options) or open text
    3. A question will have text and optionally an imag
    4. A user should be able to see the list of quizzes (live, past and upcoming)
    5. A user should be able to attempt live quizzes (at max once)
    6. Refer Summachar’s android app http://bit.ly/summachar_android
    or https://instagram.com/summachar_in to see how quizzes are
    done in the app/on IG stories

### 2. Describe points to consider if the API server needs to support 1million users accessing the live quiz at the same time.

---
<br />

## Installation

* Run following command in CMD
```bash
python -m pip install requirments.txt
python manage.py makemigrations
python manage.py migrate
```
<br />

## Demo

* There is demo data already in database to test the API.
* Admin username and password in `admin`.

<br />

## **API Reference**

#### Get all live quizzes

```http
  GET /api/
```

#### Get all past quizzes

```http
  GET /api/p/
```

#### Get all future quizzes

```http
    GET /api/f/
```

#### Get all questions and answers of a quiz

```http
    GET api/q/<str:quiz_title>
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `quiz_title` | `string` | **Required**. Title of the quiz |

<br />

## **Notes**

* You will get the path of image from either `api/a/{title}` or `api/q/{title}` endpoint. 
    To access the image in development server build the path like this `http://127.0.0.1:8000/{path/of/image}`

* To solve the problem that user can access only one live quiz, we can set
    a flag that we'll set when the user will start a live quiz and we'll unset
    that live flag when the quiz ends. Untill the flag is set user ca not acess
    any other quiz.
* This thing can not be done on this API server as it only deals with quiz data and
    not with user data.

* Points to consider if API needs to support 1 million users accessing the 
    live quiz at the same time.

    * The way this API is built is that it requires only one API call if the quiz not contains any images
        to get all the data about the quiz (Questions and answers).
    * My suggestion is we can go with cloud hosting like AWS. (E.g. EC2 - Amazon Elastic Compute Cloud)