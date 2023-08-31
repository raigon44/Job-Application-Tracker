
var check_user_password_match = function() {
    if (document.getElementById('user_password').value == document.getElementById('confirm_password').value) {
        document.getElementById('password_match_msg').style.color = 'green'
        document.getElementById('password_match_msg').innerHTML = 'both password match'
    } else {
        document.getElementById('password_match_msg').style.color = 'red'
        document.getElementById('password_match_msg').innerHTML = 'password NOT matching'
    }
}

function create_user_account() {

    const user_data = {
        "first_name": document.getElementById("firstname").value,
        "last_name": document.getElementById("lastname").value,
        "email": document.getElementById("user_email").value,
        "password": document.getElementById("user_password").value
    };

    fetch('/createaccount', {
        'method': 'POST',
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': JSON.stringify(user_data)
    })
    .then(response => {
        console.log("Recived the status code: ", response.status)
        console.log(response)
    })
    .catch(error => {
        console.error('Error: ', error)
        throw error
    });

}


//function login() {
//    fetch('/login', {
//        'method': 'GET',
//    })
//}

//$(document).ready(function() {
//  $('#loginModal').modal('show');
//  $(function () {
//    $('[data-toggle="tooltip"]').tooltip()
//  })
//});