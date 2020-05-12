# Bonus Project 1: Text-based Adventure Game

Congratulations on completing the course and the Final Project. You should be really proud of yourself; to come this far in programming takes a lot of dedication and problem-solving skills! This series of pages was intended for you guys to have some code to play with in between now and when we start offering more advanced courses in summer. Feel free to move through these pages at your own pace and on your own time. If you get stuck or have any questions, you can contact us at jade@andoverrobotics.com. 

Have fun!


-----

### BONUS PROJECT 1: TEXT-BASED ADVENTURE GAME

Your task is to create a text-based adventure game similar to the one in the video (you should have an email from Glenn with the demo video) or the Oregon Trail: the overarching goal is to create a user experience in which the player makes decisions that determine their performance in the game. This could be any kind of game: it could be like the Oregon Trail, or it could take place in any kind of world you want. We encourage you to get creative and make the project something you really like! 

The backbone requirements:
- The player should either be able to win/lose or have a final “score” based on their decisions and use of resources
- The player should have resources of some kind stored in variables. This could really be anything (like food, water, battery charge, anything!)
- There should be some sort of conditional tree: that is, each decision the player makes should influence something about what happens next in the game, and will eventually lead to winning, losing, or a high/low score.
- Including loops and functions will make your code easier to write AND read, so we really recommend that you include them!

Overview of Random Number Generation (this is not required to do the project since we didn’t formally teach it to you, but it might be a helpful tool when constructing an adventure game):
The Python function that produces random numbers is ``` random.randint(a, b)```. This function produces a random number between a and b, inclusive. 
You might be wondering how a random number can actually produce a random CHOICE: in an example code like this, each number is assigned to a choice such that a decision will be made randomly based on a list of choices.
```import random
weather_choice_list = ["Thunderstorm", "Rain", "Sun", "Partly Cloudy", "Snow", "Tornado"]
 
my_choice_num = random.randint(0, len(weather_choice_list) - 1)
my_choice = weather_choice_list[my_choice_num]
print(my_choice)
```

To read more, go to https://docs.python.org/3/library/random.html -- the official documentation on the subject. (It is a little intimidating at first, but eventually you’ll become a pro at searching for what you need in documentation!)

Stay tuned for more bonus projects: they'll appear in the next few days!

{Try It | terminal}(python3 bonus_1.py ; read -n 1 -s -r -p "Press any key to exit" ; exit)

