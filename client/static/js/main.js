$(document).ready(function() {
    $(function () {
        $('[data-toggle="popover"]').popover()
    });
    // popovers initialization - on click
    $('[data-toggle="popover-click"]').popover({
        html: true,
        trigger: 'click',
        placement: 'right',
        content: function () { return '<img id="img-item-list" src="' + $(this).data('img') + '" />'; }
    });
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
                // $('.btn-profile-update').html('<span class="spinner-border spinner-border-sm mr-2" role="status" aria-hidden="true"></span>Saving...').addClass('disabled');
                $("#alerts-info").html(alerts)
            },
            error: function(data) {
                console.log('ERROR')
                $("#alerts").html(data.responseText)
            }
        })
    });
    $('.admin-user-update-form').submit(function(e) {
        var FORM_USER_ID = $('input[name="user-id"]').val();
        console.log('1FORM_USER_ID: ', FORM_USER_ID)
        e.preventDefault()
        $.ajax({
            url: '/admin/user/update/' + FORM_USER_ID,
            method: 'POST',
            data: $('#admin-user-update-form-'+FORM_USER_ID+'').serialize(),
            success: function(alerts) {
                //console.log('2FORM_USER_ID: ', FORM_USER_ID)
                $('.btn-update').html('<span class="spinner-border spinner-border-sm mr-2" role="status" aria-hidden="true"></span>Saving...').addClass('disabled');
                console.log('SUCCESS')
                $("#alerts-info").html(alerts)
                setTimeout("window.location.replace('/admin/users');",2000);
                //window.location.replace('/admin/users')
            },
            error: function(data) {
                console.log('ERROR')
                //console.log('3FORM_USER_ID: ', FORM_USER_ID)
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
                $('.btn-login').html('<span class="spinner-border spinner-border-sm mr-2" role="status" aria-hidden="true"></span>Loading...').addClass('disabled');
                setTimeout("window.location.replace('/user/welcome');",3000);
            },
            error: function(data){
                console.log('ERROR: Invalid credentials!', data)
                $('#alerts').html(data.responseText)
            }
        })
    })
    $('#item-create-form').submit(function(e) {
        e.preventDefault()
        console.log('HERE')
        $.ajax({
            url: '/admin/item/create',
            method: 'POST',
            data: $('#item-create-form').serialize(),
            success: function() {
                console.log('SUCCESS')
                $('.btn-add-item').html('<span class="spinner-border spinner-border-sm mr-2" role="status" aria-hidden="true"></span>Saving').addClass('disabled');
                setTimeout("window.location.replace('/admin/items');",2000);
                //$('#user-create-form input').val("")
            },
            error: function(data) {
                console.log('ERROR')
                $("#alerts").html(data.responseText)
            }
        })
    });
    $('#admin-item-update-form').submit(function(e) {
        var FORM_ITEM_ID = $('input[name="item-id"]').val();
        console.log('FORM_ITEM_ID: ', FORM_ITEM_ID)
        e.preventDefault()
        $.ajax({
            url: '/admin/item/update/' + FORM_ITEM_ID,
            method: 'POST',
            data: $('#admin-item-update-form').serialize(),
            success: function(alerts) {
                $('.btn-item-update').html('<span class="spinner-border spinner-border-sm mr-2" role="status" aria-hidden="true"></span>Saving...').addClass('disabled');
                console.log('SUCCESS')
                $("#alerts-info").html(alerts)
                setTimeout("window.location.replace('/admin/items');",2000);
            },
            error: function(data) {
                console.log('ERROR')
                $("#alerts").html(data.responseText)
            }
        })
    });
    $('#admin-tour-create-form').submit(function(e) {
        e.preventDefault()
        console.log('HERE')
        $.ajax({
            url: '/admin/tour/create',
            method: 'POST',
            data: $('#admin-tour-create-form').serialize(),
            success: function() {
                console.log('SUCCESS')
                $('.btn-add-tour').html('<span class="spinner-border spinner-border-sm mr-2" role="status" aria-hidden="true"></span>Saving').addClass('disabled');
                setTimeout("window.location.replace('/admin/tours');",2000);
                //$('#user-create-form input').val("")
            },
            error: function(data) {
                console.log('ERROR')
                $("#alerts").html(data.responseText)
            }
        })
    });
    $('#admin-tour-update-form').submit(function(e) {
        var FORM_TOUR_ID = $('input[name="tour-id"]').val();
        console.log('FORM_TOUR_ID: ', FORM_TOUR_ID)
        e.preventDefault()
        $.ajax({
            url: '/admin/tour/' + FORM_TOUR_ID + '/update',
            method: 'POST',
            data: $('#admin-tour-update-form').serialize(),
            success: function(alerts) {
                $('.btn-tour-update').html('<span class="spinner-border spinner-border-sm mr-2" role="status" aria-hidden="true"></span>Saving...').addClass('disabled');
                console.log('SUCCESS')
                $("#alerts-info").html(alerts)
                setTimeout("window.location.replace('/admin/tours');",2000);
            },
            error: function(data) {
                console.log('ERROR')
                $("#alerts").html(data.responseText)
            }
        })
    });
    $('#admin-tour-delete-form').submit(function(e) {
        var FORM_TOUR_ID = $('input[name="tour-id"]').val();
        console.log('FORM_TOUR_ID: ', FORM_TOUR_ID)
        e.preventDefault()
        $.ajax({
            url: '/admin/tour/' + FORM_TOUR_ID + '/delete',
            method: 'POST',
            data: $('#admin-tour-delete-form').serialize(),
            success: function(alerts) {
                // $('#btn-tour-delete').html('<span class="spinner-border spinner-border-sm mr-2" role="status" aria-hidden="true"></span>Deleting...').addClass('disabled');
                console.log('REMOVED ITEM')
                $("#alerts-info").html(alerts)
                setTimeout("window.location.replace('/admin/tours');",2000);
            },
            error: function(data) {
                console.log('ERROR')
                $("#alerts").html(data.responseText)
            }
        })
    });
    $('#add-to-cart-form').submit(function(e) {
        // $('#add-to-cart').html('<span class="spinner-border spinner-border-sm mr-2" role="status" aria-hidden="true"></span>').addClass('disabled');
        // function loading(message) {
        //     append_html = setTimeout(function(){  }, 3000);
        //     return append_html
        //   }
       // var FORM_ITEM_CART_ID = $('input[name="add-cart-item-id"]').val();
        // e.preventDefault()
        // $.ajax({
        //     url: '/item/add_to_cart/' + FORM_ITEM_CART_ID,
        //     method: 'POST',
        //     data: $('#add-to-cart-form').serialize(),
        //     success: function() {
        //         console.log('ADDED ITEM')
                // var $this = $('#add-to-cart');
                // $this.html('<span class="spinner-border spinner-border-sm mr-2" role="status" aria-hidden="true"></span>Adding...');
                // $this.attr('disabled', true);
                // setTimeout(function() { 
                //     $this.attr('disabled', false);
                //     $this.hide();
                // }, 4000);
            //     $('#remove-from-cart').show(0).delay(2000)
            //     $('#add-to-cart').hide(0).delay(2000)
            // },
            // error: function(data) {
            //     console.log('ERROR')
            //     $("#alerts").html(data.responseText)
            // }
    });
    $('#remove-from-cart-form').submit(function(e) {
        // var FORM_ITEM_CART_ID = $('input[name="remove-cart-item-id"]').val();
        // e.preventDefault()
        // $.ajax({
        //     url: '/item/remove_from/' + FORM_ITEM_CART_ID,
        //     method: 'POST',
        //     data: $('#remove-from-cart-form').serialize(),
        //     success: function() {
        //         console.log('REMOVED ITEM')
                // var $this2 = $('#remove-from-cart');
                // $this2.html('<span class="spinner-border spinner-border-sm mr-2" role="status" aria-hidden="true"></span>Removing...');
                // $this2.attr('disabled', true);
                // setTimeout(function() { 
                //     $this2.attr('disabled', false);
                //     $this2.hide();
                // }, 4000);
    //             $("#add-to-cart").show(0).delay(2000);
    //             $("#remove-from-cart").hide(0).delay(2000);
    //         },
    //         error: function(data) {
    //             console.log('ERROR')
    //             $("#alerts").html(data.responseText)
    //         }
    //     })
    });
    $.get('/song/play', function(player_html){
        console.log('PLAYER: ', player_html)
        $('.song-player').html('<audio controls src="' + player_html + '"></audio>');
    });

    $.get('/player', function(player_html){
        console.log('PLAYER: ', player_html)
        $('#player').html('<audio controls src="' + player_html + '"></audio>');
    });
   
    //Make the footer stick to the bottom of the page.
    // function setBodyForFooter() {
    //     $("#footer").show();
    //     $("body").css("margin-bottom", parseInt($("#footer").css("height") + "px"));
    // }
    // $(window).on('load', function(){
    //     setBodyForFooter();
    // });
    // $(window).resize(function () {
    //     setBodyForFooter();
    // });
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