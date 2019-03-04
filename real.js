var socket;
const MAX_INT = Math.pow(2, 16 - 1) - 1; 	// Need the maximum value for 16-bit
var ws = new WebSocket("ws://127.0.0.1:5678/");
ws.onmessage = function (event) {
    console.log(event.data);
};



var handleSuccess = function (stream) {
    
    var context = new AudioContext({sampleRate: 16000});
    var source = context.createMediaStreamSource(stream);
    var processor = context.createScriptProcessor(256, 1, 1);

    source.connect(processor);
    processor.connect(context.destination);

    processor.onaudioprocess = function (e) {
        // Do something with the data, i.e Convert this to WAV
        //console.log(e.inputBuffer);
        ws.send(e.inputBuffer);
    };
};

navigator.mediaDevices.getUserMedia({ audio: true, video: false })
    .then(handleSuccess);