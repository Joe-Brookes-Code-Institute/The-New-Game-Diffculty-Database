# The-Game-Diffculty-Database
![Creating your first README hero image]![image](https://github.com/user-attachments/assets/86d4475c-2c4d-46c3-abca-7d9ae162ca6d)




![Markdown](https://img.shields.io/badge/markdown-%23000000.svg?style=flat=markdown&logoColor=white) ![GitHub contributors](https://img.shields.io/github/contributors/kera-cudmore/readme-examples?style=flat) ![GitHub last commit](https://img.shields.io/github/last-commit/kera-cudmore/readme-examples?style=flat)  ![GitHub Repo stars](https://img.shields.io/github/stars/kera-cudmore/readme-examples?style=social)  ![GitHub forks](https://img.shields.io/github/forks/kera-cudmore/readme-examples?style=social)

So you're starting to think about your first milestone project, and are brainstorming ideas - but have you thought about your README? This repository (and accompanying webinar) are an introduction to creating your first README - covering what to include, why you need one and how to write it.

Find the slide show for this webinar [here](https://docs.google.com/presentation/d/19_7r_To5bu7UjnZD87hrzWQi63Ij0YpaRH1XFnPZZe8/edit?usp=sharing)

⭐️ If you found this repo useful for creating your first README, please consider giving the repo a star - and if you mention me in the credits section of your readme, please do send me a message on slack - you'll make my day! 😊

- - -

## CONTENTS

* [Whats A README?](#whats-a-readme)
* [What Makes a Good README?](#what-makes-a-good-readme)
* [README Examples](#readme-examples)
* [How to Write Your README](#how-to-write-your-readme)
  * [Headings](#headings)
  * [Links](#links)
  * [Inserting Images](#inserting-images)
  * [Italic, Bold & Code](#italic-bold-and-code)
  * [Strikethrough & Bullet Points](#strikethrough--bullet-points)
  * [Code Blocks](#code-blocks)
  * [Tables](#tables)
* [Nice Extras & Other Interesting Tools](#nice-extras--other-interesting-tools)
* [Further Reading](#further-reading)
* [Credits](#credits)
  * [Media](#media)
  * [Acknowledgments](#acknowledgments)

- - -

## What's is The-Game-Diffculty-Database

The Game Difficulty Database is a platform designed to provide detailed information about the difficulty settings of various games. It helps players understand how different difficulty levels affect gameplay and overall experience.
- - -

## Why

Many games lack detailed descriptions of their difficulty settings, often providing only vague statements. This database aims to fill that gap by offering comprehensive rundowns and opinions on optimal settings, enhancing players' overall enjoyment and helping them make informed decisions.

- - -

## Examples

![image](https://github.com/user-attachments/assets/96dd5766-cf1f-40db-9368-43692b584f13)
- - -

## How to use the Database

Submitting Information
To submit information about a game:

Click the "Submit" button.
Fill out the form with game details and difficulty settings.
Click "Submit" to add your information to the database.
Retrieving Information
To retrieve information:

Navigate to the search section.
Select the categories you're interested in, such as custom difficulty features.
Browse through the results based on your selected criteria.

### Features

Submit Game Information: Add details about game difficulty settings.
Search Functionality: Find games based on various difficulty features and settings.

### Links

### Inserting Images

Images can be inserted in your README in the same way as a link, if you only want the name of the image to be displayed.

If you want the image itself to be visible in the README, you just need to place an exclamation mark at the front of the link, example shown below:

![Inserting an Image Link Example](documentation/imagelink-example.png)

Its important to be mindful of what you use in the square brackets of an image link, as this is what will be displayed on the page if the image fails to load, so make sure to use something descriptive, similar to an image alt tag.

When using images in your README, its good practice to compress the image first (PNG format seems to work best), I can recommend [tinyPNG](https://tinypng.com/). I then like to keep all images etc used within the README in a folder called *documentation*. This is good practice as it keeps the sites assets seperate from the assets used in your documentation.

###  Italic, Bold and Code![image](https://github.com/user-attachments/assets/910dcfa0-0040-4e73-9a83-26c84fceb02b)


*Italic text* we can either use an asterisk or an underscore before and after the text.

**Bold text** we can either use double asterisks or double underscores before and after the text.

`Code` we enclose the text in backticks.

![Styled Text Examples](documentation/styledtext-example.png)

### Strikethrough & Bullet Points

~~strikethrough~~ We use double tilder before and after.

* Bullet points, we use either an asterisk or a dash.
  * Nested Bullet Points are created by indenting two spaces
    * Another Nested Bullet Point

![Strikethrough & Bullet Point Example](documentation/strikethrough-bullet-example.png)

To create a numbered list we simply put a number followed by a full stop, then a space before the content.

1. First item
2. Second item
3. Third Item

![Numbered list example code](documentation/numbered-list-example.png)

### Code Blocks

Code blocks can be used in Markdown to display a larger block of code. To create a code block you need to prefix the text with three backticks and end with three backticks after.

Code blocks can be language specific, you simply need to add the language after the first set of backticks - if you don't want to use a specific language, you can use text.

**Plain Text Code Block:**

```text
function fibonacci(num, memo) {
  memo = memo || {};

  if (memo[num]) return memo[num];
  if (num <= 1) return 1;

  return memo[num] = fibonacci(num - 1, memo) + fibonacci(num - 2, memo);
}
```

**JavaScript Code Block:**

```javascript
function fibonacci(num, memo) {
  memo = memo || {};

  if (memo[num]) return memo[num];
  if (num <= 1) return 1;

  return memo[num] = fibonacci(num - 1, memo) + fibonacci(num - 2, memo);
}
```

Code Block Markdown Examples:

![Code Block Examples](documentation/codeblock-example.png)

### Tables

Tables can be a great way to display information in your README, but can be a bit fiddly to get your head around at first. Tables are created using the pipe symbol ( | ) which is placed on either side of the content, creating the sides of the table. The first row of the table will be the headings for the table. This is then followed by a row with 3 dashes in each cell, and then you just add the contents for the table in the following rows.

-----------------------------------------------------------
| Navigation Bar: Home | Games | Submit | Login/Register  |
-----------------------------------------------------------
|               Submit Difficulty Information              |
|---------------------------------------------------------|
|                                                         |
|   Game:               [Dropdown]                        |
|                                                         |
|   Difficulty:         [Dropdown]                        |
|                                                         |
|   Enemy Health:       [Input Field]                     |
|                                                         |
|   AI Difficulty:      [Dropdown or Input Field]          |
|                                                         |
|   Player Health:      [Input Field]                     |
|                                                         |
|   Resources Available: [Dropdown or Input Field]        |
|                                                         |
|   Opinion:            [Text Area]                       |
|                                                         |
|---------------------------------------------------------|
|                Additional Features (Tick Boxes)         |
|   [ ] Extra Content                                      |
|   [ ] Exclusive Unlockables                              |
|   [ ] Trophies                                           |
|   [ ] Unlockable Difficulty                              |
|   [ ] New Game Plus Only                                 |
|   [ ] Switchable Mid-Game                                |
|   [ ] Trophy Stacking                                    |
|---------------------------------------------------------|
|   Other (Not Listed): [Text Box for custom features]     |
|---------------------------------------------------------|
|                [Submit Button]                          |
-----------------------------------------------------------

-----------------------------------------------------------
| Navigation Bar: Home | Games | Submit | Login/Register  |
-----------------------------------------------------------
|               Submit Difficulty Information              |
|---------------------------------------------------------|
|                                                         |
|   Game:               [Devil May Cry V]                 |
|                                                         |
|   Difficulty:         [Dante Must Die/Very Hard]        |
|                                                         |
|   Enemy Health:       [200%]                            |
|                                                         |
|   AI Difficulty:      [Yes]                             |
|                                                         |
|   Player Health:      [33%]                             |
|                                                         |
|   Resources Available: [Lowered]                        |
|                                                         |
|   Opinion:                                               |
|                                                         |
|       Dante Must Die difficulty is only available for    |
|       players who have beaten the game on both Devil     |
|       Hunter and Son of Sparda difficulties. However,    |
|       for players on the PS5 and Series X versions, it   |
|       can be unlocked simply by beating the game once    |
|       on Legendary Dark Knight. This difficulty setting  |
|       is generally aimed at players playing on New Game  |
|       Plus who have already maxed out their character    |
|       data. It includes rearranged enemies who are both  |
|       more intelligent, more aggressive, and can take    |
|       more damage.                                       |
|                                                         |
|       While this could be irritating in some genres,     |
|       I would say that Devil May Cry does a good job of  |
|       handling it due to the game's focus on combos,     |
|       tricks, and dealing a large amount of damage to    |
|       individual enemies without taking a single hit.    |
|       As a result, I don't feel that the increased enemy |
|       health detracts from the core pillars of the game. |
|                                                         |
|       If there is one major flaw to Dante Must Die       |
|       difficulty, it's that the game's health and life   |
|       system is still very exploitable. Players can      |
|       easily spam gold orbs, and to make things      |
|       worse, there is a pay-to-win system where players  |
|       can pay real money to come back to life in the     |
|       game. This somewhat hurts my ability to recommend  |
|       this as a good difficulty setting, although in     |
|       most other ways, it's a solid and unexpected       |
|       inclusion.                                         |
|                                                         |
|---------------------------------------------------------|
|                Additional Features (Tick Boxes)         |
|   [ ] Extra Content                                      |
|   [X] Exclusive Unlockables                              |
|   [X] Trophies                                           |
|   [X] Unlockable Difficulty                              |
|   [X] New Game Plus Only                                 |
|   [X] Switchable Mid-Game                                |
|   [X] Trophy Stacking   
|  `[X] PTW
|---------------------------------------------------------|
|   Other (Not Listed): [Text Box for custom features]     |
|---------------------------------------------------------|
|                [Submit Button]                          |
-----------------------------------------------------------

-----------------------------------------------------------





Markdown for creating a table:

![Table Example](documentation/table-example.png)

You can also justify the contents within a table! You simply need to add a colon to the second row of dashes - place the colon on the left of the dashes for left justification, to the right of the dashes for right justification and to center the text, place a colon on each side of the dashes.

| Table Heading 1 for justification example | Table Heading 2 For justification example |
| :--- | :--- |
| Justify contents| To the Left |

| Table Heading 1 for justification example | Table Heading 2 For justification example |
| ---: | ---: |
| Justify contents | To the Right |

| Table Heading 1 for justification example | Table Heading 2 For justification example |
| :---: | :---: |
| Justify contents | In the Center |

![Table Justification Example Code](documentation/table-justification-example.png)
 - - -

## Nice Extras & Other Interesting Tools

Nice extras we could include in the README:

[shields.io Badges](https://shields.io/) -  lots of badges relating to site builds. I like to add these after the site image at the top of my README. I like to include the following badges in my projects, but have an explore and see if there are any others you could use (they are also great to include in your GitHub Profile!)

* GitHub last commit (Shows when the last commit to the repo was)
* GitHub contributors (Great to show at a glance you are the only contributor to your project)
* GitHub language count (Shows how many languages used in project)
* GitHub top language (to display top language used in the project)
* W3C validation (shows at a glance whether your HTML passes validation)

![Shields.io Exmaple Badges](documentation/shields-example.png)

[Gyazo GIF](https://gyazo.com) - A tool that allows you to capture a short video recording of your screen as a GIF. I like to use this to document a bug I might have (For example in my second project, each time a button was pressed the score would increase when it shouldn't have - this was a great way to capture what was happening). Have a look, or perhaps you have your own preferred screen recording tool you prefer.

[Chrome Extension Spell Checker](https://chrome.google.com/webstore/detail/webpage-spell-check/mgdhaoimpabdhmacaclbbjddhngchjik) - I love to use this both on my site and to check over my README before submission, as its easy to get spelling errors creeping into your project as you burn the midnight oil towards the end as your deadline is looming.

[Chrome Exension WAVE](https://chrome.google.com/webstore/detail/wave-evaluation-tool/jbbplnpkjmmeebjpijfedlgcdilocofh) - WAVE is a web accessibility evaluation tool developed by [WebAIM.org](https://wave.webaim.org/). It provides visual feedback about the accessibility of your web content by injecting icons and indicators into your page. No automated tool can tell you if your page is accessible, but WAVE facilitates human evaluation and educates about accessibility issues. All analysis is done entirely within the Chrome browser allowing secure valuation of intranet, local, password protected, and other sensitive web pages. I believe there is also an extension for Firefox.

[Web Disability Simulator](https://chrome.google.com/webstore/detail/web-disability-simulator/olioanlbgbpmdlgjnnampnnlohigkjla) - A fantastic chrome extension that allows you to simulate how certain disabilities can affect the users experience of your site. Really useful if you're using colour to represent a result - for example in a quiz.

- - -

## Further Reading

* [Markdown Syntax](https://www.markdownguide.org/basic-syntax/) - This site is really comprehensive on all the different things you can do in Markdown.
* [Markdown Table Generator](https://www.tablesgenerator.com/markdown_tables) - This may be useful to have a play around with to better understand how tables work in Markdown.
* [Markdown Cheatsheet](https://github.com/atapas/markdown-cheatsheet) - A great markdown cheatsheet created by Atapas.
* [Code Institute Sample README](https://github.com/Code-Institute-Solutions/SampleREADME) - Sample README created by the Code Institute

## Credits

### Media

• All screenshots of code used in this README were taken by myself from my own milestone project repositories or Code Institute hackathon projects I have participated in.

• [README hero image](https://www.slidescarnival.com/aliena-free-presentation-template/4597) - Slide template from Slide Carnival

### Acknowledgments

* [Ed](https://github.com/Edb83) - For letting me know about the heading links feature.
* [Dave](https://github.com/daveyjh) - For letting me know about table justification in markdown.
* Nerd Alert - For cheering me on while creating this webinar, and for proof-reading my documents.
* A big thank you to Jim at Code Institute for the opportunity to be a channel lead for the Milestone 1 slack channel.
