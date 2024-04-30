function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');


$(document).ready(function () {
    $('#history').click(function () {
        var isToggled = $(this).prop('checked');
        var message = isToggled ? 'Button toggled on' : 'Button toggled off';

        $.ajax({
            url: '/preferences/change/',
            type: 'POST',
            headers: {
                'X-CSRFToken': csrftoken
            },
            data: {
                'message': message
            },
            success: function (response) {
                console.log(response);
            },
            error: function (error) {
                console.error('Error sending message:', error);
            }
        });
    });
});