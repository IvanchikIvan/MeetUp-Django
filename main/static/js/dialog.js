let openDialogBtn = document.getElementById("open-dialog-btn");
let closeDialogBtn = document.getElementById("close-dialog-btn");
let dialogOverlay = document.getElementById("dialog-overlay");

openDialogBtn.addEventListener("click", function () {
    dialogOverlay.style.display = "flex";
});

closeDialogBtn.addEventListener("click", function () {
    dialogOverlay.style.display = "none";
});

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
    $('#create_meet').click(function () {
        let meet_name = $("#meet_name").val();
        
        // Example JSON data
        const data = {
            meet_name: meet_name
        };

        // Stringify JSON object
        const jsonData = JSON.stringify(data);

        $.ajax({
            url: '/create/meet/',
            type: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,
            },
            data: jsonData,
            success: function (response) {
                meet_id = response.meet_id;
                window.location.href = `/meet/${meet_id}/`
            },
            error: function (error) {
                console.error('Error sending message:', error);
            }
        });
    });
});