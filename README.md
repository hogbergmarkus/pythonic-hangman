# Hangman

![Hangman game](documentation/images/game_image_introduction.png)

## Introduction

[Pythonic Hangman](https://pythonic-hangman-0358ff7c5393.herokuapp.com/) is a fun text-based
game of Hangman, that runs in a mock terminal on Heroku.

You are able to choose from three difficulty levels, and depending on your choice,

the length of the words to guess will be different.

Have a go, see if you can guess the word, or if you get hung!

## Table of contents

- [Hangman](#hangman)
  - [Introduction](#introduction)
  - [Table of contents](#table-of-contents)
  - [User goals](#user-goals)
    - [Goals of the website](#goals-of-the-website)
    - [Goals of the user](#goals-of-the-user)
  - [User stories](#user-stories)
      - [Website owner](#website-owner)
      - [General user](#general-user)
      - [New user](#new-user)
  - [Design](#design)
  - [Features](#features)
    - [Welcome screen and game select](#welcome-screen-and-game-select)
  - [Bugs](#bugs)
    - [Bug 1](#bug-1)
  - [Fixed bugs](#fixed-bugs)
    - [Bug 1](#bug-1)

## User goals

### Goals of the website

- The goal of the website is to provide a command-line based game for entertainment.

- The instructions are easy to understand.

- The program handles user error.

- The program has no internal errors.

- The game can be played multiple times due to a large amount of words supplied,
  
  and different difficulty settings.

### Goals of the user

- The user wants to play a word-based game with a large variety of words.

- They want to be able to choose difficulty.

- The game should be easy to understand.

## User stories

### Website owner

- As the owner of the website, I want to create a user-friendly game that is accessible
  
  to as many people as possible through sipmple user interface.

- I want to tailor the game to people of different skill levels, so having difficulty
  
  settings will allow players to choose the setting they prefer.

- The library of words must be large to help prevent repetition.

### General user

As a user I expect the game to run without errors.

The game shows me progress, what letters I have used, and what letters I guessed correcly.

If I make an input that is not valid, the game should tell me what went wrong and what

was expected, without crashing.

As I grow increasingly better at the game, I want to be able to pick between difficulty

settings, that will provide longer or shorter words.

### New user

As a new user of the website, I expect to quickly understand how to play the game.

My inputs, if I get something wrong, will not break the game, but instead tell me what

went wrong and what was expected.

## Design

As part of the design process I layed out a flowshart for my codes logic,

and you can se it here: ![flowshart here.](documentation/flowshart/hangman.png)

## Features

### Welcome screen and game select

- When you first open the game, a welcome message will greet you.

- The game will then ask you to choose a difficulty level.

![Welcome and game select](documentation/images/welcome_game_select.png)

- If you do not enter a valid choice, the game will tell you, and then tell you what is expected.

![Validation game select](documentation/images/game_select_error_handling.png)

## Bugs

### Bug 1

When the game is played, the hangman diplays the wrong drawing.

For example, when lives left are 6, the hangman for 5 lives is displayed.

![lives bug](documentation/images/lives_bug.png)

## Fixed bugs

### Bug 1

I found an issue in the main game loop that caused this bug.

I was calling the lives function, on line 176, that decrements lives_left,

after I had already decremented the lives_left variable on line 174.

![Bug 1 found](documentation/images/lives_bug_found.png)

This was fixed by calling the lives function before I decrement the lives_left variable in the else statement.

![Bug 1 fixed](documentation/images/lives_bug_fix.png)
