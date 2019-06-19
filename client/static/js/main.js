$(document).ready(function() {
    $('#user-create-form').submit(function(e) {
        e.preventDefault()
        console.log('HERE')
        $.ajax({
            url: '/user/create',
            method: 'POST',
            data: $('#user-create-form').serialize(),
            success: function() {
                console.log('SUCCESS')
                location.href = '/user/thankyou'
                $('#user-create-form input').val("")
            },
            error: function(data) {
                console.log('ERROR')
                $("#alerts").html(data.responseText)
            }
        })
    });
    (function () {
        'use strict';
        window.addEventListener('load', function () {
            // Fetch all the forms we want to apply custom Bootstrap validation styles to
            var forms = document.getElementsByClassName('needs-validation');
            // Loop over them and prevent submission
            var validation = Array.prototype.filter.call(forms, function (form) {
                form.addEventListener('submit', function (event) {
                    if (form.checkValidity() === false) {
                        event.preventDefault();
                        event.stopPropagation();
                    }
                    form.classList.add('was-validated');
                }, false);
            });
        }, false);
    })();
    $('#user-login-form').submit(function(e){
        e.preventDefault()
        //console.log('LOGIN FORM')
        $.ajax({
            url: '/user/process_login',
            method: 'POST',
            data: $('#user-login-form').serialize(),
            success: function(){
                console.log('SUCCESS')
                location.href = '/user/welcome'
                // $.get('/user/welcome')
                $('#user-login-form input').val("")
            },
            error: function(data){
                console.log('ERROR: Invalid credentials!', data)
                $('#alerts').html(data.responseText)
            }
        })
    })
    // (function () {
    //     'use strict';
    //     window.addEventListener('load', function () {
    //         console.log('LOADING...')
    //         // Fetch all the forms we want to apply custom Bootstrap validation styles to
    //         var forms = document.getElementsByClassName('needs-validation');
    //         // Loop over them and prevent submission
    //         var validation = Array.prototype.filter.call(forms, function (form) {
    //             form.addEventListener('submit', function (event) {
    //                 if (form.checkValidity() === false) {
    //                     event.preventDefault();
    //                     event.stopPropagation();
    //                 }
    //                 form.classList.add('was-validated');
    //             }, false);
    //         });
    //     }, false);
    // })();
  })