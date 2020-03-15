# Citrics Bot

## Inspiration

I spent the last two years working abroad in Shenzhen, China. I worked for a company that owned a couple dozen e-commerce platforms and a few OEM Brands. Being one of two foreigners working in a mid-size Chinese company, my role was “to make things better across all platforms, products, and brands”. Needless to say I had a lot of responsibilities. The 996 work culture in China can be tiring; and 12 hour days can take a toll on your mental health, but this lifestyle gave me the opportunity to independently make high impact business decisions on a weekly basis.

One of the high impact decisions I made was to implement a Messenger Marketing Strategy for each and every one of our platforms and brands. I spent months training various marketing departments how to use third-party Bot services like Manychat and Chatfuel. I taught them how to run JSON ads and bring down the cost per-click while maintaining the ability to retarget in a more direct way. I help them build flows that delivered unique Amazon Coupons. I also helped them link Messenger flows to QR codes to bring offline store traffic into the digital space. I became passionate about the Messenger Ecosystem and the endless number of business optimizations it offered. 

After a few months of developing simple business bots I had the idea of “Dynamically generated content”. I wanted to create an engine that relied on user feedback to continually generate relevant content.
CitricsBot is a proof of concept for Dynamic Content. All of the charts that are rendered via the CitricsBot flow do not exist until the user requests them.

## What it does

Citris Bot takes user input about Cities and Town in the US and renders stats and metrics relevant to the user request.

A user can view over 50 different metrics by clicking through the flow or by directly typing a specific metric they are looking for. Users can also compare two Cities/Towns side-by-side.

![alt text](https://github.com/matthew-sessions/Citrics_messenger_bot/blob/master/pics/flow.png "flow")

## How I built it

The City/Town data is stored in a NoSQL database. The bot is powered by two separate Flask apps. The first flask app generates the charts/pictures. Each type of chart has a different endpoint. The endpoint requires one or two city ids (ids found in the NoSQL DB). The Flask app pulls the city data from the DB and then renders a chart. The chart is converted to a png and then sent to the endpoint using Flask’s “send_file” function. 

The second app takes the user response from the Facebook Message API. There are two types of responses it looks for - ‘text’ or ‘post_back’. If the response from the user is text that means the user typed something. The text is placed into a predictive model built using the Sklearn TFIDF vectorizer and the Cosine Similarities model. This NLP model maps the result to a function that corresponds with the response. When the corresponding function is called it fires a response to the user. 
If the response is a post_back the app knows the user clicked a button. Each payload for every button is mapped to a response function. So when a payload is returned the app fires a response from the corresponding function. 

User Messages are stored in a PostgreSQL Database. There are two tables. One table that stores all the messages. The other table stores the City or Cities the user is currently looking at. If a user types in a new City this row is updated. 

#### Tech Stack
* Python
* Flask
* Sklearn
* Jupyter Notebooks
* Docker
* AWS
* MongoDB
* PostgreSQL

![alt text](https://github.com/matthew-sessions/Citrics_messenger_bot/blob/master/pics/flowchart.png "flow")

## Challenges I ran into

## Accomplishments that I'm proud of

## What I learned

## What's next for CitricsBot
