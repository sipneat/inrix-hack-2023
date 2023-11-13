## inrix-hack-2023
## Inspiration
You are going to the Chase Center to see the Warriors win yet another game. Then five minutes away, you realize you forgot to account for the extra $60 cost of parking. What do you do? Drive around wasting time to find free parking? Wasting gas to try to avoid the extra cost? This is a major issue that has caused the average person to lose 17 hours of their life looking for parking costing them an average $345. This issue can easily be solved through our product Parking++.

##Slogan
Parking So Nice, We Added it Twice.

## What it does
Parking++ is a web app that aims to help you find parking suitable to your needs. Users can adjust parameters such as the distance from location, cost, and availability of parking. And then onto this the user can then use Google Street View to preview where they can park. Essentially creating a user friendly environment to solve all their parking needs.

## How we built it
For our front end, we used Figma to create a framework for our website. We used to code from Figma in Vue.js as a base to build off and make the entire user interface. Our backend is built off of Flask making use of the INRIX Blocks API to generate our dataset. 

## Challenges we ran into
For our front end, making the buttons function along with editing small details of the design such as margins being slightly off caused errors. The implementation of Google Maps into the web app was the hardest part and caused glitches within the website. We also realized our choice of Vue limited us in a sense since we realize Vue helps with product scalability a ton, but has a negative impact on building the base functionality since sending data between components is quite a hassle. Which is why we came to the conclusion that if we accounted for this sooner Angular would've suited our needs better, especially with some available plug-ins. Along with that we had a lot of raw HTML and CSS elements which mean we had to account for many minor factors, on various displays, and minor adjustments. Which is what added to our difficulty when it came to implementing our search bar and buttons.

## Accomplishments that we're proud of
The Accomplishment we are most proud of has to come down to our Google Maps Integration. When it came to the planning stages of our project we knew ease of use and a Consumer-Centric product is what our team wanted to accomplish. Which having the Google Maps Integration with an Accessible Street View, so users can see their parking spots ahead of time and get an idea of where they would be looking to go, felt as though we really tied the project back to our goal of being a Consumer-Centric product.

## What we learned
We learned how to use frameworks, and how HTML, CSS, and Javascript can play various roles depending on the framework you are using since the scope of a project can change based off that decision. The intricacies of Vue was a big one learning how for our needs other frameworks may have been better when it comes to sharing data between our components. But how the Vue framework can make a product easily scalable for developers. And in regards to the backend, we were able to improve upon our API integration skills, since we had to call upon multiple API's being the INRIX Block's, Google Maps Javascript, and the Token API we were accessing. And the Flexibility of Flask allowed us to accomplish this within a timely manner so we can work on expanding the feature set of our product. And finally, it was super exciting to learn how to host through the cloud with AWS.

## What's next for Parking++
With Parking++ we were able to accomplish the general gist of what we set out to do. But that does not mean we got to every feature we wanted to implement. The next steps would essentially to build off the versatility for the user. There were a few parameters we originally set out to account for, but was not possible for us to accomplish within the time constraints, which were to take in inputs regarding size of the users' vehicle, capacity of the lot, access to chargers for EV's, and more. Along with that refining the current features would definitely be a must to start off, since we felt as though the lack of our functioning search to make readjustments into the Google Maps API, really took away from the user experience, but this issue is also something that could be easily fixed given more time to deliver a more complete product to our users.
