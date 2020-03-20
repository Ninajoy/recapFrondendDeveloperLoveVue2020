# A recap of Frontend Developer Love Amsterdam 2020

So normally when I go to a conference, it's all about watching awesome people talk about awesome things, meeting awesome people and talk to them about awesome things, play awesome games, eat awesome food, take fun(ny) pictures, go home, The End.

However, this time i promised Fellow Frontend Guildies to show them a recap of the 3 day conference [Frontend Developer Love](https://www.frontenddeveloperlove.com/). Which is why i setup this project.

The project's goal is to put in practise what I've learned and to show what I think were the highlights.

Which means: this is a completely subjective recap of the conference and if you are interested in the objective parts: please go to [the Frontend Love youtube channel where all talks will be posted](https://www.youtube.com/channel/UC1nBp6ouBB1o5P8YvPznPOw)

Most images are screenshots from slides or pictures shared on Twitter and Facebook. Some pictures i've made myself.

## How to read/use this project

Because i want to try out some of the awesomeness the speakers talked about and because some of these solutions don't work together i have created several folders and commits in which i explore different kind of awesomenesses. This means this document will change every commit.

This commit contains the following:
	api folder
	nuxt_client folder

### Installing this project

Backend
Make sure you have python and pip installed
$ pip install pipenv
$ pipenv shell
$ pipenv install
$ cd api
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py loaddata fixtures/talks.json
$ python manage.py createsuperuser
$ python manage.py runserver
http://localhost:8000/admin/
http://localhost:8000/api/talks/

Frontend
$ cd client
$ npm install
$ npm run dev

## Speakers & Talks Overview

## Day 1

 How thinking small is changing software development big time by Sander Hoogendoorn

 How to Pack your Webpack by Johannes Ewald

 Svelte: the last framework we need? by Alexander Esselink

 Serverless gives you wings by Yan Cui

 Modern Solutions for e2e testing by Anastasiia Dragich

 Practical A11Y for Web Apps by Bob Bijvoet*

 Micro-interactions with React Spring by Emma Bostian

 But, you're not Facebook by Kitze

 Beats, Rhymes and Unit Tests by Tony Edwards

 GraphQL Without a Database by Roy Derks

 DX is the new black. Learnings from using Nuxt and Storybook at scale by Aurélie Violette*

 Refactor your life by Noer Paanakker & Sima Milli*

 Blazor with WebAssembly by Don Wibier*

 Audio Streaming - Using WebRTC for building your own Voice AIs by Lee Boonstra*

 The Future of Real-time | Offline | Data by Nader Dabit*

 The state of WebAssembly by Sendil Kumar*

## Day 2

 State of the Vuenion 2020 by Evan You

 Scalable Vue Graphics for the Modern Web by Dima Vishnevetsky

 The Future of Vue's Test Utils by Jessica Sachs

 Introduction into the Composition API by Gregg Pollack

 Composition API Best Practices by Thorsten Lünborg

 Making eCommerce sexy again with Vue Storefront and Composition API by Filip Rakowski

 Serverless with Vue and Node.js by Roman Kuba

 Climate change and the tech community by Callum Macrae

 Application Shortcuts with a Renderless Event Component by Rolf Haug

 Vue Announcer - Content Loading That Isn't Broken by Maria Lamardo

 Team First by Tim Benniks

 What is Nuxt 2020?! by Sébastien Chopin

 Deep Dive into Nuxt.js by Pooya Parsa

## Day 2

 An Animated Guide to Vue 3 Reactivity and Internals by Sarah Drasner*

 Vuelidate version for Vue 3.0 by Damian Dulisz*

 Authentication from Scratch by Adam Jahr

 Test-Driven Development with Vue.js by Sarah Dayan

 Vuetify 2+ by John Leider

 New Vue. New Compiler. Let’s unbox by Rahul Kadyan

 You might not need Vuex by Natalia Tepluhina

 Vuex ORM – Relational data management in Vue by Kia King

 BootstrapVue - The road to 2.0 and Beyond by Jacob Müller

 Micro Frontends: Composing a Greater Whole by Yoav Yanovski

 What you'll love in Vue 3 by Alex Kyriakidis*

 Performant Components through Customization by Maya Shavin*

 Announcement related to Vue CLI UI by Guillaume Chau*

 vue-router and its techniques by Eduardo San Martin Morote*

 Building Blazing Fast Sites with Gridsome by Jake Dohm*

 Full Static with Nuxt by Debbie O'Brien*

\* All the talks i haven't seen live and researched "offline"
