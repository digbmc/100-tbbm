console.log('JavaScript is working!');

document.addEventListener('DOMContentLoaded', function() {
    var button = document.getElementById('colorButton');
    button.addEventListener('click', function() {
        var colors = ['pink', 'purple', 'red'];
        var randomColor = colors[Math.floor(Math.random() * colors.length)];
        button.style.backgroundColor = randomColor; // Change to any color you like
    });
});

// document.addEventListener('DOMContentLoaded', function() {
//     var button = document.getElementById('colorButton');
//     button.addEventListener('click', function() {
//         var colors = ['pink', 'purple', 'red'];
//         var randomColor = colors[Math.floor(Math.random() * colors.length)];
//         button.style.backgroundColor = randomColor;
//     });
// });


// document.getElementById('demo').innerText = 'Hello JavaScript!';

function test() {
    document.getElementById('demo').innerText = 'Hello JavaScript!';
};


function reload(){
    Window.location.reload();
};




