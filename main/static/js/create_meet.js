document.addEventListener('DOMContentLoaded', function () {
    let form = document.getElementById('restaurant-filter-form');
    form.addEventListener('submit', function (event) {
        event.preventDefault();
        sendData();
    });
});

function sendData() {
    let features = document.querySelector('select[name="features"]').value;
    let cuisine = document.querySelector('select[name="cuisine"]').value;

    let client = {
        'features': [features],
        'cuisine': [cuisine]
    };

    console.log(client);
}
