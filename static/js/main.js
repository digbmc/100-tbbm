console.log('JavaScript is working!');

// var data = fetch('/data.json')
//         .then(response => {
//             if (!response.ok) {
//                 throw new Error('Network response was not ok');
//             }
//             return response.json();
//         })
//         .then(data => {
//             console.log(data); // 'data' is the JSON object variable
//             // You can now use the 'data' object
//         })
//         .catch(error => console.error('Error loading JSON:', error));


// console.log(data['sheets']);

// fetch('/data.json')
//     .then((response) => response.json())
//     .then(data => {
//         console.log(data)
//     });

//var data = JSON.parse(jsonData);

// var data = {{ jsonData|tojson()}};

// var category = data.sheets[2]["category"];

// console.log(category);

document.addEventListener('DOMContentLoaded', function() {
    var button = document.getElementById('colorButton');
    button.addEventListener('click', function() {
        window.location.reload();
        // var colors = ['pink', 'purple', 'red'];
        // var randomColor = colors[Math.floor(Math.random() * colors.length)];
        // button.style.backgroundColor = randomColor; // Change to any color you like
    });
});




// document.getElementById('demo').innerText = 'Hello JavaScript!';

// function test() {
//     document.getElementById('demo').innerText = 'Hello JavaScript!';
// };


// function reload(){
//     Window.location.reload();
// };




