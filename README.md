# Playstation Store Clone - An App in Django & React

## Overview

This was my final project on the General Assembly Software Engineering Course, and was undertaken in the final week of the course.

## Installation Instructions
- Clone repo code from GitHub
- Run pipenv i in the root directory to install all packages from Pipfile.
- Run pipenv shell in the root directory to spawn a shell within the virtual environment.
- Use python manage.py runserver to start the backend server in the root directory.
- Open a second window of VS Code and open client.
- Use npm i in client to install all dependencies.
- Run npm run dev from client to start the frontend.


## Goal and Timeframe

For Project 4 we had 7 days to build a full stack RESTful app with CRUD functionality, using React.js and Django.

I chose to create a clone of the Playstation Store, as this is a React app I’ve had a lot of experience with and thought it would be fun to recreate. My main goal with Project 4 was to consolidate all I’d learned so far with regards to React and use that to reproduce something complex yet familiar.

I chose to work solo for this project as I wanted to test my own knowledge and find out where I needed to improve my understanding.

## Planning

I began by sketching out my plan in Excalidraw - as this was a clone of an existing app, I used parts of the existing Playstation store for reference:

##### Login pages:

![](https://github.com/theobrooke009/project-four-remaster-frontend/blob/main/readme-images/readme-img-12.png)

##### Store & game pages:

![](https://github.com/theobrooke009/project-four-remaster-frontend/blob/main/readme-images/readme-img-13.png)

##### User profile pages:

![](https://github.com/theobrooke009/project-four-remaster-frontend/blob/main/readme-images/readme-img-14.png)


As this was an exercise in knowledge consolidation, I started by creating a detailed, day by day plan, steadily building up the app and in features from the ground up. As this was a solo project, my approach was to work methodically and exclusively on an individual feature until it was functional, before moving onto the next one.

I decided to build the login and register features first, before moving on to the index and search features, and then finally I worked on the user interaction features (liking/commenting/adding games).

## Back-End Development

This was my first time using Python to create a back end and I used Django and Django REST Framework to create a PostgreSQL database with RESTful features. Django is surprisingly intuitive when it comes to this setup and when it comes to setting up the database.

The back end has 3 models - Games, Users & Reviews, with the following one to many relationships:

 - Games > Comments
 - Users > Games
 - Games > Comments

The Games model is the main model and I used it to control how information was displayed on the front-end, as well as any user added content, filtering or recommendations:

```python
class Games(models.Model):
    name = models.CharField(max_length=50, unique=True)
    image = models.CharField(max_length=400)
    price = models.FloatField()
    platform = models.CharField(max_length=50)
    genre = models.CharField(max_length=50, default='Action')
    full_game = models.CharField(max_length=50)
    game_info = models.CharField(max_length=5000)
    size = models.FloatField()
    release_date = models.DateField()
    developer = models.CharField(max_length=50)
    rating = models.CharField(max_length=300, blank=True)
    is_official = models.BooleanField(default=True)
    liked_by = models.ManyToManyField(
        'jwt_auth.User',
        related_name='liked_games',
        blank=True
    )

```

Additionally I created 8 views, each relating to a different part of the site’s core functionality - login & register, like & comment, browsing & post.

The views.py & urls.py for the Games model have 5 requests, relating to 6 off these views, with login & register applying to the Users model:

```python
urlpatterns = [
    path('', GameListView.as_view()),
    path('<int:pk>/', GameDetailView.as_view()),
    path('<int:game_pk>/comments/', CommentListView.as_view()),
    path('<int:game_pk>/comments/<int:comment_pk>/', CommentDetailView.as_view()),
    path('<int:game_pk>/like/', GameLikeView.as_view())
]
```

I tested the back end extensively in Insomnia, making sure that every request and relationship was functional and behaving as expected before moving on to the front end.

## Front End Development

The front end was built using React and my aim was to capture as much of the functionality and  feel of the Playstation Store as possible.

I used React hooks throughout and built the site steadily from the ground up, beginning with user registration & login, before moving onto the index page, individual game profiles and finally, social features such as liking and leaving reviews.

I approached each component methodically - beginning with the front end request before moving on to data manipulation and styling. It was this approach which greatly accelerated my understanding of the request response cycle, which had previously been a pretty large gap in my knowledge.

#### Sample Code

The below is from the individual game profile page; this component features multiple hooks and, as this is the page with the most user interaction is probably the most complex part of the project:

```javascript
React.useEffect(() => {
    const getData = async () => {
      try {
        const response = await getOneGame(gameId)
        setGame(response.data)
      } catch (err) {
        setIsError(true)
      }
    }
    getData()
  }, [gameId])

  React.useEffect(() => {
    const getData = async () => {
      try {
        const response = await getAllGames()
        setAllGames(response.data)
      } catch (err) {
        setIsError(true)
      }
    }
    getData()
  },[gameId])

  React.useEffect(() => {
    const getData = async () => {
      try {
        const response = await getUser()
        setUser(response)
      } catch (err) {
        setIsError(true)
      }
    } 
    getData()
  },[] )
```

On this page I wanted individual information, but also wanted to display recommended games (as in ones in the same genre, but excluding the game on the page) along with user specific information.

One of the biggest challenges here was having the status of the selected game to persist in the like (purchase button) when the page loads, with games already liked showing the user a different message than ones which hadn’t been, much like in the real Playstation Store.

## App Flow

The landing page has three options - sign up, sign in and store:

![](https://github.com/theobrooke009/project-four-remaster-frontend/blob/main/readme-images/readme-img-1.png)

The store option without logging in only has search functionality:

![](https://github.com/theobrooke009/project-four-remaster-frontend/blob/main/readme-images/readme-img-2.png)

![](https://github.com/theobrooke009/project-four-remaster-frontend/blob/main/readme-images/readme-img-3.png)

![](https://github.com/theobrooke009/project-four-remaster-frontend/blob/main/readme-images/readme-img-4.png)

After signing in, the full functionality of the app is possible:

![](https://github.com/theobrooke009/project-four-remaster-frontend/blob/main/readme-images/readme-img-5.png)

Individual games are accessible and will provide recommendations:

![](https://github.com/theobrooke009/project-four-remaster-frontend/blob/main/readme-images/readme-img-6.png)

Add to cart functions as a like button and will push the game through to the user profile:

![](https://github.com/theobrooke009/project-four-remaster-frontend/blob/main/readme-images/readme-img-7.png)

From the game profile, the user can also leave reviews:

![](https://github.com/theobrooke009/project-four-remaster-frontend/blob/main/readme-images/readme-img-8.png)

![](https://github.com/theobrooke009/project-four-remaster-frontend/blob/main/readme-images/readme-img-9.png)

Using the submit game feature will allow the user to add a game to the Indie games section:

![](https://github.com/theobrooke009/project-four-remaster-frontend/blob/main/readme-images/readme-img-10.png)

![](https://github.com/theobrooke009/project-four-remaster-frontend/blob/main/readme-images/readme-img-11.png)

## Challenges

As I chose to build this entirely myself, the biggest challenge here was definitely the request response cycle. This was the first time I’d used a React frontend & Django backend. I overcame this through taking a slow, methodical approach combined with extensive testing of all requests.

## Wins

The biggest win was definitely building something from the ground up by myself. This really solidified my understanding of React as well as giving me a good grounding and confidence in the technologies I was using for the first time (Python/Django/SQL etc). I feel that I planned my work well and made sure to thoroughly troubleshoot all the issues which came up.

I also managed to build most of the functionality which hadn’t worked or has been buggy in Project 3 - this is why I chose something relatively simple, because I saw the most important thing to me was addressing previous gaps in my understanding and really nailing the fundamentals of full stack development.

Additionally, building something I was familiar with in a medium I was unfamiliar with definitely helped me understand how concepts are applicable across different languages, which provided me with a firm foundation and context for my future learning.

## Known Bugs

 The A-Z filter on the main index page doesn’t work as intended. (NOW FIXED)

## Future Improvements

 In future I’m going to expand on the store parts, adding a shopping cart in place of the like-as-purchase feature.
 Improve the recommended features, having them not just give games of the same genre, but by publisher and liked by users as well.
 Add a review score to the comments.
 Add more social features to the front end (recent comments/reviews etc).
 Add a friend system.

## Key Learnings/Takeaways

My biggest learning here was definitely how to plan my work. I wrote out how to move methodically through building my app, going slowly, and feature by feature, making sure that what I was working on was finished and working as intended before I moved on. That way I didn’t end up with a lot of things that were 75% complete and a load of confusion about what still needed to be done. I felt that I planned effectively enough, and combined with a more developed sense of what full stack development is, this made for a relatively drama free week where I was able to really get a handle on everything we’d learned in React.

From a technical perspective, I definitely now have a better understanding of the request/response cycle. Once I’d taken the time to understand how both the front and back end requests interact with each other, that’s when everything came together and I felt as if I had the final piece of the puzzle.




