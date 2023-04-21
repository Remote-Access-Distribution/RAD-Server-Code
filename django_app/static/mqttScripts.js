// This is javascript to send a post request in with the distro data
function sendMqttMessage(distro, socket, state) {
    $.ajax({
        url: 'distro_change_state_request/',
        type: 'POST',
        headers: { 'X-CSRFToken': '{{ csrf_token }}' },
        data: {
            distro: distro,
            socket: socket,
            state: state
        },
        error: function(error) {
            console.log(error);
        }
    });
}