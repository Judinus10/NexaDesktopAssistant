$(document).ready(function () {
    

    $('.text').textillate({
        loop:true,
        sync:true,
        in:{
            effect:"bounceIn",
        },
        out:{
            effect:"bounceOut",
        },
    })

    // Siri configuration
    var siriWave = new SiriWave({
        container: document.getElementById("siri-container"),
        width: 800,
        height: 200,
        style: "ios9",
        amplitude: "1",
        speed: "0.30",
        autostart: true
      });

    // Siri message animation
    $('.siri-message').textillate({
        loop: true,
        sync: true,
        in: {
            effect: "fadeInUp",
            sync: true,
        },
        out: {
            effect: "fadeOutUp",
            sync: true,
        },

    });

    //mic button click animation
    $("#button").click(function () { 
        eel.playAssistantSound()
        $("#Oval").attr("hidden", true);
        $("#siriWave").attr("hidden", false);
        eel.allCommands()()
    });

    function doc_keyUp(e) {
        // this would test for whichever key is 40 (down arrow) and the ctrl key at the same time

        console.log("Key pressed: ", e.key);

        if (e.key === 'b' && (e.ctrlKey || e.metaKey)) {
            console.log("Ctrl+J or Cmd+J detected");
            eel.playAssistantSound()
            $("#Oval").attr("hidden", true);
            $("#siriWave").attr("hidden", false);
            eel.allCommands()
        }
    }
    document.addEventListener('keyup', doc_keyUp, false);

    // toogle fucntion to hide and display mic and send button 
    function ShowHideButton(message) {
        if (message.length == 0) {
            $("#MicBtn").attr('hidden', false);
            $("#SendBtn").attr('hidden', true);
        }
        else {
            $("#MicBtn").attr('hidden', true);
            $("#SendBtn").attr('hidden', false);
        }
    }
});