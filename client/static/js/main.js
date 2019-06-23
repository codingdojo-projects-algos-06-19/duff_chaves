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
                $('.btn-register').html('<span class="spinner-border spinner-border-sm mr-2" role="status" aria-hidden="true"></span>Loading...').addClass('disabled');
                setTimeout("window.location.replace('/user/thankyou');",2000);
                //$('#user-create-form input').val("")
            },
            error: function(data) {
                console.log('ERROR')
                $("#alerts").html(data.responseText)
            }
        })
    });
    $('#user-update-form').submit(function(e) {
        e.preventDefault()
        $.ajax({
            url: '/user/update/' + CURRENT_USER_ID,
            method: 'POST',
            data: $('#user-update-form').serialize(),
            success: function(alerts) {
                console.log('SUCCESS')
                $("#alerts").html(alerts)
            },
            error: function(data) {
                console.log('ERROR')
                $("#alerts").html(data.responseText)
            }
        })
    });
    $('.admin-user-update-form').submit(function(e) {
        var FORM_USER_ID = $('input[name="user-id"]').val();
        //console.log('1FORM_USER_ID: ', FORM_USER_ID)
        e.preventDefault()
        $.ajax({
            url: '/admin/user/update/' + FORM_USER_ID,
            method: 'POST',
            data: $('form').serialize(),
            success: function(alerts) {
                //console.log('2FORM_USER_ID: ', FORM_USER_ID)
                $('.btn-update').html('<span class="spinner-border spinner-border-sm mr-2" role="status" aria-hidden="true"></span>Saving...').addClass('disabled');
                console.log('SUCCESS')
                $("#modal-alerts").html(alerts)
                setTimeout("window.location.replace('/admin/users');",2000);
                //window.location.replace('/admin/users')
            },
            error: function(data) {
                console.log('ERROR')
                //console.log('3FORM_USER_ID: ', FORM_USER_ID)
                $("#modal-alerts").html(data.responseText)
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
                $('.btn-login').html('<span class="spinner-border spinner-border-sm mr-2" role="status" aria-hidden="true"></span>Loading...').addClass('disabled');
                setTimeout("window.location.replace('/user/welcome');",3000);
            },
            error: function(data){
                console.log('ERROR: Invalid credentials!', data)
                $('#alerts').html(data.responseText)
            }
        })
    })
    $.get('/player', function(player_html){
        console.log('PLAYER: ', player_html)
        $('#player').html('<audio controls src="' + player_html + '"></audio>');
    });
    // SC.initialize({
    //     client_id: 'FvkgucGq5QyPAepKyYOUkjEQq2zLVKPb'
    //   });      
    // //   SC.get('/tracks', {
    // //     genres: 'punk', bpm: { from: 120 }
    // //   }).then(function(tracks) {
    // //     console.log(tracks);
    // //   });
    // SC.initialize({
    //     client_id: 'FvkgucGq5QyPAepKyYOUkjEQq2zLVKPb'
    //   });
    //   // stream track id 293
    // //   SC.stream('/tracks/293').then(function(player){
    // //     player.play().then(function(){
    // //       console.log('Playback started!');
    // //     }).catch(function(e){
    // //       console.error('Playback rejected. Try calling play() from a user interaction.', e);
    // //     });
    // //   });
    // // (function () {
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