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