This project is a wev demonstration of the Mozilla DeepSpeech API

There is a front-end layer to capture the microphone stream and send it over a websocket to the backend.

The backend receives the stream, then performs VAD to create chunks of audio which are sent to the transcriber. The transcription is then sent via the same websocket to the front-end.

Since streaming decode hasn't been implemented in DeepSpeech this still works as it would on offline mode but will expand to accomodate that in the future. 
