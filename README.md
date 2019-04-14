## Inspiration

Some languages, like English, have highly varied pronunciations. The Americans, the British, the Chinese, the Australians, the Indians - all have their own prosody and enunciations, which make their version of English very different from others.  We all have faced difficulty in understanding the foreign versions of English which limits our capability to socialize and interact effectively with people of different cultures and backgrounds than us. We, especially being International students have faced this problem in our day-to-day life. It can get both embarrassing and frustrating at the same time.

We want to bridge this gap by eliminating this barrier altogether so that we can understand others and express ourselves 100%. With "To-may-to To-mah-to" we hope to solve this problem and become more confident and comfortable in our day-to-day interaction. 

The name "To-may-to To-mah-to" is inspired by the [classic song](https://www.youtube.com/watch?v=zZ3fjQa5Hls) by Louis Armstrong and Ella Fitzgerald.


## What it does
"To-may-to To-mah-to" is a web application which takes one accent as input, runs our accent-conversion algorithm and produces the desired accent as output so that we can understand the other person better. Our product currently supports Voice and Video Calls.

## How we built it
We have designed the front end using React and deployed it using [AWS Amplify](https://aws-amplify.github.io). Real-time communication is established using [Pusher Channels](https://pusher.com/channels). 
The first version of this product uses Google's Speech to Text and Text to Speech API to map accents. Google Speech APIs provides us with information about each words timestamp in the audio. This helps us to determine the duration and the location of pauses in speech and the speaking rate. Further, we extended this idea to do direct Speech to speech translation using Neural Networks. One of the approaches uses Mel Frequency Cepstral Coefficient and another uses LSTMs/RNNs.

## Challenges we ran into
Automatic Speech Recognition Systems have a lot of challenges, the biggest one being effectively handling accents. Neural Style Transfer and Neural Voice Cloning are the biggest challenges. We currently use a different voice which does not provide as much real-life experience as that of the user's voice. To solve this problem we need to train our model on the user's voice to generate a similar voice. We can solve this problem by prompting the users to create their own vocal avatar using applications like [Lyrebird](https://lyrebird.ai) API. Converting vanilla javascript to react native turned out to be challenging as well.

## Accomplishments that we're proud of
Despite many challenges, we were able to create a working prototype of the application which successfully converts the accent into the desired accent and encourages people to have more satisfactory interactions by removing one of the biggest barriers in communication.

## What we learned
We learned a lot in terms of both technical and behavioral aspects. We started with learning how to use GCP's API to how to host our product on AWS. We then explored how to use ANN, MFCCs, and CNN to build a model for Automatic Speech to Speech Translation. Besides, learning a lot of technical stuff, we also learned a lot of other more important things like patience and never giving up. We experienced the magic of team-work and how we can learn a lot from one another. We learned to reach out for help, when needed and got some amazing guidance. This hackathon was a life-changing experience for all of us and one that we will never forget.

## What's next for To-may-to To-mah-to?
We really want to enhance all the features of "To-may-to To-mah-to" to make it more accurate, user-friendly and easier to use. We would love to give it the real-life touch so that it is more natural. We also plan to render the video, especially the lip movements so that they are aligned and in perfect sync with the target audio file. We plan to make our product as close to real-time as possible so that our users can use it with absolutely no time lag.

Currently, our model just supports English due to the available training data and simplicity of development. We can also, later, extend our model to include other languages.

## Authors:
- Duy Nguyen
- Edgar Yu
- Indu Manimaran
- Surbhi Batra
- Vishal Seshagiri
