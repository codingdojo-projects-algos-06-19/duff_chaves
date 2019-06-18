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
  })